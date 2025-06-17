import os # for file and directory manipulation
import pandas as pd  # for data manipulation and analysis
from sklearn.model_selection import train_test_split  # for splitting the dataset into training and testing sets
from sklearn.preprocessing import StandardScaler, LabelEncoder  # for feature scaling and encoding categorical variables
import joblib

# Create output directory
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

# Get the absolute path of the root directory of the project
BASE_DIR = os.path.abspath(os.path.join(os.getcwd(), ".."))

# Combine
csv_path = os.path.join(BASE_DIR, "personality_dataset_raw.csv")

# Load raw dataset
df = pd.read_csv(csv_path)

"""## Handling Missing Values"""

# Get numeric column that have missing values
missing_cols_numeric = df.select_dtypes(include="number").columns[df.select_dtypes(include="number").isnull().any()]

# Get object column that have missing values
missing_cols_object = df.select_dtypes(include="object").columns[df.select_dtypes(include="object").isnull().any()]

# Impute numerical columns with the median
for col in missing_cols_numeric:
    df[col].fillna(df[col].median(), inplace=True)

# Impute categorical columns with the mode
for col in missing_cols_object:
    if col in df.columns:
        df[col].fillna(df[col].mode()[0], inplace=True)

"""## Encoding Categorical Data"""

label_enc = LabelEncoder()

# Dictionary to store encoders
encoders = {}

# Encode categorical features
categorical_features = df.select_dtypes(include='object').columns.tolist()

# Get  numerical feature
numerical_features = df.select_dtypes(include=['number']).columns.tolist()

for col in categorical_features:
    label_enc = LabelEncoder()
    df[col] = label_enc.fit_transform(df[col])
    encoders[col] = label_enc

# Save the encoders for future decoding
joblib.dump(encoders, os.path.join(OUTPUT_DIR, "label_encoders.joblib"))

"""## Feature Scaling"""

X = df.drop(columns=['Personality'])
y = df['Personality']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X[numerical_features])

# Save the scaler
joblib.dump(scaler, os.path.join(OUTPUT_DIR, "scaler.joblib"))

"""## Combine Scaled Features with Encoded Categorical Features"""

# Convert scaled features back to DataFrame
X_scaled = pd.DataFrame(X_scaled, columns=numerical_features)

# Add encoded categorical features to the scaled DataFrame
for col in categorical_features:
    X_scaled[col] = df[col].values

# Reorder columns to match original DataFrame
X_scaled = X_scaled[X.columns]

"""## Split Data 80:20"""

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)

# Save train/test splits as CSV
pd.DataFrame(X_train, columns=X.columns).to_csv(os.path.join(OUTPUT_DIR, "X_train.csv"), index=False)
pd.DataFrame(X_test, columns=X.columns).to_csv(os.path.join(OUTPUT_DIR, "X_test.csv"), index=False)
y_train.to_csv(os.path.join(OUTPUT_DIR, "y_train.csv"), index=False)
y_test.to_csv(os.path.join(OUTPUT_DIR, "y_test.csv"), index=False)

"""## Export Data to CSV"""

# Save fully processed dataset
df_processed = pd.concat([X_scaled, y.reset_index(drop=True)], axis=1)

df_processed.to_csv(os.path.join(OUTPUT_DIR,"extrovert_introvert_processed.csv"), index=False)

print("✅ Preprocessing complete. File saved as 'extrovert_introvert_processed.csv'")