import os
import mlflow
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import StratifiedKFold
from tqdm import tqdm

# === Setup MLflow local or remote ===
mlflow.set_tracking_uri("http://127.0.0.1:5000/")
mlflow.set_experiment("Ekstrovert Introvert Modelling")

# === Load data ===
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PREPROCESS_DIR = os.path.join(BASE_DIR, "preprocessing", "output")

X_train = pd.read_csv(os.path.join(PREPROCESS_DIR, "X_train.csv"))
y_train = pd.read_csv(os.path.join(PREPROCESS_DIR, "y_train.csv")).squeeze()
X_test = pd.read_csv(os.path.join(PREPROCESS_DIR, "X_test.csv"))
y_test = pd.read_csv(os.path.join(PREPROCESS_DIR, "y_test.csv")).squeeze()

input_example = X_train.head(5)

# === Hyperparameter Tuning ===
n_estimators_range = np.linspace(10, 1000, 5, dtype=int)
max_depth_range = np.linspace(1, 50, 5, dtype=int)

best_accuracy = 0
best_params = {}
best_model = None

# === Grid Search with Cross-Validation & MLflow Logging ===
skf = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)
param_grid = [(n, d) for n in n_estimators_range for d in max_depth_range]

for n_estimators, max_depth in tqdm(param_grid, desc="Grid Search"):
    cv_accuracies = []
    for train_idx, val_idx in skf.split(X_train, y_train):
        X_tr, X_val = X_train.iloc[train_idx], X_train.iloc[val_idx]
        y_tr, y_val = y_train.iloc[train_idx], y_train.iloc[val_idx]
        model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
        model.fit(X_tr, y_tr)
        y_pred = model.predict(X_val)
        cv_accuracies.append(accuracy_score(y_val, y_pred))
    mean_cv_acc = np.mean(cv_accuracies)

    with mlflow.start_run():
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_metric("cv_accuracy", mean_cv_acc)

        # Train on full train set, evaluate on test set
        model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred, average="weighted", zero_division=0)
        rec = recall_score(y_test, y_pred, average="weighted", zero_division=0)
        f1 = f1_score(y_test, y_pred, average="weighted", zero_division=0)

        mlflow.log_metric("test_accuracy", acc)
        mlflow.log_metric("test_precision", prec)
        mlflow.log_metric("test_recall", rec)
        mlflow.log_metric("test_f1_score", f1)

        mlflow.sklearn.log_model(model, artifact_path="modelling", input_example=input_example)
        mlflow.log_artifact(os.path.join(PREPROCESS_DIR, "extrovert_introvert_processed.csv"), artifact_path="data")

        if acc > best_accuracy:
            best_accuracy = acc
            best_params = {"n_estimators": n_estimators, "max_depth": max_depth}
            best_model = model
    print(f"Logged modelling with n_estimators={n_estimators}, max_depth={max_depth}, test_accuracy={acc:.4f}")

# Log best model
if best_model is not None:
    with mlflow.start_run(run_name="Best_Model"):
        mlflow.log_param("n_estimators", best_params["n_estimators"])
        mlflow.log_param("max_depth", best_params["max_depth"])
        mlflow.log_metric("best_test_accuracy", best_accuracy)
        mlflow.sklearn.log_model(best_model, artifact_path="best_modelling", input_example=input_example)
        mlflow.log_artifact(os.path.join(PREPROCESS_DIR, "extrovert_introvert_processed.csv"), artifact_path="data")

print("Best accuracy:", best_accuracy)
print("🏆 Best parameters:", {k: int(v) for k, v in best_params.items()})