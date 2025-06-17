{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "kZLRMFl0JyyQ"
   },
   "source": [
    "# **1. Dataset Introduction**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "hssSDn-5n3HR"
   },
   "source": [
    "This dataset was obtained from Kaggle under the title **\"Extrovert vs. Introvert Behavior Data\"**.\n",
    "It contains personality traits like extroversion and introversion shape how individuals interact with their social environments. This dataset provides insights into behaviors such as time spent alone, social event attendance, and social media engagement, enabling applications in psychology, sociology, marketing, and machine learning. Whether you're predicting personality types or analyzing social patterns, this dataset is your gateway to uncovering fascinating insights\n",
    "\n",
    "* **Source**: [Extrovert vs. Introvert Behavior Data](https://www.kaggle.com/datasets/rakeshkapilavai/extrovert-vs-introvert-behavior-data)\n",
    "* **Data Type**: Structured (CSV)\n",
    "* **Target**: `Personality` column\n",
    "\n",
    "**Feature Descriptions** in the dataset:\n",
    "\n",
    "* **Time_spent_Alone**: Hours spent alone daily (0–11)\n",
    "* **Stage_fear**: Presence of stage fright (Yes/No)\n",
    "* **Social_event_attendance**: Frequency of social events (0–10)\n",
    "* **Going_outside**: Frequency of going outside (0–7)\n",
    "* **Drained_after_socializing**: Feeling drained after socializing (Yes/No)\n",
    "* **Friends_circle_size**: Number of close friends (0–15)\n",
    "* **Post_frequency**: Social media post frequency (0–10)\n",
    "* **Personality**: Target variable (Extrovert/Introvert)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "fKADPWcFKlj3"
   },
   "source": [
    "# **2. Import Library**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "| **Library**    | **Function**                                                                             |\n",
    "| -------------- | ---------------------------------------------------------------------------------------- |\n",
    "| `pandas`       | Used for reading and manipulating tabular data (e.g., CSV files).                        |\n",
    "| `numpy`        | Provides support for numerical operations, arrays, and mathematical tools.               |\n",
    "| `matplotlib`   | Basic plotting library for creating visualizations like line charts, bars.               |\n",
    "| `seaborn`      | Statistical visualization library built on top of matplotlib (e.g., heatmaps, boxplots). |\n",
    "| `scikit-learn` | Provides preprocessing tools, machine learning models, and evaluation metrics.           |\n",
    "| `joblib`       | Efficiently saves and loads Python objects like models, scalers, and encoders.           |\n",
    "| `os`           | Provides functions for interacting with the operating system (e.g., file paths).       |\n",
    "| `mlflow`       | Manages the machine learning lifecycle, including experimentation and deployment.       |\n",
    "| `python-dotenv`| Loads environment variables from a `.env` file for configuration management.            |\n",
    "| `dagshub`      | Enables version control and collaboration for machine learning experiments and datasets. |\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-25T04:46:24.158583Z",
     "start_time": "2025-05-25T04:46:21.823169Z"
    },
    "id": "BlmvjLY9M4Yj"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pandas in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (2.2.3)\n",
      "Requirement already satisfied: numpy in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (2.2.3)\n",
      "Requirement already satisfied: matplotlib in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (3.10.1)\n",
      "Requirement already satisfied: seaborn in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (0.13.2)\n",
      "Requirement already satisfied: scikit-learn in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (1.6.1)\n",
      "Requirement already satisfied: joblib in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (1.4.2)\n",
      "Requirement already satisfied: mlflow in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (3.1.0)\n",
      "Requirement already satisfied: dagshub in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (0.5.10)\n",
      "Requirement already satisfied: streamlit in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (1.43.0)\n",
      "Requirement already satisfied: python-dotenv in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (1.1.0)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from pandas) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from pandas) (2025.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from pandas) (2025.1)\n",
      "Requirement already satisfied: contourpy>=1.0.1 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from matplotlib) (1.3.1)\n",
      "Requirement already satisfied: cycler>=0.10 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from matplotlib) (0.12.1)\n",
      "Requirement already satisfied: fonttools>=4.22.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from matplotlib) (4.56.0)\n",
      "Requirement already satisfied: kiwisolver>=1.3.1 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from matplotlib) (1.4.8)\n",
      "Requirement already satisfied: packaging>=20.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from matplotlib) (24.2)\n",
      "Requirement already satisfied: pillow>=8 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from matplotlib) (11.1.0)\n",
      "Requirement already satisfied: pyparsing>=2.3.1 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from matplotlib) (3.2.1)\n",
      "Requirement already satisfied: scipy>=1.6.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from scikit-learn) (1.15.2)\n",
      "Requirement already satisfied: threadpoolctl>=3.1.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from scikit-learn) (3.6.0)\n",
      "Requirement already satisfied: mlflow-skinny==3.1.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from mlflow) (3.1.0)\n",
      "Requirement already satisfied: Flask<4 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from mlflow) (3.1.0)\n",
      "Requirement already satisfied: alembic!=1.10.0,<2 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from mlflow) (1.16.1)\n",
      "Requirement already satisfied: docker<8,>=4.0.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from mlflow) (7.1.0)\n",
      "Requirement already satisfied: graphene<4 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from mlflow) (3.4.3)\n",
      "Requirement already satisfied: pyarrow<21,>=4.0.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from mlflow) (19.0.1)\n",
      "Requirement already satisfied: sqlalchemy<3,>=1.4.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from mlflow) (2.0.41)\n",
      "Requirement already satisfied: waitress<4 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from mlflow) (3.0.2)\n",
      "Requirement already satisfied: cachetools<7,>=5.0.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from mlflow-skinny==3.1.0->mlflow) (5.5.2)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from mlflow-skinny==3.1.0->mlflow) (8.1.8)\n",
      "Requirement already satisfied: cloudpickle<4 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from mlflow-skinny==3.1.0->mlflow) (3.1.1)\n",
      "Requirement already satisfied: databricks-sdk<1,>=0.20.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from mlflow-skinny==3.1.0->mlflow) (0.56.0)\n",
      "Requirement already satisfied: fastapi<1 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from mlflow-skinny==3.1.0->mlflow) (0.115.12)\n",
      "Requirement already satisfied: gitpython<4,>=3.1.9 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from mlflow-skinny==3.1.0->mlflow) (3.1.44)\n",
      "Requirement already satisfied: importlib_metadata!=4.7.0,<9,>=3.7.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from mlflow-skinny==3.1.0->mlflow) (8.7.0)\n",
      "Requirement already satisfied: opentelemetry-api<3,>=1.9.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from mlflow-skinny==3.1.0->mlflow) (1.34.1)\n",
      "Requirement already satisfied: opentelemetry-sdk<3,>=1.9.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from mlflow-skinny==3.1.0->mlflow) (1.34.1)\n",
      "Requirement already satisfied: protobuf<7,>=3.12.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from mlflow-skinny==3.1.0->mlflow) (5.29.3)\n",
      "Requirement already satisfied: pydantic<3,>=1.10.8 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from mlflow-skinny==3.1.0->mlflow) (2.11.5)\n",
      "Requirement already satisfied: pyyaml<7,>=5.1 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from mlflow-skinny==3.1.0->mlflow) (6.0.2)\n",
      "Requirement already satisfied: requests<3,>=2.17.3 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from mlflow-skinny==3.1.0->mlflow) (2.32.3)\n",
      "Requirement already satisfied: sqlparse<1,>=0.4.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from mlflow-skinny==3.1.0->mlflow) (0.5.3)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.0.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from mlflow-skinny==3.1.0->mlflow) (4.12.2)\n",
      "Requirement already satisfied: uvicorn<1 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from mlflow-skinny==3.1.0->mlflow) (0.34.3)\n",
      "Requirement already satisfied: Mako in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from alembic!=1.10.0,<2->mlflow) (1.3.10)\n",
      "Requirement already satisfied: colorama in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from click<9,>=7.0->mlflow-skinny==3.1.0->mlflow) (0.4.6)\n",
      "Requirement already satisfied: google-auth~=2.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from databricks-sdk<1,>=0.20.0->mlflow-skinny==3.1.0->mlflow) (2.40.3)\n",
      "Requirement already satisfied: pywin32>=304 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from docker<8,>=4.0.0->mlflow) (308)\n",
      "Requirement already satisfied: urllib3>=1.26.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from docker<8,>=4.0.0->mlflow) (2.3.0)\n",
      "Requirement already satisfied: starlette<0.47.0,>=0.40.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from fastapi<1->mlflow-skinny==3.1.0->mlflow) (0.46.2)\n",
      "Requirement already satisfied: Werkzeug>=3.1 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from Flask<4->mlflow) (3.1.3)\n",
      "Requirement already satisfied: Jinja2>=3.1.2 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from Flask<4->mlflow) (3.1.6)\n",
      "Requirement already satisfied: itsdangerous>=2.2 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from Flask<4->mlflow) (2.2.0)\n",
      "Requirement already satisfied: blinker>=1.9 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from Flask<4->mlflow) (1.9.0)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from gitpython<4,>=3.1.9->mlflow-skinny==3.1.0->mlflow) (4.0.12)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython<4,>=3.1.9->mlflow-skinny==3.1.0->mlflow) (5.0.2)\n",
      "Requirement already satisfied: pyasn1-modules>=0.2.1 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from google-auth~=2.0->databricks-sdk<1,>=0.20.0->mlflow-skinny==3.1.0->mlflow) (0.4.2)\n",
      "Requirement already satisfied: rsa<5,>=3.1.4 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from google-auth~=2.0->databricks-sdk<1,>=0.20.0->mlflow-skinny==3.1.0->mlflow) (4.9.1)\n",
      "Requirement already satisfied: graphql-core<3.3,>=3.1 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from graphene<4->mlflow) (3.2.6)\n",
      "Requirement already satisfied: graphql-relay<3.3,>=3.1 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from graphene<4->mlflow) (3.2.0)\n",
      "Requirement already satisfied: zipp>=3.20 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from importlib_metadata!=4.7.0,<9,>=3.7.0->mlflow-skinny==3.1.0->mlflow) (3.23.0)\n",
      "Requirement already satisfied: opentelemetry-semantic-conventions==0.55b1 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from opentelemetry-sdk<3,>=1.9.0->mlflow-skinny==3.1.0->mlflow) (0.55b1)\n",
      "Requirement already satisfied: annotated-types>=0.6.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from pydantic<3,>=1.10.8->mlflow-skinny==3.1.0->mlflow) (0.7.0)\n",
      "Requirement already satisfied: pydantic-core==2.33.2 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from pydantic<3,>=1.10.8->mlflow-skinny==3.1.0->mlflow) (2.33.2)\n",
      "Requirement already satisfied: typing-inspection>=0.4.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from pydantic<3,>=1.10.8->mlflow-skinny==3.1.0->mlflow) (0.4.1)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from requests<3,>=2.17.3->mlflow-skinny==3.1.0->mlflow) (3.4.1)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from requests<3,>=2.17.3->mlflow-skinny==3.1.0->mlflow) (3.10)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from requests<3,>=2.17.3->mlflow-skinny==3.1.0->mlflow) (2025.1.31)\n",
      "Requirement already satisfied: pyasn1>=0.1.3 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from rsa<5,>=3.1.4->google-auth~=2.0->databricks-sdk<1,>=0.20.0->mlflow-skinny==3.1.0->mlflow) (0.6.1)\n",
      "Requirement already satisfied: greenlet>=1 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from sqlalchemy<3,>=1.4.0->mlflow) (3.2.3)\n",
      "Requirement already satisfied: anyio<5,>=3.6.2 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from starlette<0.47.0,>=0.40.0->fastapi<1->mlflow-skinny==3.1.0->mlflow) (4.8.0)\n",
      "Requirement already satisfied: sniffio>=1.1 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from anyio<5,>=3.6.2->starlette<0.47.0,>=0.40.0->fastapi<1->mlflow-skinny==3.1.0->mlflow) (1.3.1)\n",
      "Requirement already satisfied: h11>=0.8 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from uvicorn<1->mlflow-skinny==3.1.0->mlflow) (0.14.0)\n",
      "Requirement already satisfied: appdirs>=1.4.4 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from dagshub) (1.4.4)\n",
      "Requirement already satisfied: httpx>=0.23.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from dagshub) (0.28.1)\n",
      "Requirement already satisfied: rich>=13.1.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from dagshub) (14.0.0)\n",
      "Requirement already satisfied: dacite~=1.6.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from dagshub) (1.6.0)\n",
      "Requirement already satisfied: tenacity>=8.2.2 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from dagshub) (9.0.0)\n",
      "Requirement already satisfied: gql[requests] in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from dagshub) (3.5.3)\n",
      "Requirement already satisfied: dataclasses-json in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from dagshub) (0.6.7)\n",
      "Requirement already satisfied: treelib>=1.6.4 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from dagshub) (1.7.1)\n",
      "Requirement already satisfied: pathvalidate>=3.0.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from dagshub) (3.2.3)\n",
      "Requirement already satisfied: boto3 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from dagshub) (1.38.35)\n",
      "Requirement already satisfied: semver in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from dagshub) (3.0.4)\n",
      "Requirement already satisfied: dagshub-annotation-converter>=0.1.5 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from dagshub) (0.1.9)\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from streamlit) (5.5.0)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: watchdog<7,>=2.1.5 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from streamlit) (6.0.0)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from streamlit) (0.9.1)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from streamlit) (6.4.2)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
      "Requirement already satisfied: narwhals>=1.14.2 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from altair<6,>=4.0->streamlit) (1.29.1)\n",
      "Requirement already satisfied: lxml in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from dagshub-annotation-converter>=0.1.5->dagshub) (5.3.1)\n",
      "Requirement already satisfied: httpcore==1.* in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from httpx>=0.23.0->dagshub) (1.0.7)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from Jinja2>=3.1.2->Flask<4->mlflow) (3.0.2)\n",
      "Requirement already satisfied: attrs>=22.2.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (25.1.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2024.10.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.36.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.23.1)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from rich>=13.1.0->dagshub) (3.0.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from rich>=13.1.0->dagshub) (2.19.1)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from markdown-it-py>=2.2.0->rich>=13.1.0->dagshub) (0.1.2)\n",
      "Requirement already satisfied: botocore<1.39.0,>=1.38.35 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from boto3->dagshub) (1.38.35)\n",
      "Requirement already satisfied: jmespath<2.0.0,>=0.7.1 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from boto3->dagshub) (1.0.1)\n",
      "Requirement already satisfied: s3transfer<0.14.0,>=0.13.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from boto3->dagshub) (0.13.0)\n",
      "Requirement already satisfied: marshmallow<4.0.0,>=3.18.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from dataclasses-json->dagshub) (3.26.1)\n",
      "Requirement already satisfied: typing-inspect<1,>=0.4.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from dataclasses-json->dagshub) (0.9.0)\n",
      "Requirement already satisfied: mypy-extensions>=0.3.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from typing-inspect<1,>=0.4.0->dataclasses-json->dagshub) (1.1.0)\n",
      "Requirement already satisfied: yarl<2.0,>=1.6 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from gql[requests]->dagshub) (1.20.1)\n",
      "Requirement already satisfied: backoff<3.0,>=1.11.1 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from gql[requests]->dagshub) (2.2.1)\n",
      "Requirement already satisfied: requests-toolbelt<2,>=1.0.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from gql[requests]->dagshub) (1.0.0)\n",
      "Requirement already satisfied: multidict>=4.0 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from yarl<2.0,>=1.6->gql[requests]->dagshub) (6.4.4)\n",
      "Requirement already satisfied: propcache>=0.2.1 in c:\\users\\thinkpad\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from yarl<2.0,>=1.6->gql[requests]->dagshub) (0.3.2)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "%pip install pandas numpy matplotlib seaborn scikit-learn joblib mlflow dagshub streamlit python-dotenv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-25T04:46:24.640676Z",
     "start_time": "2025-05-25T04:46:24.160442Z"
    }
   },
   "outputs": [],
   "source": [
    "!pip freeze > requirements.txt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-25T04:46:24.645167Z",
     "start_time": "2025-05-25T04:46:24.642092Z"
    }
   },
   "outputs": [],
   "source": [
    "import os # for file and directory manipulation\n",
    "import pandas as pd  # for data manipulation and analysis\n",
    "import numpy as np  # for numerical operations\n",
    "import matplotlib.pyplot as plt  # for creating basic plots and charts\n",
    "import seaborn as sns  # for statistical data visualization\n",
    "from sklearn.model_selection import train_test_split  # for splitting the dataset into training and testing sets\n",
    "from sklearn.preprocessing import StandardScaler, LabelEncoder  # for feature scaling and encoding categorical variables"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "f3YIEnAFKrKL"
   },
   "source": [
    "# **3. Load Dataset**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-25T04:46:24.699602Z",
     "start_time": "2025-05-25T04:46:24.647038Z"
    },
    "id": "GHCGNTyrM5fS"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Time_spent_Alone</th>\n",
       "      <th>Stage_fear</th>\n",
       "      <th>Social_event_attendance</th>\n",
       "      <th>Going_outside</th>\n",
       "      <th>Drained_after_socializing</th>\n",
       "      <th>Friends_circle_size</th>\n",
       "      <th>Post_frequency</th>\n",
       "      <th>Personality</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>4.0</td>\n",
       "      <td>No</td>\n",
       "      <td>4.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>No</td>\n",
       "      <td>13.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>Extrovert</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>9.0</td>\n",
       "      <td>Yes</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>Yes</td>\n",
       "      <td>0.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>Introvert</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>9.0</td>\n",
       "      <td>Yes</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>Yes</td>\n",
       "      <td>5.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>Introvert</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.0</td>\n",
       "      <td>No</td>\n",
       "      <td>6.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>No</td>\n",
       "      <td>14.0</td>\n",
       "      <td>8.0</td>\n",
       "      <td>Extrovert</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3.0</td>\n",
       "      <td>No</td>\n",
       "      <td>9.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>No</td>\n",
       "      <td>8.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>Extrovert</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Time_spent_Alone Stage_fear  Social_event_attendance  Going_outside  \\\n",
       "0               4.0         No                      4.0            6.0   \n",
       "1               9.0        Yes                      0.0            0.0   \n",
       "2               9.0        Yes                      1.0            2.0   \n",
       "3               0.0         No                      6.0            7.0   \n",
       "4               3.0         No                      9.0            4.0   \n",
       "\n",
       "  Drained_after_socializing  Friends_circle_size  Post_frequency Personality  \n",
       "0                        No                 13.0             5.0   Extrovert  \n",
       "1                       Yes                  0.0             3.0   Introvert  \n",
       "2                       Yes                  5.0             2.0   Introvert  \n",
       "3                        No                 14.0             8.0   Extrovert  \n",
       "4                        No                  8.0             5.0   Extrovert  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Get the absolute path of the root directory of the project\n",
    "BASE_DIR = os.path.abspath(os.path.join(os.getcwd(), \"..\"))\n",
    "\n",
    "# Combine \n",
    "csv_path = os.path.join(BASE_DIR, \"personality_dataset_raw.csv\")\n",
    "\n",
    "# Load the dataset from the root directory\n",
    "df = pd.read_csv(csv_path)\n",
    "\n",
    "# Show the first 5 rows to understand the structure\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "bgZkbJLpK9UR"
   },
   "source": [
    "# **4. Exploratory Data Analysis (EDA)**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Basic Data Overview"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-25T04:46:24.743909Z",
     "start_time": "2025-05-25T04:46:24.700576Z"
    },
    "id": "dKeejtvxM6X1"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 2900 entries, 0 to 2899\n",
      "Data columns (total 8 columns):\n",
      " #   Column                     Non-Null Count  Dtype  \n",
      "---  ------                     --------------  -----  \n",
      " 0   Time_spent_Alone           2837 non-null   float64\n",
      " 1   Stage_fear                 2827 non-null   object \n",
      " 2   Social_event_attendance    2838 non-null   float64\n",
      " 3   Going_outside              2834 non-null   float64\n",
      " 4   Drained_after_socializing  2848 non-null   object \n",
      " 5   Friends_circle_size        2823 non-null   float64\n",
      " 6   Post_frequency             2835 non-null   float64\n",
      " 7   Personality                2900 non-null   object \n",
      "dtypes: float64(5), object(3)\n",
      "memory usage: 181.4+ KB\n"
     ]
    }
   ],
   "source": [
    "# Summary of dataset: data types and missing values\n",
    "df.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " **Insights from Basic Data Overview**\n",
    "\n",
    "1. **Dataset Size and Completeness**\n",
    "\n",
    "   * The dataset contains **2,900 rows and 8 columns**, **have duplicated values**, and **have missing values**.\n",
    "   * This makes the dataset must to cleaning before ready for analysis.\n",
    "\n",
    "2. **Feature Types**\n",
    "\n",
    "   * There are **5 numeric (float64)** \n",
    "   *  **3 categorical/object features** such as `Personality` \n",
    "\n",
    "3. **Target Distribution (`Personality`)**\n",
    "\n",
    "   * The `Personality` variable is object (`Introvert` or `Extrovert`).   \n",
    "\n",
    "4. **Feature Observations**\n",
    "    * **Time_spent_Alone**: Hours spent alone daily (0–11)\n",
    "    * **Stage_fear**: Presence of stage fright (Yes/No)\n",
    "    * **Social_event_attendance**: Frequency of social events (0–10)\n",
    "    * **Going_outside**: Frequency of going outside (0–7)\n",
    "    * **Drained_after_socializing**: Feeling drained after socializing (Yes/No)\n",
    "    * **Friends_circle_size**: Number of close friends (0–15)\n",
    "    * **Post_frequency**: Social media post frequency (0–10)\n",
    "    * **Personality**: Target variable (Extrovert/Introvert)\n",
    "\n",
    "5. **duplicated data** found in the data but no need to handle."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Time_spent_Alone</th>\n",
       "      <th>Stage_fear</th>\n",
       "      <th>Social_event_attendance</th>\n",
       "      <th>Going_outside</th>\n",
       "      <th>Drained_after_socializing</th>\n",
       "      <th>Friends_circle_size</th>\n",
       "      <th>Post_frequency</th>\n",
       "      <th>Personality</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>2837.000000</td>\n",
       "      <td>2827</td>\n",
       "      <td>2838.000000</td>\n",
       "      <td>2834.000000</td>\n",
       "      <td>2848</td>\n",
       "      <td>2823.000000</td>\n",
       "      <td>2835.000000</td>\n",
       "      <td>2900</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>unique</th>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>top</th>\n",
       "      <td>NaN</td>\n",
       "      <td>No</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>No</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Extrovert</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>freq</th>\n",
       "      <td>NaN</td>\n",
       "      <td>1417</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1441</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1491</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>4.505816</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.963354</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>6.268863</td>\n",
       "      <td>3.564727</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>3.479192</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.903827</td>\n",
       "      <td>2.247327</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.289693</td>\n",
       "      <td>2.926582</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>2.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>4.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>8.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>10.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>11.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>10.000000</td>\n",
       "      <td>7.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>15.000000</td>\n",
       "      <td>10.000000</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Time_spent_Alone Stage_fear  Social_event_attendance  Going_outside  \\\n",
       "count        2837.000000       2827              2838.000000    2834.000000   \n",
       "unique               NaN          2                      NaN            NaN   \n",
       "top                  NaN         No                      NaN            NaN   \n",
       "freq                 NaN       1417                      NaN            NaN   \n",
       "mean            4.505816        NaN                 3.963354       3.000000   \n",
       "std             3.479192        NaN                 2.903827       2.247327   \n",
       "min             0.000000        NaN                 0.000000       0.000000   \n",
       "25%             2.000000        NaN                 2.000000       1.000000   \n",
       "50%             4.000000        NaN                 3.000000       3.000000   \n",
       "75%             8.000000        NaN                 6.000000       5.000000   \n",
       "max            11.000000        NaN                10.000000       7.000000   \n",
       "\n",
       "       Drained_after_socializing  Friends_circle_size  Post_frequency  \\\n",
       "count                       2848          2823.000000     2835.000000   \n",
       "unique                         2                  NaN             NaN   \n",
       "top                           No                  NaN             NaN   \n",
       "freq                        1441                  NaN             NaN   \n",
       "mean                         NaN             6.268863        3.564727   \n",
       "std                          NaN             4.289693        2.926582   \n",
       "min                          NaN             0.000000        0.000000   \n",
       "25%                          NaN             3.000000        1.000000   \n",
       "50%                          NaN             5.000000        3.000000   \n",
       "75%                          NaN            10.000000        6.000000   \n",
       "max                          NaN            15.000000       10.000000   \n",
       "\n",
       "       Personality  \n",
       "count         2900  \n",
       "unique           2  \n",
       "top      Extrovert  \n",
       "freq          1491  \n",
       "mean           NaN  \n",
       "std            NaN  \n",
       "min            NaN  \n",
       "25%            NaN  \n",
       "50%            NaN  \n",
       "75%            NaN  \n",
       "max            NaN  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Statistical summary of all columns\n",
    "df.describe(include=\"all\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of duplicated rows: 388\n"
     ]
    }
   ],
   "source": [
    "# Count and show duplicated rows\n",
    "print(\"Number of duplicated rows:\", df.duplicated().sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Time_spent_Alone             63\n",
       "Stage_fear                   73\n",
       "Social_event_attendance      62\n",
       "Going_outside                66\n",
       "Drained_after_socializing    52\n",
       "Friends_circle_size          77\n",
       "Post_frequency               65\n",
       "Personality                   0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Check column that have missing values\n",
    "df.isna().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Displaying unique features value of object column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-25T04:46:24.758970Z",
     "start_time": "2025-05-25T04:46:24.745105Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Unique values in 'Stage_fear': ['No' 'Yes' nan]\n",
      "Number of unique values in 'Stage_fear': 3\n",
      "\n",
      "Unique values in 'Drained_after_socializing': ['No' 'Yes' nan]\n",
      "Number of unique values in 'Drained_after_socializing': 3\n",
      "\n",
      "Unique values in 'Personality': ['Extrovert' 'Introvert']\n",
      "Number of unique values in 'Personality': 2\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# List of categorical features and uniques values to check\n",
    "categorical_features = df.select_dtypes(include='object').columns.tolist()\n",
    "\n",
    "# Display unique values for each categorical feature\n",
    "for col in categorical_features:\n",
    "    unique_values = df[col].unique()\n",
    "    print(f\"Unique values in '{col}': {unique_values}\")\n",
    "    print(f\"Number of unique values in '{col}': {len(unique_values)}\\n\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Distribution of Target Variable (Personality)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-25T04:46:24.870361Z",
     "start_time": "2025-05-25T04:46:24.760051Z"
    }
   },
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Percentage by class:\n",
      "Personality\n",
      "Extrovert    51.413793\n",
      "Introvert    48.586207\n",
      "Name: proportion, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Visualize the distribution of the target variable\n",
    "sns.countplot(x='Personality', data=df)\n",
    "plt.title('Distribution of Personality')\n",
    "plt.xlabel('Personality')\n",
    "plt.ylabel('Count')\n",
    "plt.show()\n",
    "\n",
    "# Percentage distribution\n",
    "print(\"Percentage by class:\")\n",
    "print(df['Personality'].value_counts(normalize=True) * 100)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "From distribution of Personality, students are classified as *Personality*. The distribution bar chart shows the data is balance."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Correlation Matrix with Target"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-25T04:46:25.353451Z",
     "start_time": "2025-05-25T04:46:24.871873Z"
    }
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABXcAAASlCAYAAADj1+r/AAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjEsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvc2/+5QAAAAlwSFlzAAAPYQAAD2EBqD+naQABAABJREFUeJzs3Qd8E/Ubx/En3aW7pYO9N8hSWS6GDFGGCydLUHGhqAgOUFARRf64FQei4h44UIYIKrKXbJC9SwuU0r3yfz2/2pEOWsCSHvm8X69oc7lc7nIhyX3z3POz2e12uwAAAAAAAAAALMXN2SsAAAAAAAAAADh9hLsAAAAAAAAAYEGEuwAAAAAAAABgQYS7AAAAAAAAAGBBhLsAAAAAAAAAYEGEuwAAAAAAAABgQYS7AAAAAAAAAGBBhLsAAAAAAAAAYEGEuwAAAAAAAABgQYS7AAAA5dSHH34oNptNdu/e/Z8tU5ely9RlI9sVV1xhLudaRkaGjBw5UqpVqyZubm7Sp0+fMnvdOGsbAQAAULYIdwEAgEvZsWOH3HXXXVK7dm3x8fGRwMBA6dChg7zyyiuSnJws54tPP/1UpkyZIuXJwIEDTeioz3lRz/U///xjbtfLpEmTTnv5Bw8elKefflrWrl0rVvDBBx/ISy+9JNdff71Mnz5dHnrooVLd7+KLLzbP0VtvvfWfr1PNmjVz90HBS0pKipSF559/XmbOnFkmywYAADjfeTh7BQAAAM6VWbNmyQ033CDe3t7Sv39/adq0qaSlpcmiRYvk0UcflY0bN8rUqVPlfAl3N2zYIA8++KDD9Bo1aphg1dPT0ynr5eHhIUlJSfLjjz/KjTfe6HDbjBkzTOB+piGihrvPPPOMCShbtGhR6vvNnTtXnOG3336TKlWqyP/+979S30cD8BUrVpht1Odr2LBh//l66XP38MMPF5ru5eUlZRXuasD9X1UuAwAAuBLCXQAA4BJ27dolN910kwk3NVSrVKlS7m333nuvbN++3YS/Z8tut5tw0tfXt9BtOl0DMj0F31m0AlMDVGfRYF0rpT/77LNC4a4G0j179pRvvvnmnKyLhswVKlQos9CyJEeOHJHg4ODTus8nn3wiERER8vLLL5tAVFsvaND7X9LA+bbbbhMry8rKMj/cOPO1DgAAcC7QlgEAALiEF198URISEuT99993CHZz1K1bV4YPH+7QD3X8+PFSp04dE0hqgPb4449Lamqqw/10+tVXXy1z5syRCy+80IS677zzjixcuNAEqZ9//rk8+eSTJjDTIDE+Pt7cb9myZdK9e3cJCgoy0y+//HL566+/StyO77//3gSglStXNuul66frmZmZmTuP9lbVoHrPnj25p9TnBIDF9dzVwPvSSy8VPz8/Ezj27t1bNm/e7DCPtjzQ+2oQri0WdD5d/0GDBpmgtLRuueUW+eWXXyQuLi53mlajalWq3lbQsWPH5JFHHpFmzZqJv7+/aevQo0cP+fvvv3Pn0ef7oosuMn/r+uRsd8526nOildqrVq2Syy67zDznuj+L6kc7YMAAEwoW3P5u3bpJSEiIqRA+lcTERFP5qr10dR81aNDAtJnQ4D//PliwYIGpFs9ZV92GkmgArqGuvub0udfr55ruN60Iz9k+/bczceJEE6jmp9vcvn17CQsLM/8uWrduLV9//bXDPLrd+nxpW4qc50FfW0r/X1RwnfM6LLic++67z1QzN2nSxKzX7NmzzW0HDhyQwYMHS2RkpJmut2tLjIJee+01c5u+NnQ/679nZzy/AAAAp4PKXQAA4BK0DYD22dWwqTSGDBliAicN0jSo0zB2woQJJvD77rvvHObdunWr3HzzzaaX79ChQ02Yl0ODV60M1XBSg2H9W4NUDSc17Bo7dqyp5J02bZp06tRJ/vzzT9NTtTgaVmrAOWLECPN/XdaYMWNMaKz9W9UTTzwhJ06ckP379+ee8q/zFufXX38166PPjwZn2rZBgy6tsF29enWhgE0rbmvVqmWeD739vffeM9WkGvCVxrXXXit33323fPvttyZ0UxqiNWzYUFq1alVo/p07d5qerNpSQx83OjraBOgaiG/atMkE3Y0aNZJx48aZ5+LOO+80QbXKv7+PHj1qtlMruLUyVcO+omj/ZX1eNeRdsmSJuLu7m8fT9g0ff/yxebziaIDbq1cvE9zecccdpsWBBv/a9kNDRt0f4eHhZjnPPfec+cFBn0el23Aq+hrUYF1fK/o60udRw8yckPq/kp6eLrGxsQ7TNPDUi4b4+rzrtujrvXr16rJ48WIZPXq0HDp0yKHPsz6P+lzceuutpopWf+jQffjTTz+ZHyiUPg/6b01f87rflP5gcSZ0n3355Zcm5K1YsaJ53eprpW3btrnhrz73+sOC7hv9N5PTtuTdd9+VBx54wPx71x95tMp+3bp15jkv6gcHAACAcsMOAABwnjtx4oSWTNp79+5dqvnXrl1r5h8yZIjD9EceecRM/+2333Kn1ahRw0ybPXu2w7wLFiww02vXrm1PSkrKnZ6VlWWvV6+evVu3bubvHDpPrVq17FdeeWXutGnTppll7Nq1y2G+gu666y57hQoV7CkpKbnTevbsadatIF2WLlOXnaNFixb2iIgI+9GjR3On/f3333Y3Nzd7//79c6eNHTvW3Hfw4MEOy+zbt689LCzMXpIBAwbY/fz8zN/XX3+9vXPnzubvzMxMe1RUlP2ZZ57JXb+XXnop9366XTpPwe3w9va2jxs3LnfaihUrCm1bjssvv9zc9vbbbxd5m17ymzNnjpn/2Wefte/cudPu7+9v79OnT4nbOHPmzNz75afba7PZ7Nu3b3d43CZNmthL67777rNXq1Yt93Uzd+5c81hr1qxxmK+o101R21iUnNdzwYvuezV+/HizD7dt2+Zwv1GjRtnd3d3te/fuLfa1mpaWZm/atKm9U6dODtN1efraKEinFfUaznkd5qfX9fW6ceNGh+l33HGHvVKlSvbY2FiH6TfddJM9KCgodx31veF09gUAAEB5QVsGAABw3stphRAQEFCq+X/++Wfzf62OzS9nkKmCvXm1mlRP2S+KVn/m77+7du3a3PYDWkmqFZJ60VPTO3fuLH/88Ueh09vzy7+skydPmvtqlapWVG7ZskVOl1Zb6jrpKfChoaG50y+44AK58sorc5+L/LTqNj99fN2WnOe5NHT7tQ3B4cOHTcWl/r+4Ckk9lT6nT7G2n9DH0kpkrZDWyuHS0uVoy4bS6Nq1q6lM1WpgrZDVNg1avVsSfb600lerQAu+djSD1KrRM6FtQr744gvp169fbksCrfTWimmt3v0vtWnTRubNm+dw0QEI1VdffWX2t7YtyHnt6qVLly5m3+jrt6jX6vHjx001ud73dPbZ6dCK4saNG+de1+db+zdfc8015u/866v/XnV9ctZFW4xopbu2BwEAALAS2jIAAIDznvZozQlDS0N71WqYqL1E84uKijIhkN5eMNwtTsHbNNjNCX2Lo6GThmdF0R6t2sNXA9GCYare73TlbEv+VhI5tE2AthTQ4Fl78ebQU/Hzy1lXDfBynuuSXHXVVSZs18BSw2Xtl6vPt/ajLUjDbj3F/8033zQD4+XvL6z9XEtL+x6fzuBp2jNWexzr+mnbCA1SS/N8atuGgj8k5LRcKPjaKS1tCRETE2PaF2hrhhwdO3Y0g9NpS4z/aqA+bWmgYW1R9PWr7Qq0vUFxg8Tl0PYLzz77rHn+8veqLtgv979S8N+aPl/aH3jq1Knmcqr1feyxx0x7En1+9XWo4b7+2KCtSQAAAMozwl0AAHDe08BRA7cNGzac1v1KG0Llr1As6bacqlztj6v9WItSXH9cDaq0OlG3RytKtTepVpRq9aGGU6eq+P0vaWVqUXIGDCttFa1WxGpfY+2pq71+i/P888/LU089Zfrzag9jrTDWIFP7pZ7ONp9qPxVlzZo1ueHf+vXrTV9lZ8mpztV+x0X5/fffTdBb1vT51orukSNHFnl7/fr1zf+1d7T229XB6zSU10EMPT09Tb/g0g5SVty/v/zhfmn+rWl/5eJ+TNEK9ZzwXXtnayCtA7Fpxa+ut/ZwfuaZZ0q1vgAAAM5AuAsAAFzC1Vdfbar3dICsdu3anXLeGjVqmGBIqxTzD3KlgzNpwKq3n6mcwaI0oC2uOrI42sZAWxLoQGQamuXQatYzDaZztkWDrYK0zYNWceav2v0vaWXkBx98YIJaHeSsOF9//bUJLt9//32H6bovdP3KoiJUq5W1hYOe5q+Dsr344ovSt29fU2Fc0vOpFaBaJZ6/ejenZcaZvHZ0XbSCWFsy6IBfBWkLCA1/z0W4q69fHQSupNeuhqP6w4NWfmuQn0PD3YKK229aEa77uKDSVj9rdbHuAw2DS/NvTV/n+hzrRQeA0x8fdNA7HSxOtwUAAKA8oucuAABwCVppqOHNkCFDTEhb0I4dO8yp/zktA9SUKVMc5pk8ebL5f8+ePc94PVq3bm0CMj3lX0OygvRU8pIqZvNXyGoIpRWGBem2lqZNg1ZUagWxVtDmD9K0yllbAeQ8F2VBw0itxH399ddNy4tTbXfBqmDt/XrgwAGHaTkhdFGB4OnSSui9e/ea50X3e82aNU31Z/72AkXR50vDRN2m/P73v/+ZELNHjx6nvS7fffedCXjvvfdeE+4WvOgPFxqmlrRu/wWtHNYfSDS0LUifd+0NnLPPdHvzV9lqy42ZM2cWup/ut6L2mf470dewtoHI3yNan4/S0HW47rrrzHNTVNV+/n9r+qNJftq+Q4N9fd2lp6eX6vEAAACcgcpdAADgEjQo0tPBtSpPq3F1gKimTZuacHTx4sUmLNRBxVTz5s1NkKeVvjmtEJYvX26Cvj59+pxVhaRWqb733nsm5GvSpImpDtVesBpULliwwFT0/vjjj0XeVytItZpR102rNTU8+/jjj4tsh6Ahsvaz1UHhtNpUWz3owFJF0RYRuj5a0XzHHXdIcnKyvPbaaxIUFHTKdglnS58L7R9cEg0vtQ2FPlf6HGiLBK1UrV27dqF9rD2R3377bVOxqaGhDg52qp7IRdF+xhqYjx07Vlq1apVbcXrFFVeY9hBaxVscfY719fHEE0+YMFNfSxqSa+WttpHIqdw+Hbqt2ltYt70o2v7g3XffNQP9abVpWXr00Uflhx9+MPtE/73o60yDZ90nWmGt26zV1PoDiIbi3bt3NxXa2t7ijTfeMP1s84e1Speh1c46v7ZP0f2l+02ruTVk14ppfb3roIFvvfWWaf1Q2kHZXnjhBfPvSpc3dOhQE9geO3bM3F8fU/9W2mNXf2DQHruRkZGyefNmE9DrdpR2IEYAAACnsAMAALiQbdu22YcOHWqvWbOm3cvLyx4QEGDv0KGD/bXXXrOnpKTkzpeenm5/5pln7LVq1bJ7enraq1WrZh89erTDPKpGjRr2nj17FnqcBQsWaOJq/+qrr4pcjzVr1tivvfZae1hYmN3b29ss58Ybb7TPnz8/d55p06aZZezatSt32l9//WVv27at3dfX1165cmX7yJEj7XPmzDHz6WPmSEhIsN9yyy324OBgc5suX+my9LouO79ff/3VPA+63MDAQPs111xj37Rpk8M8Y8eONfeNiYlxmF7UehZlwIABdj8/v1POk7N+L730Uu40fc4ffvhhe6VKlcz66XouWbLEfvnll5tLft9//729cePGdg8PD4ft1PmaNGlS5GPmX058fLx5rlq1amVeA/k99NBDdjc3N/PYp3Ly5Ekzr+4ffe3Uq1fPbE9WVlahxy1unXJER0ebbbn99tuLnScpKcleoUIFe9++fYvdH0U9V0Up7vVccPv030LdunXNv6GKFSva27dvb580aZI9LS0td77333/fbLu+vhs2bGjWK+c1lN+WLVvsl112mdm3epu+TnLMnTvX3rRpU/M4DRo0sH/yySdFLkOv33vvvcU+h3qb/hvW/REVFWXv3LmzferUqbnzvPPO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s2btcfmvvvpK7dq1s8t36tRJP/30k9v9LpdLDz/8sOrXr6+QkBCddtppWrVq1UHdBsJdAAAAAAAAAF7liy++0J133qkRI0Zo7ty5OvLII9W3b19t27atyuWnT5+uQYMG6eqrr9a8efN03nnn2cvixYvLlnn22Wf1yiuv6K233tLMmTMVFhZm15mbm3vQtoNwFwAAAAAAAPBSxfI5LC776oUXXtC1116rq666Sh06dLCBbGhoqN5///0ql3/55ZfVr18/3X333Wrfvr1GjhypY445Rq+99lpZ1e5LL72kBx98UOeee646d+6sjz76SFu2bNG3336rg4VwFwAAAAAAAICj5eXlKSMjw+1ibqtKfn6+5syZY9smlPL19bXX//777yofY26vuLxhqnJLl1+3bp2SkpLclomKirLtHqpb53+BcBcAAAAAAACAoz311FM2TK14MbdVJSUlRUVFRapbt67b7ea6CWirYm7f0/Kl/+7LOv8L/gdtzQAAAAAAAABwCAwfPtz20K0oKChIhzvCXQAAAAAAAMBLufajX21tFBQUVOMwNz4+Xn5+fkpOTna73VyvV69elY8xt+9p+dJ/zW3169d3W+aoo47SwUJbBgAAAAAAAABeIzAwUMcee6wmT55cdltxcbG93q1btyofY26vuLwxadKksuWbN29uA96Ky5i+vzNnzqx2nf8FKncBAAAAAAAAeJU777xTQ4YM0XHHHacuXbropZdeUlZWlq666ip7/+DBg9WwYcOyvr233367Tj75ZD3//PPq37+/xowZo3/++UfvvPOOvd/Hx0d33HGHHn/8cbVu3dqGvQ899JAaNGig884776BtB+EuAAAAAAAA4KVcrsOjLcO+uvjii7V9+3Y9/PDDdsIz0zphwoQJZROibdy4Ub6+5U0Punfvrs8++0wPPvig7r//fhvgfvvttzriiCPKlrnnnntsQHzdddcpLS1NPXr0sOsMDg7WwUK4CwAAAAAAAMDr3HLLLfZSld9//3232wYOHGgv1THVu4899pi9HCq1qufulVdeeVDLlEs98sgj/2kjY5Pu9+nTR2FhYYqOjtbhwryIzYvSfNNQU6eccootQS/VrFkzW9Zem/Y/AAAAAAAAcDjYp8pdE76NHj265IH+/oqNjVXnzp01aNAge1/FUuX98fLLL8vlcslpXnzxRW3dulXz589XVFSUDUV79eql1NRUR4e9ptzcbJfZpv01e/ZsG3ofzvu/Noo+/WzFnn2h/KJjlbdhrbZ98IZy16yodvmYMwcouk9/+cfXUVFGhjJn/qmUz9+Xq6Bgv9cJz4rpd45izx0of7O/1q9R0nuvK3f1Hl4D/Qcopu/ZCjCvgcx0Zfz9p7Z/+l7ZayBuwCWK6NpDgQ0by5Wfp5wVS7Xt43eVv2XTIdwq7Kuhg5ro7NPqKTzMT4uWZ+qFt1dr09bcapc3b+NXXdxEp59cR7HRAUpJzdfPU7bpo68Sy5bp2TVO5/atpzYtwxUVEaCh/5un1euzDtEWYV9cfVkznX16PUWE+WvRsgyNemOVNm3N2eP+HzqomU7vVUdx0YFK2ZmvnyYnafQXG+39fn4+uu7yZup6XKwa1AtRVlah/lmQqjdHr9OOnfmHcMuwJ7E9jlOLYVcr6pgjFNygjv654CYlj5+858f07KIOo+5TeIfWyk3cqtVPvalNH33jtkzTGy9VizuvVlC9BGUsXK4ld4xU+uxFB3lrcCCuHNhQZ/ZOUHiYvxavyNTL763X5qS8apf/9NUjVS9h9xnGv5uYrFc+2GB/jokK0PWXN9axnSIVEuxn31M+/WaL/pyVelC3Bftn6CWNdVafugoP/fdzwDtrtXkvnwOuvLixTu+Z8O/ngAJN+M18Dth0QOvFoRfd92zFnTOw7Ngt+f29HAuY48G+Z5UcC5jjwRl/avtn5ccCIe072fUFtWitgNg4bXr2Ee2aPf0QbhGAPdnnNLZfv3428Fu/fr1+/vlnG2KahsJnnXWWCgsLq3xMQYWAaE9MiOjEMHTNmjV2hj3Ta6NOnTr/2XpN0Fndc3qoZg40s/yZ6t39lZCQoNDQ0MN6/9c2Ed1OVsLg65Qy9lNtuO9m+2be6P4n5BdZdUgfcWIvxQ8aqpSvP9W6O69V0tsvKLLbyYq/5Kr9Xic8K6L7yapz5fVK+fITrbv7RuVuWKsmDz0lv8iq/39F9uilOpdfo5QvP9ba26/W1jdeUOSJpyjhsqFly4R27KzUCeO1fvht2vjoffLx81eTh5+WT9DB6xuEA3PpgIa6oH8DPf/2al1/7wLl5hVp1MNHKDCg+r/plw5opHP71deL/7dGV9w6V299tP7f9dQvWyY4yFcLl2XY+1B7XXZBY114VkMb6F531zzl5Bbphcc67XH/X3ZBE513ZgO9+NZqXXbTbL354Vpddn5jXXh2w7J936ZlhA17h94xRw88tURNGobqmQfLe4zB8/zCQpWxcIUW3/ZojZYPadZIx49/Wzt+n6lpx52rda+OVqe3H1d8nx5ly9QfeIbaPzdcqx5/XdO6DFDmwuU64cf3FJgQexC3BAfiknPqa0C/unrp3fW65cElys0r1tPD2ypgD38Dbrp/iS68fl7Z5e7Hl9vbp87cWbbMfTe3UOP6wXrwuVW69p7FNtR96I5WatWsZp/3cegMGtBQ5/evr+ffWqMb7ltkXwOjHuqwl88BDe0XuC+9u06Db5uvtz/eoEHnNdQFZ9Y7oPXCA8cCQ65XylefaP29N9ljt8YPPLnHY4GEy67Wjq8+0bo7rtHWN1+w60i4tPxYwDco2B5TJL/32iHcEhxKLvkcFhdvtc/hblBQkA38zGxxxxxzjG0g/N1339mg98MPP7TLmDDwzTff1DnnnGOrNp944gkVFRXp6quvtjPFhYSEqG3btrZSc0+n5ZtT/G+77TbbjNhUCZvfa1oqVGRaBlxzzTU2RIyMjFTv3r21YMECt2Wefvpp2ww5IiLCjiE3N3efKk9Ny4X4+HgbPppZ8ebOnevWdmDs2LH66KOP7HabbTCBtxETE1N2m1FcXGxn2Ct9Do488kh9/fXXu7VBMM+lCYvNcz1t2rQ9js9sq/l9ZtvM9pvHmZn6SpmxdezY0a7LjNXM6FdRXl6e7r33XjVu3Ngu06pVK7333ntVtmXYsWOHrdI2+94Etp06ddLnn3++x/FVbMtgXh9mfZUvpft0f/b/8uXLbXNq05i6Q4cO+vXXX+06TUNrbxXT/3ylT56gjN9/Uf7mjUp+9xUV5+cpqlffKpcPadNBOSuWKPOv31S4PVnZC+cqY/rvCm7Vdr/XCc+KO/sCpf36s9J/m6j8TRuV9PbLKs7LU/Sp1bwG2nVUzvIlypj2mwq2JytrwRz7c0irdmXLJD5+v9J/+0X5iRvsB8Qtrz2ngIS6Cm7Z+hBuGfbFwLMa6uOvEjVt1k6t3ZCtJ15eqbjYQPU4Ia7axxzRLlJ/zdqhGXNSlbQ9T1P/3qHZ89PUvnVE2TK/TN2u0V8mas6CmrfswaE38JyG+ujLDZo2c4fWrM/S4y8uV1xskE7qGl/tY45oH6lpM1L09z87lbQtT79PT9Gs+all+z8ru0j/e3ihpkzbrsTNOVqyoqQavF3rCNWtotoPnrF94h9aOeIlJX/3a42Wb3rdJcpZt0nL7nlGu5av1YY3PlXS2IlqfnvJ51ej+R1XKfG9L7Vp9DjtWrZGi24aoaLsXDW+8oKDuCU4EOefUVeffLNF0+ekae3GHD3z+lrFxwSqx3Ex1T4mPbNQqekFZZeux0Rrc1KuFizNLFumY5twfTMxWSvWZGnrtjxbtZuVVaQ2zWt2ph4OnYFn1dfHX2/SX7NT7eeAJ19ZVfI5oEv1X8p0bBuhv2bt3O1zgPk7fyDrxaEVe9YFSp/8s9LNsZs5Fnjn5ZJjt97VHAu0LTkeLD0WyF44xx4bVjwezJo/WyljPtSuWX8dwi0BcEh77ppA1QSV48aNK7vNhHADBgzQokWLNHToUBtsNmrUSF999ZWWLl1qZ6IzwfCXX365x3WbNhAmIJ45c6aeffZZ25B40qRJZfebJsbbtm2zgeicOXNs4Hzqqadq586Sb5jN+s1YnnzySRt61q9fX2+88UaNty0zM1NDhgyxIeuMGTNsde6ZZ55pby8Nf00180UXXWQrmk1gbQJVY8WKFWW3GSbYNSHwW2+9pSVLluh///ufLr/8ck2dOtXtd9533302kF62bJlte7Enl112mX1ezTjM9pvHBgQE2PvMdTOuSy65xO4H8zw89NBDZSG8MXjwYBvQvvLKK/b3vf322woPD6/yd5lQ3ITHP/74oxYvXmxn/rviiis0a9asGs9CaJ6P0ov5vaa9x4knnrhf+998YWDCYBM0m/vfeecdPfDAA/Jqfv4KbtFa2YvKv4CQy6XsRfMU3LpDlQ/JWbnUPia4Zcmbd0Cdego7+nhlzZu93+uEB/n7K7hlG2UtdN9f5roJ8qtigl0T0pZ+gAuoW0/hx3TRrrnV/9/2DS05iCv+928hapf6dYPsgdY/FQJYE8wtW5WpI9pGVvu4xcszdEznaDVqUFKR3bJZmDq1j9TMuZxu6yQN6gYrPjZIs+enuu3/pSszbIBfncXLMnTskTFq3CDEXm/VLEyd20dpxpzyqr3KzCm5xcUuZe7y3JlGODDRXY9SypS/3W7bPmmaYrqWzE/hExCgqGM6KmVyhdNvXS6lTJmu6K5HH+rhogbq1wlSXEyg5i7KKLstK6dIy1bvUoc2VX/Or8zfz0en9YjThN+3u92+ZOUu9eoWp4gwP5mT+3p1i7XVwPOXlv8u1JLPATGBbl/Eln4OMAFudcyXdsd0jlKj+qWfA0LVqX2EZs5LPaD14hAfC7RorayF89yP3RbOU0ib9lU+xLRbs8eDrSoeD3ZR1h6OBQA4uOfunrRr104LFy4su37ppZfqqqvKT+s2Hn20/PQwU736999/2/DVBJDVMeHmiBEj7M8mWH3ttdc0efJkW01rAlcTLJpw11SdGqNGjbJVm6Yi1oSPpmrUVOuai/H444/b6s6aVu+a4LoiEyCa1gEmkDWtKEzFsPndphLXVJYapsrUMC0aStsMmApZEzCb392tWzd7W4sWLew2mEDVVASXMgGm2b6a2Lhxo+6++277/Jc+R6VeeOEFG3SbQNdo06aNDdafe+45WyW7cuVK+/ybsPS0004rG1N1TMXuXXfdVXb91ltv1cSJE+06unTpstexmufIXEpbWdx88832OdnTtu5p/5txm/WYCuPS595Uie/tuTP7wlwqKn39OJ1fZKR8/PxUmO5eUVeUnqrABo2rfIz5VtYvIlJNHjNV3T7y8fdX2i8/aOe3Y/Z7nfAc/4gou7+K0lJ3219BDaveX+ZbetNio9njL5pTL+xrIHXi99oxrprKfB8f1b3qRmUvW6y8RE7Nr41Mv1QjNd29D+rOtHzbQ686n47bpLBQP33y6rE2sPP19dH/fbpBk/5wP7hH7RYb8+/+T3Nvi5Vq9v+/91Xlk6832v3/6ZvHl+3/dz5ep0lTt1W5vDkF98YrW+jXP7YpO6foP94KHCpBdeOVl5zidpu5HhAVId/gIAXERMnX319523ZUWmaHwtpW/7kRnhPz7995U31bkbleet/enHh8jO3VO3Gq+2vjsZdW66HbW+nb945VYWGxcvOLNeKFVdqSXH0vXxx6sf9+DthZ+TWQVrDH94FPx21WaIifPn716LL3gXc/26hf/0g5oPXi0PGPKD12cz8WMNdD93QsEBGlpiNfKDseTP3le+34puR4EIAXhbumP2zF3qzHHXfcbsu8/vrrev/9920gmZOTo/z8fB11VElVQHUqV66aylsT5pa2JNi1a5fi4txPMTXrNqGfYapRb7jhBrf7Tbj622+/1Wi7kpOT9eCDD9oA0fxeUy2anZ1tt2FfrF692j6ucvBonoOjj3aveqjquavOnXfeadtSfPzxxzagNZXMLVu2LNv2c8891215UyVrAm+zHWYCOD8/P7dgeU/MY0wYa8LczZs327GbkLSmPXVLpaen22C8f//+Npje3/1vKqNNO4nSYNeoSchsKqgrftFgmAB5kLxTSIfOdrIs0z8pZ9VyBdZroDpX3qi41Eu1Y9xnnh4eDgHTTzf+/EFK+r9XlbNqmQLrNVTdoTcp/sLLbC/myupde6uCmjTThgf+55HxYnd9eiZo2A2tyq7f+8SS/VpPrxPj1adnHT324gqt35itVs3DdOvVLbQjNd9OqILaqc/JdXT3zW3Krt/z2P5NctW7R4Jd16Ojlmndxmy1bhGm265pZSdWmzAl2W1ZM7naY/d2MMeAtq8vAM859cQ4/e/aZmXX739m5QGv84xeCZo1P007Ut1DvKsuamQn6bzr8eVKzyiwIfDDt7fSHY8s07rE6idsxMF1Ws94Dbu+5BjQuO+JZfu1nl7d4+xnipEvrtT6xBz7OeCWoc3s+8DESlXcOHyEmuPB8y+xxwK5q5crwBwLXHWjCi/YqR1jdz8WwOHJ5fLefrWHg/8s3DVBoqnGLWVOpa9ozJgxturT9Hw14arpEWsqSM3p9HtS2mKglAmQTYsHwwS7JuwzwWtl/9XEXKYlg+k1a1orNG3a1FZ4mvGbYHNfmLEapqWBqYDdU9Vo5eduT0yrBVMlbdZrWlOYkNI816Ylxt6UVtHWlNlf5nkw4bDpt2vGeccdd+zTc2ECYtOewfQHNlXQe7On/b+/hg8fbkPxyvtg/eBz5HRmZlNXUZH8o9xf/35RMSqsVMlZKv6iIcr4Y7LSp0yw1/MT19uG+XWvu107vvl8v9YJzynMTLf7yy86psb7K+GSK5X+x69Km/yzvZ63cb18goNV/4Y7lDL2M3sqV6m619yi8GNP0IaHhqlwp3s1DzzH9NVdurL89LuAgJKuSzFRgW4H5qbiZvW6rGrXc9OQ5rZ6d8q0kn27dmO26iUE67LzGxHu1mLTZu3Q0pXl/fYDS/d/dIAN5kvFmP2/tuTzSFVuuqqFPv06UZP/LDmAX7shy+7/KwY2cQt3TbA78t4OqlcnWLc9sICqXYczVbqmercic70gPVPFuXnKT0lVcWGhguq4F1ME1Y1TXhLvA7XB9DmptuXC7u8BAdpZoYLfXF+zIXuv66sTH6hjOkXqkefdv7gxp+SbSdqG3rVIGzaVBLmmn2+ndhE69/S6euk9zubxFNMnd9nKiq+BkpAm1rwGKnwOMO8Le/occOOQZrZ6d8pfO8o+B5ie6ped39CGu+YMoP1ZLw6dwszSYzf3YwFzvTCt6jZL8ZcMUXqF40FzLGCOB+tdf3tJsU+FYwEAh3HP3SlTptierhdcUP2kCn/99Ze6d++um266yVaqmom7Sqtr95fpr5uUlGT7tpr1VbyYCdCM9u3b7xYgm965NWXGbSb1Mn12SycmS0nZ8wfZwMDAsiCzlJnsyzzWVPxWHqupPj0Qpt2C6d/7yy+/6Pzzz9cHH3xQtu1m/JW3xyxvKnZNQGuC0so9f6tjHmsqgU2fYNNj2bRwMK0d9oUZp3mtmNYZZhK0A2Em5UtMTLTV1aVM7+G9MfvBhMsVL4dLWwYVFSp37SqFdqpQDe7jo9AjjlLuqqVVPsQ3KMhW3lfkKgvQffZrnfCgwkLlrlmpsEr7K6zz0ba/clV8zGuguNKHttLXQIUzMkywG9HlRG145B4VbEs6OOPHfsnJLbKT3pRe1idma8fOfB3bufxLGXOapZkYa/GK6vsiBgX52tMwKyr697RM1F45OUXavDW37GKqblN25um4I2Pc9n+HNpG2r3J1goP8VOyqYv9X2P2lwW6jBiG648GFysik167Tpc2Yr7jeXd1uiz+1u1JnzLc/uwoKlD53ieJ7l7QVs3x8FNerm9JmVOjpCI/JyS22bRFKLyZ4NV/sHHNEeY/t0BBftW8VrqUVAsDq9DslQWnpBZoxz70lV3BgyaFj5c8M5iODz39yVIkDeQ24fw749zVQxecA01d3T58DKh8XlLZnMLYm5+3XenGIjwXWrlJYp6Pcj906HaWclVVXdJsgt+yz/79cxUW7HQsAOIwqd81p+CZQNcGlCdUmTJhgT3M3p9mbybmqY/qlmsnETI9WU+Fr2giYIK5ite++Mm0ITBWtmVTLTLZlQsstW7bYKlZTuWraG9x+++22v6z52bQk+PTTT+1kZnvqLVt53Gas5vEZGRm2jcDeKl5Nha+pMP3hhx9sKGyWN5XKpnLZhJsmUO3Ro4dtT2ACUxMumgrhfWXaT5jxXHjhhfZ53LRpk31OS0P2YcOG6fjjj9fIkSNttazpcWx61pZOKNesWTP7e82Ed2ZCNRPYbtiwwbY9qKoPsnkuTC/j6dOnKyYmxvb0Na8BE1zXhAmdze/+5ptv7PNjXkeGmcCtuknc9sS0uDAtKMw2mP1vJrkzLTSMii1CvE3qj+NU76a7bMCXu2aFYs4cYN+wzWypRr2b77YVlymfl3wJsGvODMX0P19561crd1XJaTjxFw/Rrjkzzbt6jdaJ2mXH92PV4NZ77P7KWbVCsWeV7K+0KRPt/fVvvce+BrZ/+r69vuufGYo9+wLlrVtd1poj4ZIh9vbSD3qmFUPkSb216ekRKs7JLqsMLs7Okmsfz2TAofHVD5s1eGBjbdqao63Jubr60qY28J02s7xv5ouPHqE/Z+zQuJ+32uvTZ+/UFRc2VnJKnm3L0LpFuC4+p6F+mlz+JVpEuL/qxgcpPrbki8wmDUveE001T8UKMXjWV+M3a8jFTZS4pWT/X3N5M+3Ymac/Z5R/Qf3S4531x98pGvfjFnv9r9k7NPiipkrenqd1G7PUxuz/8xrpp0lJZcHu4/d1UJuW4br3scXy9TXV4CVn2GTsKlRhIZU9tYFfWKjCWjUpux7avJEij2yn/J3pyk3cqraP36nghnW14Kp77f0b3hmjpjddpnZP3a3ED8cqvldX1R94hmafc33ZOta99IGOfP8Zpc1ZrPTZC9XstiHyDwtR4ujyyZRRu4z7OVmXDWigTUm5StqWZ9sppKTma9o/5WfxPPdgW02bnarvJpafmWE+Qvc7OV6//JFSOevRxi252rQ117aAeOuTRPv/vsdxMTq2U6QeePbAW0Hgv/XVD1s1+MJG9nNAUnKehg5qXPI5YFZ59eYLj3TQnzN36pufS/7OT5+dqssvbKTklPx/PweE6aKzG+inKdv2ab3wrJ0/jFX9m+9WzppVts2COdazx26//XsscIs5Htyh7Z+VHwvEnHW+ctet+bctw7/HAnPKjwXMWX3mGKGUmXQtqFkLFe3KVGEKLTsAx4W7Jsw1rRBMtawJ+EwgaIJBE7D5mk/51bj++us1b948GzKa4G3QoEG2ite0EthfZj0//fSTHnjgATt52/bt223/1Z49e6pu3bp2GfP7TIXwPffcYydRM8HnjTfeaEPmmnjvvffsxGymSthU2JqesxUnFauKabtgerred999dlwm9P7www9tyGomYDNh+Nq1a23rCLPe+++/f7+231TfmpYRZv0mZDXVyqZyt7SfrFm36Y/78MMP299t9puZrM2E3aXefPNN+/vNvjDratKkSbXjMcGpGXffvn1tn13zvJhg3YTUNWEqhM2XAuec497+wLSSMO0l9mf7TQWw6TlsQmwT2JvWEWefffYBVwU7WebfU+3kWPEXDbYBXN76tdr01AMq+ndCtIC4BLdvZkv66roUf/GV8o+NU1FGun0jTxnzYY3Xidolc/pUbYuKth/K7P5at0YbH7+//DUQX8ft9CrbV9flUsIg8xqIt6+BzH9mlH3gM2L6lfy/bTrSTLxXbstrzyn9N0L+2uizbzYrONhPd93Yyk6Ks2hZhu4auVj5BeX7vkG9YEVFlre/een/1uqaS5vozuta2tN3TRAw/pet+vDLxLJlTjw+VvffVt7f9ZG7Sib0/GDMRn3wxb71o8fB8+nYRLv/77mlTcn+X5quYSMWue3/hvVCFF1h/7/49mpde1kzDbuxdcn+35mv8RO26oMxG+z9CXGBOqlryZlRH77qPj/ArcPna97imn0ewMEVdewR6jb547LrHUaVfK5L/GicFl49XEH1ExTSuH7Z/TnrN9kgt8Pzw9Xs1sHK3ZSkRdc/qJRJ08qW2frVzwpMiFWbEbcpqF6CMhYs06yzrlF+pUnWUHuMGb9VwUG+uvPaZgoP9deiFZka/vRKFVR8D6gbrKgI9xZoph2DOQ1/wu+7n6lYVOTS/c+s0DWDGuuJu9soONjXVgo/8+ZazZrP///a5vNvNiskyFd33dCy7HPA3SOX7vFzwMvvrtXVlzbR/65roZhIf6WkFmj8L0ka/dWmfVovPH8sYI7dEi4uP3ZLfOKB6o8Fxn5qK7YTBg0pOxYwge/2f4uBjJAWbdTk0VFl1+teWTKvkSn22fp6+e1wLpc5axeO5eOqfN4F4GCmEtpURZsJ7EonlqupFRf3PWjjQu3X9ouJWnaB+4SH8B7tx05SzwHlQQa8zx/f9FCPs2vWpgiHp2nfn6wfA9p6ehjwkP4FK3TqJbM8PQx40OQxXXTy+dM9PQx4yNRx3bV84OmeHgY8qN1X3l2wMnvF4VG4dXzb/2b+La+dUA3wBNPiwbR0MC0jTKBr2nCY9hv7GuwCAAAAAAAATuP1re9L+71Wdfnzzz89PTw7iVt14zP9g72d6bN78803q127drbdhGnP8N1333l6WAAAAAAAAMBB5/WVu/Pnl8wEXF3vXE8zPYULCqqeoKa0r7A3M/2G9zSRHwAAAAAAAKrnctFz18m8Ptxt1aqVarOmTZt6eggAAAAAAAAAaiGvb8sAAAAAAAAAAE5EuAsAAAAAAAAADuT1bRkAAAAAAAAAb1Xs6QHggFC5CwAAAAAAAAAORLgLAAAAAAAAAA5EuAsAAAAAAAAADkTPXQAAAAAAAMBLuVw+nh4CDgCVuwAAAAAAAADgQIS7AAAAAAAAAOBAhLsAAAAAAAAA4ED03AUAAAAAAAC8lEv03HUyKncBAAAAAAAAwIEIdwEAAAAAAADAgQh3AQAAAAAAAMCB6LkLAAAAAAAAeCmXi567TkblLgAAAAAAAAA4EOEuAAAAAAAAADgQ4S4AAAAAAAAAOBA9dwEAAAAAAAAv5RI9d52Myl0AAAAAAAAAcCDCXQAAAAAAAABwIMJdAAAAAAAAAHAgeu4CAAAAAAAAXqrY5ekR4EBQuQsAAAAAAAAADkS4CwAAAAAAAAAORLgLAAAAAAAAAA5Ez10AAAAAAADAS7nk4+kh4ABQuQsAAAAAAAAADkS4CwAAAAAAAAAORLgLAAAAAAAAAA5Ez10AAAAAAADAS7lc9Nx1Mip3AQAAAAAAAMCBCHcBAAAAAAAAwIEIdwEAAAAAAADAgei5CwAAAAAAAHgpl8vTI8CBoHIXAAAAAAAAAByIcBcAAAAAAAAAHIi2DAAAAAAAAICXKpaPp4eAA0DlLgAAAAAAAAA4EOEuAAAAAAAAADgQ4S4AAAAAAAAAOBA9dwEAAAAAAAAv5XLRc9fJqNwFAAAAAAAAAAci3AUAAAAAAAAAByLcBQAAAAAAAAAHoucuAAAAAAAA4KVcLk+PAAeCyl0AAAAAAAAAcCDCXQAAAAAAAABwIMJdAAAAAAAAAHAgeu4CAAAAAAAAXsolH08PAQeAyl0AAAAAAAAAcCDCXQAAAAAAAABwIMJdAAAAAAAAAHAgH5fL5fL0IAAAAAAAAAAcehPm5+tw0O+oQHkjJlQD/nXWtUs9PQR40A//10FnDl3k6WHAQ356v5M23TLQ08OABzV67SteA17OvAZOvWSWp4cBD5k8pot+DGjr6WHAg/oXrNDWYZd6ehjwkPrPf6bzblrp6WHAg759o42nhwDsN9oyAAAAAAAAAIADEe4CAAAAAAAAgAPRlgEAAAAAAADwUi6Xj6eHgANA5S4AAAAAAAAAOBDhLgAAAAAAAAA4EOEuAAAAAAAAADgQPXcBAAAAAAAAL+VyeXoEOBBU7gIAAAAAAACAAxHuAgAAAAAAAIADEe4CAAAAAAAAgAPRcxcAAAAAAADwUsXy8fQQcACo3AUAAAAAAAAAByLcBQAAAAAAAAAHItwFAAAAAAAAAAei5y4AAAAAAADgpVwuT48AB4LKXQAAAAAAAABwIMJdAAAAAAAAAHAgwl0AAAAAAAAAcCB67gIAAAAAAABeyuXy8fQQcACo3AUAAAAAAAAAByLcBQAAAAAAAAAHItwFAAAAAAAAAAei5y4AAAAAAADgpYpdnh4BDgSVuwAAAAAAAADgQIS7AAAAAAAAAOBAhLsAAAAAAAAA4ED03AUAAAAAAAC8lIueu45G5S4AAAAAAAAAOBDhLgAAAAAAAAA4EOEuAAAAAAAAADgQPXcBAAAAAAAAL+WSj6eHgANA5S4AAAAAAAAAOBDhLgAAAAAAAAA4EG0ZAAAAAAAAAC9V7PL0CHAgqNwFAAAAAAAAAAci3AUAAAAAAAAAByLcBQAAAAAAAAAHoucuAAAAAAAA4KVc9Nx1NCp3AQAAAAAAAMCBCHcBAAAAAAAAwIEIdwEAAAAAAADAgei5CwAAAAAAAHgpeu46G5W7AAAAAAAAAOBAhLsAAAAAAAAA4ECEuwAAAAAAAADgQPTcBQAAAAAAALxUscvH00PAAaByFwAAAAAAAAAciHAXAAAAAAAAAByIcBcAAAAAAAAAHIieuwAAAAAAAICXcrk8PQIcCCp3AQAAAAAAAMCBCHcBAAAAAAAAwIEIdwEAAAAAAADAgei5CwAAAAAAAHgpeu46G5W7AAAAAAAAAOBAhLvV8PHx0bfffnvQf0+zZs300ksvHdTf8fvvv9vtSUtL8+g6auqUU07RHXfccdB/DwAAAAAAAOBkXtOW4corr9To0aN3u33VqlVq1arVbrdv3bpVMTExOhx0797dbk9UVJScYNy4cQoICPD0MA4Ll52ToL4nRSss1E/LVmfrjU+TtGVbfrXLv/dUK9WND9zt9h9+26m3PktSeKivLju3jo7uEKaE2AClZxZpxvwMffLddmXnFB/krcG+uvy8OurXM9bu/6Wrs/X6R5v3uP8/eLZt1ft/yg698ckW+/Mtgxvo6A7hio0OUG5esV3vB18laVNS3kHdFuybsJ59FXHqOfKLjFbB5g1K/ep9FWxYXeWyCbc/oqDWHXe7PWfxXO146yn7c+SZAxVyzInyi4mTigqVv3GtMr7/XPnVrBOH32ugouhLrlV4j9OV9vUH2vX7Twdl/PhvXDmwoc7snaDwMH8tXpGpl99br817+Hv96atHql5C0G63fzcxWa98sMH+HBMVoOsvb6xjO0UqJNhPm7bm6tNvtujPWakHdVtQc7E9jlOLYVcr6pgjFNygjv654CYlj5+858f07KIOo+5TeIfWyk3cqtVPvalNH33jtkzTGy9VizuvVlC9BGUsXK4ld4xU+uxFB3lrsL9CT+yjsFPOkl9ElAq2bFTGN6NVkLimymVjb3xQQa067HZ77tJ5Sn3vOftzcKfjFdrtVAU0ai7fsAhtf364CreU/F1A7TTorDj1OTFKYSG+Wr42R299vk1btxdUu/w7I5urTtzux+E/TU3TO19ssz8H+PvoqgsS1OPYCPvz/GVZemvMNntcCBzudu7cqVtvvVXff/+9fH19dcEFF+jll19WeHh4tcuPGDFCv/zyizZu3KiEhASdd955GjlypFs+ZwopK/v88891ySWX1HhsXhPuGv369dMHH3zgdpt5civKz89XYGCg6tWrp8PF3ranqKjIvpjMi7M2iI2N9fQQDgsX9IvT2afG6sX3Nys5pcAGfY/d0UQ3PrxGBYVVN9T53xPrVPFl0LRhsJ64s6n++ifDXo+LDlBslL/e/ypZG7fm2Tf/my+vb29/6q1Nh2rTUAMXnhGvc06L1wvvJioppUBXDKirkcOa64YHVla7/28fuVp+Fd5YmjYK0pN3tdCfs9PLblu9IUe/z0jTth0Figjz02Xn1tXjw5pp6D0rVEyfploh5Jjuih4wRKlfvKP89asV3qu/Em5+QEmP3a7iXSX/lytK+b9R8vEr/zjgGxauusNHKWfe32W3FWzbqryv3lNhSrJ8AgIV0fssxd/ykJIevbXKdeLwew2UCu7cRYHN2qgobedB3w4cmEvOqa8B/erqmTfWKml7nq68qJGeHt5WQ+9apIKCqv9g33T/Evn6lr8PNG8coucebKepM8v39303t1B4qJ8efG6VMjIL1fvEOD10Ryv72NXrsw/JtmHP/MJClbFwhRI/HKvjvn59r8uHNGuk48e/rY3vjNH8wXcprnc3dXr7ceVu3a6USdPsMvUHnqH2zw3X4ptHKG3WAjW/bYhO+PE9/d6xn/K38/egtgk+qqsiz7lc6V+/r4KNqxV20hmKve4+bX9mWJXvA6kfvigf/wrvA6Hhih/2tHIXziy7zScwSPnrVihnwQxFX3TdIdsW7J8BfWJ01inRevmjJCXvKNClZ8VrxK0NdetjG6o9FrjrmY1ux4JN6gfpsdsbafrczLLbhl6YoOOOCNNz726xxT3XXlxH913XQMOfTzwUm4WDiGO5vbvsssts4eSkSZNUUFCgq666Stddd50+++yzKpffsmWLvYwaNUodOnTQhg0bdMMNN9jbvv76a7dlTVZpMstS0dHR2he1I807RIKCgmzIWfFy6qmn6pZbbrFtAOLj49W3b98q2zIkJibqoosusk+wCR/PPfdcrV+/3q0y2CTwZqfVr19fcXFxuvnmm+0OL7Vt2zadffbZCgkJUfPmzfXpp5+6jc/lcumRRx5RkyZN7FgbNGig2267rUbblpeXp3vvvVeNGze2jzXVyO+9916VLRU+/PBDux3jx4+3LzCzvPkWYU/rqMq0adN00kkn2e0xjzFjzcrKqtF433jjDbVu3VrBwcGqW7euLrzwwirbMpSOvfLFPN+lvvvuOx1zzDF2XS1atNCjjz6qwsJCebtzT43VFz+maOaCXVq/OU8vvL9ZsdH+6nZ0RLWPydhVpLSM8kuXzuG20nPRypKDtQ1b8myIO2vhLiVtL9DC5dn66Jttdrla8t0A/nVen3iN+X6bZszP1PpNuXr+3UTFmf1/TGS1j8nILFJqRmHZpcuRkdqSnKdFK8r/X0+YmqrFK7NtuLtmY64++iZZdeICVaeKil94hgles6ZPVvaM31WYtElpY96RKz9fYd16V7m8K3uXijPTyi7B7TrLlZ/nFuzl/DNNeSsWqWjHtpJ1jhst35BQBTRocgi3DJ58DRi+UbGKHjhUOz98Wa4i3mdru/PPqKtPvtmi6XPStHZjjp55fa3iYwLV47jqz0xLzyxUanpB2aXrMdHanJSrBUvLD+w7tgnXNxOTtWJNlrZuy7NVu1lZRWrTPOwQbRn2ZvvEP7RyxEtK/u7XGi3f9LpLlLNuk5bd84x2LV+rDW98qqSxE9X89vLP283vuEqJ732pTaPHadeyNVp00wgVZeeq8ZUXHMQtwf4K63mmsmf8ppzZU1WYvFnpY9+TqyBPIV1OrnJ5V06WijPTyy6BbTrZ5XMXlIe7OXOmadekb5S/cvEh3BLsr7N7x+jLCTs1a2GWNmzO18ujk2yRzglHVl1hWNWx4PGdwrR1W74Wr8qx94cG++q07lF6f+x2LVqZozWJeXr14yS1bxmiNs2CD+HWAYfesmXLNGHCBL377rs64YQT1KNHD7366qsaM2aMDWurcsQRR2js2LE2B2zZsqV69+6tJ554wlb+Vs6sTEZXMas0+da+II6RbLsGU936119/6a233trtfhPQmtA3IiJCf/75p13OlF2bVN1U+pb67bfftGbNGvuvWacJUc2llAkkTUhs7jcpvQk4TeBbyuz0F198UW+//bZtF2HC5U6dOtVoGwYPHmzLtl955RX7ojPrqK403MjOztYzzzxjX5hLlixRnTp19mkdZjvN9psy9IULF+qLL76wYa8Jyvfmn3/+sUHwY489phUrVtj/ID179txjS4nSy5QpU+yLvHR5sz/MuG+//XYtXbrUjtk85+Y/jDerGx9gT5ufv2xX2W3mm9UVa3PUrkVIjdbh7yedckKUJv215z7LYSF+ys4tVjFdGWqNegn/7v+llfd/ttq3DK3ROvz9fNSra7R+mVb9abZBgT7q0yNGW7fnK2Vn9ad44RDy81dA4xbKXbGw/DaXy14PbN6mRqsI636qsudOt+Fedb8j7MTTVJydZU/3h5e8Bnx8FDv4Vu2aPN4Gxqjd6tcJUlxMoOYuKq/Qy8op0rLVu9ShTfWfDyu/D5zWI04Tft/udvuSlbvUq1ucPXvDnOzRq1usAgJ8NH8pVfxOFd31KKVMcf8yZ/ukaYrpepT92ScgQFHHdFTK5OnlC7hcSpkyXdFdjz7Uw8Xe+PnZ1gl5qyqEsC6X8lYuVmDT1jVaRegJpyh33ozqPwugVqsbV3K2pSnEKWWO11auz1XbFsE1PhY8uUukJv9d/re9ZZMg24qh4no3JxfYoo+arhc42PLy8pSRkeF2MbcdqL///tsGsMcdd1zZbaeddpo9A37mzPIvwvYmPT1dkZGR8q9wtoRhikNNwWmXLl30/vvv2+LPfeFVbRl++OEHt7DyjDPOsP+aCtJnn3222seZ4LK4uNgGoaW9MEzJtNmxprL09NNPt7eZHr2vvfaa/Pz81K5dO/Xv31+TJ0/Wtddeq5UrV+rnn3/WrFmzdPzxx9vlTVVs+/bty36PqZ41Cb15gZies6aC1+zYvTHr/vLLL21puHmsYSpY98QE1iZcPvLII/drHU899ZQtSS+tsDXPoQmFTz75ZL355pt7/JbBbGdYWJjOOussG5g3bdpURx999F5bSuzYsUPXXHONhg4dai+GqdK97777NGTIkLIxm/4l99xzj+1tUhXzH7vyf25TqXw4iYkq+a9tvnGtKC2zUNH/3rc3XY+OtKddTt5DuBsZ7qdLzorXhD/os1ebxESW9Moy1bcVpWUUlr029sZU+Jr9/+tfu+/b/r1iNXRgPdtrMXFrrh4YtU6FRZzHUxv4hkfIx8/PVt1UVJyRroC6Dff6+ICmrWw17s5P39ztvuAjjlHsVf+zbRmKM9K0/bWRKs4qr+bD4f0aiOhzrlRcRI9dh4iJ/vd9IN39izdzvfS+vTnx+Bjbq3fi1BS32x97abUeur2Vvn3vWBUWFis3v1gjXlhlz/SAMwXVjVdesvt+NtcDoiLkGxykgJgo+fr7K2/bjkrL7FBY2z0fc+DQM/1wq3wf2JUu/zoN9vr4gMYtFVC/idK/+L+DOEocTNFRfmWf/StKzyhSTGTNjgVMha/p1Tt5RvnryDy2oKBYWZXmWknLrPl6gYPtqaeesjlRRSYbMmfJH4ikpCRbFFmRCWjNmf3mvppISUmxeZVp5VCRKXw0Vb2hoaG2P+9NN92kXbt21fhMfjsWeZFevXrZ4LGUCRgHDRqkY489do+PW7BggVavXm2DyIpyc3NtBWupjh072mC3lGnPsGhRySQDphLW7PiKv8sEwBX7aAwcOFAvvfSSDShNVeyZZ55py7crJ/qVzZ8/3/5eE6zWlAlNO3fuvN/rMM+Jqdit2FrCfLNgQvB169a5hdaV9enTxwa6pdtpLgMGDLAv5D2F0aZK2DzONKyuOA5TSV2xUtf0EDb7xlQnV7XO6v6zSxfJqU45IVI3X17+Ye3RVzce8DpP7xGtOYt3aWd61afehgT7asStTbRxS74++969qgeH1ildo3Xr4PL9P+KlA6+mPP2kGP2zKFM703bf/7/NSNO8Jbtsm4/z+yZo+I1NdNeT1fdyhnOY0/bzN2+ocuKtvJVLlPzU3fILj1BY99MUN/RObRs1nJ67XvAaMJXA4af0V/Iz93h0bKjeqSfG6X/XNiu7fv8zKw94nWf0StCs+WnakeoeEF91USOFh/nprseXKz2jwIbAD9/eSnc8skzrEktO3QXgXCEnnGInYKtu8jXUPj2Pj9CNg+qWXX/8zc0HvE7TfmHu0iylpjNRmrdwuXaf1MuJhg8frjvvvLPGxXymWNCc1b4nJs87UKaC2BSAmtaolYPmhx56qOxnU/ho2p0+99xzhLvVMWGu6SNb1e17YhJzE8pW7pFbeUI2U21bkanyNWFnTZm+taZNwa+//moraE1ab3bo1KlTd1t3Rabn7b4yj6k4I9++rsM8J9dff32VLzZTcbwnJiSfO3eurXo230o8/PDD9sU9e/bsaptG33jjjbalhal8rhh2m3GYoPb888/f7THVVQ9X95/9gluc+wFm5vxdWrG2fPwBASUdV6Ij/ZRaIZyNjvDXusTcva4vITZAR7YP05NvVN0YPyTIV4/d3kQ5uUV64o1EFfGe71Ez52fYlgulzOlShvkG3W3/R/pr7ca9738zUd5RHcL1xGtVh8SmxUN2Tr7tx7x8zUZ9+VoHdT82UlNnuleI4NAr3pUpV1GRfCPKZ181fCOjVJSx5xYrZqKU0GNPVMaPX1R5vzk1syglyV7y169S3YdfUVj33sr8pbw/PQ7P10BQy3byDY9U/cfKvyA3VWFR5w+xk7Uljbj5P94K7Kvpc1Jty4XKnwNiogK0M608nDXX12zY+6Rnpo/6MZ0i9cjzq9xur183yE7SZiZl27CpJMg1/Xw7tYvQuafX1Uvvlc9HAecwVbqmercic70gPVPFuXnKT0lVcWGhgurEVVomTnlJ7hW/8DxzVk2V7wPhUbav+t7eB0KO6qbMie4T/aB2M/OhmJYLlY8FzGf/1ApnckZF+mndpr2fZZEQ66/O7UL1zDvufUTNWYHm/cVU9Fas3o2O8NvtjEHAU4KCgvbpzOxhw4a5zelUFVOYaM4or9hW1TB9c3fu3Fl2tnl1MjMzbVGjycK++eabPeZ7hunpayp8zRnnNd0Wrwp395eZrMu0ZjAl2KY3xv4wVbpmx8+ZM6esLYMJcksnOasYsppqXXMxPTfM40z1rxlDdUxfXhMimxC4tKXCvtrXdZjxmB63VYXlNWECWvN7zMVUzZpQ1/TTrSqkfeGFF2zLiOnTp9uJ6iqPwzyP+zKOff3P7gQ5ecXK2e7+RYI5mDuqXZjWJeaVVdq2bRGin6fuvYVCnxOjlZ5RqNmLyg8US5n1jLyjia3SHPl6ItWatUBObrFycsv7f5fu/yM7hGvtv2F+yf4P1Y+/7X1Ga9NH1+z/WQtrcMq9j/uHSHhYUaEKEtcquG0n5S6cXXKbj4+C2nRS1h8T9vjQkKO72Zmys2f/UaNfZSe49K/Z6d1w9mvAXM9dUXImUqmEmx9U1qw/7IQ9qC3vA+4H7DtS83XMEZFlYW5oiK/atwrX95PcD0yq0u+UBKWlF2jGPPfPqcGBJaGxq9KU2qaWwYeZPBwrbcZ8JZzhPv9F/KndlTpjvv3ZVVCg9LlLFN+7m5LHTy5ZwMdHcb26acMbn3hiyNiToiIVbFqnoNYdlbf4n/L3gdYdlfXXL3t8aPCRJ9j3ATN5GpwjN89lJ7uuyJx92bltaFmYa44FzKRnE/7YezHGqd2ilJ5ZpH8Wu0+WvmZjnj32M+v9e37JcWKDOgG2MGTF2r0XkAC1UUJCglvRZnW6detm8zuT6ZWekW8yLJOjmTB2TxW7Zg4vk0GNHz++RhOlmTPrTdvXfcmtCHdrwPSWNRW05557ru2F0ahRI23YsEHjxo2zvV3N9b1p27atTepNtatpDWHCTdOvtmLFrJkIzLQUMC8M007gk08+sfebVgR70qxZM9tz1vShNX1vTR9dMz7zrcJFF9Ws1cC+ruPee+9V165d7QRqpg+uqX42Ya+pODZ9h/fW+3jt2rV2UjTzgv3pp5/sfwjzHFVmqpjNc/z666/b5tKlvUzM8xIVFWWrfk3vXlMtfOGFF9pm1qZVw+LFi/X444/Lm303eacu7p+gzdvylZxSoMvPTbCn2P89rzywe+LOpvp7XoZ++K088DUF3aedGKXJf6fvNkmaDXb/10RBgb4a9V6ivR7y79+mjMwiVTrWgwd9OylFl5xVx/ZATN6erysG1NUOs//nlp9C/+RdzTV9boZ+mLLDbf/3OTFGv05P3W3/m4naeh4frblLMu0HvviYAA08M0H5BcWaXZMgGIdE5pQfFHvFzcrfuEb561fbykrfoCBl/RvCxVxxi4rSdypj/Ge7nY6fs3C2irN27VbFE9H3fOUu+kdF6am2gjO8Z1/5Rccqe677BDw4PF8D5nrl21xFhSrOSFXhtqpnB4bnjfs5WZcNaKBNSblK2pZn2ymkpOZr2j/l7/nPPdhW02an6ruJ29zeB/qdHK9f/kjZ7X1g45Zcbdqaa1tAvPVJojJ2FarHcTE6tlOkHnj2wFtB4L/hFxaqsFblZ9KFNm+kyCPbKX9nunITt6rt43cquGFdLbjqXnv/hnfGqOlNl6ndU3cr8cOxiu/VVfUHnqHZ51xfto51L32gI99/RmlzFit99kI1u22I/MNClDh6nEe2EXuW9cdPir7kBvtlX8HGNQrteYZ8AoOVM2uqvT9q0I0qTt+pzJ/cz9QI7XKKchfPkSt79wIPn5Aw+cXEyy8yxl73r1Pf/muqgSv394XnfT8lVQPPiLVn2pkJzy49O94GvjMXlO/bx25rpBkLdumnqWlu7wG9u0bqtxkZu70HmEnZfp2erqsuSFBmdpFycop17cV1tHxtjlvlMHA4at++vc30zJxab731lm0davKwSy65RA0alLRI3Lx5s0499VR99NFHdv4sE+yaObpMy1CT75VO8GaYQNm0Rv3++++VnJxs8zUT/JpM7cknn9Rdd921T+Mj3K0BE7T+8ccfNtA0laWmpLphw4Z2p+1LJa+ZhM0Eoaavbd26dW34WLG3hqleffrpp23LABPymmpas6MrV6tWxQTG999/v23lYCYeM2Gnub4v9mUdpl+vqfJ94IEHdNJJJ9l+uy1bttTFF1+8199jttME46YVg+mNayZj+/zzz23P4sqmTZtmn4sbbrjBXkqZINqE4eYbEBMWm9Dd9Ekx5e2m2tk8z95u7IQdtsLm1isaKCzUV0tXZevhlze6VdqasC4y3P3PwFHtw1QnLlCTqphIrVWTYLVrUdLH+N0n3WfbHXrfKvvBAbXD1z+nKDjIV7cOaWgnRlti9v8L69z2f/06gYqKKO8Tbph2DOZ03El/7l7hnV/gUsc2YTq3T5ztt2gmaVi8IlvDnlxjw17UDjlzpystPFKR/S+WX0S0CjavV8rrT5QdePnHxttZsysyE6wEtWpvJ0mrzFVcbCfiCjvhFDtJS3F2pvI3rNG2Fx9WYdKmQ7Zd8NxrAM40ZvxW+z5w57XNFB7qr0UrMjX86ZUqKCjf9w3qBisqwr0C37RjqJsQpAm/7366fVGRS/c/s0LXDGqsJ+5uo+BgX/sl4jNvrtWs+YQ7tUXUsUeo2+SPy653GFXyeT7xo3FaePVwBdVPUEjjkmDOyFm/yQa5HZ4frma3DlbupiQtuv5BpUwqr97c+tXPCkyIVZsRtymoXoIyFizTrLOuUX6lSdZQO+TOn6GMsEiF971QfpHmfWCDdv7f02V98v2i48wbvNtj/BLqK7BFO+14+8kq1xl8xLE2MC4Vc0VJe77MiWO165exB3V7sO++mZRq3wNuurSuPRZctiZHj722uYpjQfdjgSPbhdpKXFPoU5X3v95uP0Lce20De+bevGVZenvM3s8IQe1X6aMhqmBatZpA12SBprDQzAtliiNLmcDXnFluwlzDtCOdOXOm/bny2eZmripTZGkyLFPM+L///c/mamY5c/a6CZH3hY/LPBqAzrp2qaeHAA/64f866Myh7qcdw3v89H4nbbploKeHAQ9q9NpXvAa8nHkNnHrJLE8PAx4yeUwX/Riw+1lk8B79C1Zo67BLPT0MeEj95z/TeTdxBoI3+/aNNvJmH5UU9jve4JPlleiOBQAAAAAAAAAORLjrAH/++afCw8OrvdQ2ThsvAAAAAAAA4ET03HWA4447zs6W5xROGy8AAAAAAIC3YnJ0ZyPcdYCQkJDdmi/XZk4bLwAAAAAAAOBEtGUAAAAAAAAAAAci3AUAAAAAAAAAB6ItAwAAAAAAAOClXPTcdTQqdwEAAAAAAADAgQh3AQAAAAAAAMCBCHcBAAAAAAAAwIHouQsAAAAAAAB4KXruOhuVuwAAAAAAAADgQIS7AAAAAAAAAOBAhLsAAAAAAAAA4ED03AUAAAAAAAC8VDE9dx2Nyl0AAAAAAAAAcCDCXQAAAAAAAABwINoyAAAAAAAAAF7KRVsGR6NyFwAAAAAAAAAciHAXAAAAAAAAAByIcBcAAAAAAAAAHIieuwAAAAAAAICXKi729AhwIKjcBQAAAAAAAAAHItwFAAAAAAAAAAci3AUAAAAAAAAAB6LnLgAAAAAAAOClXC5PjwAHgspdAAAAAAAAAHAgwl0AAAAAAAAAcCDCXQAAAAAAAABwIHruAgAAAAAAAF6KnrvORuUuAAAAAAAAADgQ4S4AAAAAAAAAOBDhLgAAAAAAAAA4ED13AQAAAAAAAC9VTM9dR6NyFwAAAAAAAAAciHAXAAAAAAAAAByIcBcAAAAAAAAAHIieuwAAAAAAAICXcrkOl6a7PvJGVO4CAAAAAAAAgAMR7gIAAAAAAACAAxHuAgAAAAAAAIAD0XMXAAAAAAAA8FKHTctdL0XlLgAAAAAAAAA4EOEuAAAAAAAAADgQ4S4AAAAAAAAAOBA9dwEAAAAAAAAvVVzs6RHgQFC5CwAAAAAAAAAORLgLAAAAAAAAAA5EuAsAAAAAAAAADkTPXQAAAAAAAMBLuVyeHgEOBJW7AAAAAAAAAOBAhLsAAAAAAAAA4ECEuwAAAAAAAADgQPTcBQAAAAAAALxUMT13HY3KXQAAAAAAAABwIMJdAAAAAAAAAHAgwl0AAAAAAAAAcCAfl8tFZw0AAAAAAADACz3/7eERDQ47z0feiAnVgH+dOXSRp4cAD/rp/U7qO2S+p4cBD5k4+ihtvOF8Tw8DHtTkrXFaN/QcTw8DHtT8/fE6+fzpnh4GPGTquO7aOuxSTw8DHlT/+c/0Y0BbTw8DHtK/YAXHg17OHA8CTkVbBgAAAAAAAABwIMJdAAAAAAAAAHAg2jIAAAAAAAAAXspVfHj03JW8s+culbsAAAAAAAAA4ECEuwAAAAAAAADgQIS7AAAAAAAAAOBA9NwFAAAAAAAAvNRh03LXS1G5CwAAAAAAAAAORLgLAAAAAAAAAA5EWwYAAAAAAADAS7loy+BoVO4CAAAAAAAAgAMR7gIAAAAAAACAAxHuAgAAAAAAAIAD0XMXAAAAAAAA8FLFxTTddTIqdwEAAAAAAADAgQh3AQAAAAAAAMCBCHcBAAAAAAAAwIHouQsAAAAAAAB4KRctdx2Nyl0AAAAAAAAAcCDCXQAAAAAAAABwIMJdAAAAAAAAAHAgeu4CAAAAAAAAXoqeu85G5S4AAAAAAAAAOBDhLgAAAAAAAAA4EOEuAAAAAAAAADgQPXcBAAAAAAAAL1VM011Ho3IXAAAAAAAAAByIcBcAAAAAAAAAHIhwFwAAAAAAAAAciJ67AAAAAAAAgJdyFXt6BDgQVO4CAAAAAAAAgAMR7gIAAAAAAACAAxHuAgAAAAAAAIAD0XMXAAAAAAAA8FIul8vTQ8ABoHIXAAAAAAAAAByIcBcAAAAAAAAAHIhwFwAAAAAAAAAciJ67AAAAAAAAgJcqLvb0CHAgqNwFAAAAAAAAAAci3AUAAAAAAAAAByLcBQAAAAAAAAAHoucuAAAAAAAA4KVcLpenh4ADQOUuAAAAAAAAADgQ4S4AAAAAAAAAOBDhLgAAAAAAAAA4ED13AQAAAAAAAC9VTMtdR6NyFwAAAAAAAAAciHAXAAAAAAAAAByIcBcAAAAAAAAAHIieuwAAAAAAAICXctF019Go3AUAAAAAAAAAByLcBQAAAAAAAAAHItwFAAAAAAAAAAei5y4AAAAAAADgpVy03HU0KncBAAAAAAAAwIGo3D2MuFwuXX/99fr666+VmpqqefPm6aijjvL0sOBBl59XR/16xios1E9LV2fr9Y82a8u2/GqX/+DZtqobH7jb7T9M2aE3Ptlif75lcAMd3SFcsdEBys0rtuv94KskbUrKO6jbgn03eEA99TslTuFm/6/K0iujE7Ulufr9P3pUB9VL2H3/j/91u17/eLP9+dn7WunI9uFu9/84JUWvjN50ELYA+yv85H6KPP08+UVGK3/TeqV+8a7y16+uctk6dz6m4DZH7HZ7zqI52v76E7vdHnPp9Yro2VepX76vzCk/HJTx48BF9D5TUf0GyC8qRvmJ67Tj03eUv25VlcvWu+cJhbTrtNvt2QtmK/nlkfbn5u+Pr/KxO7/8QOkTvvmPR4//ytBLGuusPnXt+8Ci5Zl64Z212rw1t9rlfX2lKy9urNN7Jtj3+ZTUAk34bZs++mrTAa0Xh17oiX0UdspZ8ouIUsGWjcr4ZrQKEtdUuWzsjQ8qqFWH3W7PXTpPqe89Z38O7nS8QrudqoBGzeUbFqHtzw9X4ZYNB307sO9iexynFsOuVtQxRyi4QR39c8FNSh4/ec+P6dlFHUbdp/AOrZWbuFWrn3pTmz5y/9ve9MZL1eLOqxVUL0EZC5dryR0jlT570UHeGhwIjgUB70G4e4CuvPJKjR492v4cEBCgJk2aaPDgwbr//vvl77//T+/vv/+uXr162ZA2Ojq6Ro+ZMGGCPvzwQ/vYFi1aKD4+fr9/P5zvwjPidc5p8Xrh3UQlpRToigF1NXJYc93wwEoVFFZ9zsXtI1fLz8en7HrTRkF68q4W+nN2etltqzfk6PcZadq2o0ARYX667Ny6enxYMw29Z4WKOZWj1rjozDo6t0+CRv3fBiWl5GvI+fX15F0tde39y1VQUPWOuu3RFfL1Ld//zRoG6+l7W7ntf+On31P00biksut5ecUHcUuwr0KPPVExF16lnZ+9rbz1KxXZ+yzVufVhbXnkVhVnuu9LI+WtZ6UK71d+YRGq9+ALyp47fbdlQ446QUHN26gwbcdB3w7sv7Djeyju4quV8vEbylu7UpF9zlG9Ox/VpvtvrPI1sO31p+TjV/4a8A2PUMNHX1HWP3+V3bbxjsFujwnpfKzir7xVWXN2f52gdhg0oKHO719fT72ySlu35enqQU006qEOGnL7POVX8z5w6YCGOrdvPT316mqt35ittq3Cdd8trZSVVaixPyXt93pxaAUf1VWR51yu9K/fV8HG1Qo76QzFXneftj8zTMW7MnZbPvXDF+VT4X3ANzRc8cOeVu7CmWW3+QQGKX/dCuUsmKHoi647ZNuCfecXFqqMhSuU+OFYHff163tdPqRZIx0//m1tfGeM5g++S3G9u6nT248rd+t2pUyaZpepP/AMtX9uuBbfPEJpsxao+W1DdMKP7+n3jv2Uv33nIdgq7CuOBQHvQluG/0C/fv20detWrVq1SsOGDdMjjzyi554r+Zb7UFqzZo3q16+v7t27q169elWGy/n51X9Th8PLeX3iNeb7bZoxP1PrN+Xq+XcTFRftr27HRFb7mIzMIqVmFJZduhwZqS3JeVq0IqtsmQlTU7V4ZbZ9Q1+zMVcffZOsOnGBqlPFt7zwnPP6Jujz75P097wMrUvM1bPvbFBcdIC6HxNV7WPSzf5PLyy7nHBUlN3/C5fvclsuL8/ltlx2LuFubRJx2tna9dckZf09RYVbN9mQt7ggT+Hde1e5fHH2LhVnpJVdgtsfKVd+nrIrhXZ+0bGKufga7Xj/Jamo6BBtDfZHZN9zlfnHL9o1bbIKtiRqx0dv2H0acdJpVS5fnLVLRRlpZZeQjkfb5bNml4e7Fe83l9CjTlDu8kUq3J58CLcM+2LgWfX18deb9NfsVK3dkK0nX1mluNhA9egSW+1jOraN0F+zdmrGnFQlbc/T1L93aPb8NLVrHXFA68WhFdbzTGXP+E05s6eqMHmz0se+J1dBnkK6nFzl8q6cLPvFT+klsE0nu3zugvJwN2fONO2a9I3yVy4+hFuC/bF94h9aOeIlJX/3a42Wb3rdJcpZt0nL7nlGu5av1YY3PlXS2IlqfvuVZcs0v+MqJb73pTaNHqddy9Zo0U0jVJSdq8ZXXnAQtwQHgmNB7KviYtdhcfFWhLv/gaCgIBumNm3aVDfeeKNOO+00jR8/3lbdmiremJgYhYaG6owzzrABcKkNGzbo7LPPtveHhYWpY8eO+umnn7R+/XpbtWuY+3x8fGyF8J6Y+2+99VZt3LjRLt+sWTN7+ymnnKJbbrlFd9xxh63k7du3r7198eLFdjzh4eGqW7eurrjiCqWkpJStLysry47d3G8C4+eff96uy6ynlPk93377rds4TJWxqR4ulZiYqIsuusjeHhsbq3PPPdduX8Vxn3feeRo1apT9PXFxcbr55ptVUFBQtkxeXp7uvfdeNW7c2D7XrVq10nvvvWfbUJifzWMrmj9/vh3b6tVVn4LsDeolBNhTZeYvLQ/lsnOKtWJtttq3DK3ROvz9fNSra7R+mZZa7TJBgT7q0yNGW7fnK2Vn+T6DZ5nWCibInbvEff8vN/u/VViN93/v7jGa+MfuFZq9usXoy9eO0NtPtNVVA+vb1wFqCT9/BTZpqdxlC8tvc7ns9cAWbWu0irATT1X2P9NsuFfGx0dxV96uzEnfqmBr4kEYOP4zfv4KatpKOUvnl9/mciln6QIFtWxXo1WYEHjXrD/dXwMV+EZGK7Tzccr8c9J/NWr8x+rXDVJcTKDmLEgruy0ru0jLVmXaALc6S1Zk6pjOUWpUP9heb9ksVJ3aR2jmvNQDWi8OIT8/2zohb1WFENblUt7KxQps2rpGqwg94RTlzptR7d8AHF6iux6llCl/u922fdI0xXQtae/nExCgqGM6KmVyhS99XS6lTJmu6K5HH+rhogY4FgS8D20ZDoKQkBDt2LHDBpcmzDVBb2RkpA0ozzzzTC1dutS2cDAhpqmk/eOPP2y4a243YaoJMceOHasLLrhAK1assI8169yTl19+WS1bttQ777yj2bNny8/Pr+w+0zbChM5//VVSgZOWlqbevXvrmmuu0YsvvqicnBw7NhPCTpkyxS5z9913a+rUqfruu+9Up04d22Zi7ty5+9TD1wS0Jkzu1q2b/vzzT1tJ/Pjjj9tK54ULFyowsOTbvd9++80Gu+ZfE8hefPHF9vdce+219n4TMv/999965ZVXdOSRR2rdunU2iDYB7tChQ/XBBx/orrvuKvu95nrPnj1t8FsVExabS0UmND6cxEQG2H/NN64VpWUUKiaqZv/tzbe6ppfer3/t/obev1eshg6sp5BgPyVuzdUDo9apsMh7vyWrbWL/3cdp6e4fstIyCsru25vux0bZ/f/LNPdT7X6bkaptKfnakVag5o1DdPVF9dWoXpBGvlr+pQ08xy88Qj5+fraysqLizDQF1Gu418cHNmulwIZNtfNj99M4I08fIFdxkTKn/Pifjxn/Lb+IyCpfA+Z6QP0avAaat1Zgo2ba/sGr1S4T0b23inNzlD3HPQxA7REbXfIZa2el94HUtALFxlRfXfXpuM0KDfHTx68ebatfTKuedz/bqF//SDmg9eLQMf1wzd+Ayi1Yinely79Og70+PqBxSwXUb6L0L/7vII4StUlQ3XjlJZcX+RjmekBUhHyDgxQQEyVff3/lbXP/wj8veYfC2rY4xKNFTXAsCHgfwt3/kKkknTx5siZOnGirYk1VqwlUTZsE49NPP7XBrbl94MCBtsrWBLidOpVMYmL65JYyVa6GCVZr0nM3KipKERERNtQ1VcQVtW7dWs8++2zZdROwHn300XryySfLbnv//fft2FauXKkGDRrYythPPvlEp556allA3KhRo316Pr744gsVFxfr3XfftUFsafBqtsf0BT799NPLqpNfe+01O/Z27dqpf//+9nk04a4Zz5dffqlJkybZiujKz5MJ0B9++GHNmjVLXbp0sYHyZ599tls1b0VPPfWUHn30UbfbRowYIcm5pxWd0jVatw4u/8A+4qUDn+Di9JNi9M+iTO1Mc/9QYPw2I03zluxSbLS/zu+boOE3NtFdT66ptn8TDi5TSXv7leX/Px96Ye0Br7Nvz1jNXpix2/7/+ffyD/bmFK+daQV2krX6dQK1dQ8TNMAZwrqfZidgqzj5WkCTForo3V9JT5Z/iYbDV8RJfZSfuL7aydeMcFPZO2OqXIVU6dQWp/WM17DrW5Zdv++JZfu1nl7d49SnZ4JGvrhS6xNz1Kp5mG4Z2kwpO/M18fft/+GIUVuFnHCKnYCtusnXANQ+HAviv8qz4FyEu/+BH374wVbcmmDRhJmXXnqpzj//fHv7CSecULacaTnQtm1bLVtW8oH7tttusxW1v/zyiw0uTdDbuXPn/3x8xx57rNv1BQsW2CpZM+aq+vaaSl5TUVxx7CZsNmPfF+b3mEpcEzpXlJuba39PKdOOomKlsaniXbRoUVmLBXPfySdX3SPMBNEmDDbhtAl3v//+e1uVa8Lz6gwfPlx33nnnbpW7A25cKaeaOT/DnmZTKsC/JEyPifS3PVFLRUf6a+3Gvc9mXScuQEd1CNcTr1X9wcCc1pOdk29nW12+ZqO+fK2Duh8bqakzd5+oBwffjHnpWrGmvBdWQEBJx53oqADtdNv/AVqzMadG+//ojhEa+cq6vS67fE3J665BnSDC3VqgaFemXEVF8ot0/1LQNyJ6t0rOysxkOWHHn6j078e43R7cqoN8I6LU4Ml3ypf181P0hUMUcepZ2vLADf/xVuBAFGVmVPkaMNeL0vf+GgjvcpJSv/2s2mWCWndQYP1G2m4m4kOtYfrkLltZfvptQEDJ54BY8z6QWh7Cx0QHaPW68veLym4c0sxW7075q+SLvLUbs1U3IUiXnd/Qhrs70/L3a704dIqzSt4HzN/tinzDo+xZHHv7GxByVDdlTvz6II8StYmp0jXVuxWZ6wXpmSrOzVN+SqqKCwsVVCeu0jJxyktyr/iFZ3AsCIBw9z9g+uO++eabts2ACRtN+wHTimFvTFsE07bgxx9/tAGvqSg1vW1N79z/kmn5UNGuXbtsr99nnnlmt2VNsFrTXrWmGrfytzsVe+Wa32OCZVOxXFlCQkLZz6ZFReX1mpDc2Fs7itLn0fQMNi0mTGWwaetgehxXxwS5h1sbhpzcYuXkugdrpqLyyA7hWptY8gYeEuyrti1C9eNve5/R1vROSs8o1KyFmXv/5T7uHyJQO/a/aZtwtNn//4a5ocG+atciVD9M2fuH8NNPirOnbc1csPuM2pW1bBpS5Sm68JCiQuVvXKPgdp2Vs2BWyW0+Pvb6rt9/2uNDQ4/tLh//AGXNnOp2e9bM35W7fKH73/DbHlLWjKl20jbUMkWFytuw2k6Mlz3v38mQfHwU0r6zMvbSVsOE+woI0K6/f99jZW/e+lW2uhe1631gc5L7AfuO1Hwd0zlaq9eXHPCbdgvtW0fouwlJ1a4nKMh3t892pe0ZjK3Jefu1XhxCRUUq2LROQa07Km/xPyW3+fjY61l//bLHhwYfeYJ8/P3t5GnwHmkz5ivhjJ5ut8Wf2l2pM0p6t7sKCpQ+d4nie3dT8vjJ5b34e3XThjc+8cSQUQnHggAId/+j8LRyf9f27dursLBQM2fOLGvLYPrwmh66HTp0KFvOtEK44YYb7MVUlP7f//2fDXdL+9EWHYQZyY855hjb09dMumaC6MpM714TuJqxN2nSxN5mJoczLRIqVtCagHbr1q1l101/4ezsbLffY1ozmNYSpm/w/jAtK0zQa/r/lrZlqMz0MTb7wATsEyZMsD2MIX07KUWXnFXHznCavD1fVwyoqx1phfp7bnlg9+RdzTV9boZ+mFJ+qr3poNHnxBj9Oj1V/2bsbs35ex4frblLMpWeWaT4mAANPDNB+QXFml2TN38cMt9O3K5B59TV5uQ8JW3P15Dz69vAd/rc8m/Un76npb0+/tcUt/1/+kmx+nXazt32v2m90KtrjGYtzFDmriI1bxys6y9tqIXLd2ndvx8c4XmZv36vuCtvVf6G1TaEi+h9tnwDg7RrekkQG3flbSpM26H0b92/eAvrfqqy589ScVZ59Z9hrle+zYQHxRlpKkzecvA3CPssY+J3ir/mDtteI2/dSkX2OUc+QcHKnFZyUG7uK0rdqdSxH+0W3GbPnWEr/6riExxiA+CdX7x/SLYDB+arH7Zq8IWNtGlrjpKS8zR0UGPt2JmvabPKD+xfeKSD/py5U9/8XBLMTp+dqssvbKTklHyt35it1i3CdNHZDfTTlG37tF54VtYfPyn6khtUkLhWBRvXKLTnGfIJDFbOrJIv76IG3aji9J3K/OkLt8eFdjlFuYvnyJW9a/f//yFh8ouJl19kjL3uX6e+/ddUA1fu7wvP8gsLVVirkmM4I7R5I0Ue2U75O9OVm7hVbR+/U8EN62rBVffa+ze8M0ZNb7pM7Z66W4kfjlV8r66qP/AMzT7n+rJ1rHvpAx35/jNKm7NY6bMXqtltQ+QfFqLE0eM8so3YO44FAe9CuHuQmD635557ru0b+/bbb9vWBPfdd58aNmxobzfuuOMO25u3TZs2Njw1rRJMKGw0bdrUVrCa1g4mvDQVrFW1UdgfZiI3EyIPGjRI99xzj225YKp1x4wZY/vjmt9z9dVX20nVTCsJE84+8MAD8vUtOdW7lJmUzfTKNROmmRDaTMpWsQr3sssu03PPPWe397HHHrM9ezds2KBx48bZ31uTHr4mgB4yZIidOK10QjWzjm3bttkJ4AzTtsH03jXhuHnezXggff1zioKDfHXrkIa2Gf6SVdl6+IV1br2QTFgXFVHeEsMwp+DUiQ/UpD93b56fX+BSxzZhOrdPnMLD/Gx15+IV2Rr25Br7Bo/a48ufttn9f/uVjf/d/1l6YNRaFRRU3P9Bigx3fxsw7Rjqxgdq4h+7H6QXFrrs/QP6Jig40FfbdxZo2uw0fT4++ZBsE2ome85f8o2IVNTZg+yp+Pmb1mnbqyPLDr79YuPlcrl/Wvev20DBrTto28vu/cjhTFmzp9lTsmPOu1R+UTHKS1yr5BcfsYG84R+bIBW7V2eaCfeC23TU1lEPV7ve8BNMZZePds3kS1Qn+PybzQoJ8tVdN7RUeJi/Fi3L0N0jl9r38lIN6gUr6t+Jd4yX312rqy9tov9d18KezpuSWqDxvyRp9Feb9mm98Kzc+TOUERap8L4X2veBgs0btPP/nlbxrpJQxy86Tqr0PuCXUF+BLdppx9vlc3JUFHzEsTYwLhVzxW3238yJY7Xrl7EHdXuwb6KOPULdJn9cdr3DqPvtv4kfjdPCq4crqH6CQhqXhPNGzvpNNsjt8PxwNbt1sHI3JWnR9Q8qZVJ5BffWr35WYEKs2oy4TUH1EpSxYJlmnXWN8itNsobag2NB7KtKbwtwGB8XXZMPiAkV09LS7CRplZnA9vbbb7ctGkwP2549e+rVV1+1AaRhKnR//vlnbdq0yVa29uvXz7YWMIGqMXLkSL3xxhtKTk7W4MGD9eGHH+5xLC+99JK9rF9ffqrkKaecoqOOOsreXpGpsjVhrAmUTY9aEyab3//CCy/YUNm0VDD9gE0Qa4LpYcOG2fYRFde1ZcsWXXXVVXbSONOO4uWXX7aBsbnfPC9GUlKS/T0//fSTMjMzbbhtJmkzE56Zba7q+TOht+m1ayZdK+3Re//999vw2VQ/m2pic9387lJr1661Fcdm4jgTSu+PM4eW9PmFd/rp/U7qO6Tk9DN4n4mjj9LGG8739DDgQU3eGqd1Q8/x9DDgQc3fH6+Tz5/u6WHAQ6aO666twy719DDgQfWf/0w/BuzbHCM4fPQvWMHxoJczx4Pe7J639j43ixM8e8PeW3sejgh3UWPVBcW1wZ9//mlD48TERNWtW3e/1sGbuXcj3PVuhLsg3AXhrncj3AXhrncj3AXhLuGuk9GWAY5mqo63b9+uRx55RAMHDtzvYBcAAAAAAABwGvcmqqi1Nm7caHvhVncx93ujzz//3LaUMK0dTEsGAAAAAAAA1Fyxy3VYXA6mnTt32rmlTIvR6OhoO1eVaWm6tzPgTevTipcbbijvYW+YPK9///4KDQ21c16ZVqOFhYX7NDYqdx3C9LQ1fWj3dP/BVtoDtzYxPXtL+/sCAAAAAAAA/zUT7G7dulWTJk1SQUGBnQfquuuu02effbbHx1177bV67LHHyq6bELdUUVGRDXbr1aun6dOn2/WbObcCAgL05JNVT3JaFcJdh/D391erVq08PQwAAAAAAACgVrbuzMvLc7stKCjIXg7EsmXLNGHCBM2ePVvHHXecve3VV1/VmWeeqVGjRu2x4NKEuSa8rcovv/yipUuX6tdff7VtRs08VyNHjtS9995r248GBgbWaHy0ZQAAAAAAAADgaE899ZSioqLcLua2A/X333/bVgylwa5x2mmnydfXVzNnztzjYz/99FPFx8friCOO0PDhw5Wdne223k6dOrnNH9W3b19lZGRoyZIlNR4flbsAAAAAAACAl3Id5H61h8rw4cN15513ut12oFW7RlJSku2HW/kM+9jYWHtfdS699FI7T5Sp7F24cKGtyF2xYoXGjRtXtt6Kwa5Ren1P662McBcAAAAAAACAowXtYwuG++67T88888xeWzLsL9OTt5Sp0K1fv75OPfVUrVmzRi1bttR/hXAXAAAAAAAAgFcZNmyYrrzyyj0u06JFC9szd9u2bW63FxYWaufOndX2063KCSecYP9dvXq1DXfNY2fNmuW2THJysv13X9ZLuAsAAAAAAADAqyQkJNjL3nTr1k1paWmaM2eOjj32WHvblClTVFxcXBbY1sT8+fPtv6aCt3S9TzzxhA2OS9s+TJo0SZGRkerQoUON18uEagAAAAAAAICXKi52HRaXg6V9+/bq16+frr32Wltp+9dff+mWW27RJZdcYvvpGps3b1a7du3KKnFN64WRI0faQHj9+vUaP368Bg8erJ49e6pz5852mdNPP92GuFdccYUWLFigiRMn6sEHH9TNN9+8T+0lCHcBAAAAAAAAoBqffvqpDW9Nz9wzzzxTPXr00DvvvFN2f0FBgZ0sLTs7214PDAzUr7/+agNc8zjTAuKCCy7Q999/X/YYPz8//fDDD/ZfU8V7+eWX2wD4scce076gLQMAAAAAAAAAVCM2NlafffZZdXerWbNmcrnKq4cbN26sqVOnam+aNm2qn376SQeCyl0AAAAAAAAAcCAqdwEAAAAAAAAvVaHgFA5E5S4AAAAAAAAAOBDhLgAAAAAAAAA4EOEuAAAAAAAAADgQPXcBAAAAAAAAL+Uqpumuk1G5CwAAAAAAAAAORLgLAAAAAAAAAA5EuAsAAAAAAAAADkTPXQAAAAAAAMBLFbvouetkVO4CAAAAAAAAgAMR7gIAAAAAAACAAxHuAgAAAAAAAIAD0XMXAAAAAAAA8FKuYnruOhmVuwAAAAAAAADgQIS7AAAAAAAAAOBAhLsAAAAAAAAA4ED03AUAAAAAAAC8FD13nY3KXQAAAAAAAABwIMJdAAAAAAAAAHAgwl0AAAAAAAAAcCB67gIAAAAAAABeipa7zkblLgAAAAAAAAA4EOEuAAAAAAAAADgQ4S4AAAAAAAAAOBA9dwEAAAAAAAAv5aLprqNRuQsAAAAAAAAADkS4CwAAAAAAAAAORLgLAAAAAAAAAA5Ez10AAAAAAADAS7lc9Nx1Mip3AQAAAAAAAMCBCHcBAAAAAAAAwIFoywAAAAAAAAB4qeJi2jI4GZW7AAAAAAAAAOBAhLsAAAAAAAAA4ECEuwAAAAAAAADgQPTcBQAAAAAAALyUy0XPXSejchcAAAAAAAAAHIhwFwAAAAAAAAAciHAXAAAAAAAAAByInrsAAAAAAACAl3IV03PXyajcBQAAAAAAAAAHItwFAAAAAAAAAAci3AUAAAAAAAAAB/JxuVw01gAAAAAAAAC80NBHt+lw8P6IOvJGTKgG/Gvz7Rd7egjwoIYvf6H115zr6WHAQ5q9+53OHLrI08OAB/30fif1HTLf08OAB00cfZSWDzzd08OAh7T76hedd9NKTw8DHvTtG234LODlnwN+DGjr6WHAg/oXrPD0EID9RlsGAAAAAAAAAHAgwl0AAAAAAAAAcCDaMgAAAAAAAABeqpjpuByNyl0AAAAAAAAAcCDCXQAAAAAAAABwIMJdAAAAAAAAAHAgeu4CAAAAAAAAXspVTM9dJ6NyFwAAAAAAAAAciHAXAAAAAAAAAByIcBcAAAAAAAAAHIieuwAAAAAAAICXcrnouetkVO4CAAAAAAAAgAMR7gIAAAAAAACAAxHuAgAAAAAAAIAD0XMXAAAAAAAA8FLFxfTcdTIqdwEAAAAAAADAgQh3AQAAAAAAAMCBCHcBAAAAAAAAwIHouQsAAAAAAAB4KRc9dx2Nyl0AAAAAAAAAcCDCXQAAAAAAAABwIMJdAAAAAAAAAHAgeu4CAAAAAAAAXsrloueuk1G5CwAAAAAAAAAORLgLAAAAAAAAAA5EuAsAAAAAAAAADkTPXQAAAAAAAMBLuYqLPT0EHAAqdwEAAAAAAADAgQh3AQAAAAAAAMCBCHcBAAAAAAAAwIHouQsAAAAAAAB4qeJil6eHgANA5S4AAAAAAAAAOBDhLgAAAAAAAAA4EOEuAAAAAAAAADgQPXcBAAAAAAAAL+Vy0XPXyajcBQAAAAAAAAAHItwFAAAAAAVD3t8AAIgsSURBVAAAAAeiLQMAAAAAAADgpVzFtGVwMip3AQAAAAAAAMCBCHcBAAAAAAAAwIEIdwEAAAAAAADAgei5CwAAAAAAAHgpeu46G5W7AAAAAAAAAOBAhLsAAAAAAAAA4ECEuwAAAAAAAADgQPTcBQAAAAAAALxUsavY00PAAaByFwAAAAAAAAAciHAXAAAAAAAAAByIcBcAAAAAAAAAHIieuwAAAAAAAICXchW7PD0EHAAqdwEAAAAAAADAgQh3AQAAAAAAAMCBCHcBAAAAAAAAwIHouQsAAAAAAAB4KXruOhuVuwAAAAAAAADgQIS7qDWuvPJKnXfeeWXXTznlFN1xxx0eHRMAAAAAAABQW9GWwaEh6OjRo+3PAQEBatKkiQYPHqz7779f/v6Hzy4dN26c3b5SzZo1s2Evge/ehfU4XeG9z5ZfZLQKNm9Q2tgPVLBxTZXLxt/ysIJad9zt9twlc7XjnWckXz9F9r9YwR2Oll9cHblys5W3YrHSv/9MxRmph2BrsD8iep2pqL7nyS8qRvmJ67Xj83eUv25VlcvWu/txBbfttNvt2Qv/0bZXRpZdD6jfSDEXDFFwm46Sn58KtiRq25tPq2hnykHdFuy/y8+ro349YxUW6qelq7P1+kebtWVbfrXLf/BsW9WND9zt9h+m7NAbn2yxP98yuIGO7hCu2OgA5eYV2/V+8FWSNiXlHdRtwb4bPKCe+p0Sp3Cz/1dl6ZXRidqSXP3+Hz2qg+ol7L7/x/+6Xa9/vNn+/Ox9rXRk+3C3+3+ckqJXRm86CFuA/RXd92zFnTNQftGxytuwVsnvv67c1SuqXT7mzAGK7nuWAuLrqCgjQ5kz/tT2z96Tq6DA3h/SvpNdX1CL1gqIjdOmZx/RrtnTD+EWYX8MOitOfU6MUliIr5avzdFbn2/T1u0l+7Qq74xsrjpx5Z+9S/00NU3vfLHN/hzg76OrLkhQj2Mj7M/zl2XprTHblJ5ZdFC3BfuHzwHeKbbHcWox7GpFHXOEghvU0T8X3KTk8ZP3/JieXdRh1H0K79BauYlbtfqpN7Xpo2/clml646VqcefVCqqXoIyFy7XkjpFKn73oIG8NgJo4fJJAL9OvXz998MEHysvL008//aSbb77ZBqHDhw/fp/UUFRXJx8dHvr61r4g7NjbW00NwpJCjuylqwGClffmu8tevUvgpZyr+xvuV/MT/VLwrY7fld7z/vHz8yv8U+IZFqM49zypn/gx73ScwUAGNmytz4lgVbNkgn5BwRZ8/RHHX3q3tz99/SLcNNRN6fA/FXjRUOz55U3lrVyrytLNV945HtPnBm1Scmb7b8tveeNr9NRAeoQYjXlb2P3+V3eafUE/17n1Ku6b9qrTvPlNxbo4CGjQpO/BH7XPhGfE657R4vfBuopJSCnTFgLoaOay5bnhgpQoKq+6pdfvI1fLz8Sm73rRRkJ68q4X+nF3+ulm9IUe/z0jTth0Figjz02Xn1tXjw5pp6D0rRKuu2uOiM+vo3D4JGvV/G5SUkq8h59fXk3e11LX3L1dBQdU76rZHV8jXt3z/N2sYrKfvbeW2/42ffk/RR+OSyq7n5RUfxC3BvorofrLqDLleye+8opzVyxXb/3w1fuBJrb39ahVlpO22fGSPXkq47Golvfm8clYstV/k1b/5LtN9T9tGv22X8Q0KVu6GtUr7baIa3T3CA1uFfTWgT4zOOiVaL3+UpOQdBbr0rHiNuLWhbn1sQ7XvAXc9s1EVDwma1A/SY7c30vS5mWW3Db0wQccdEabn3t2i7JxiXXtxHd13XQMNfz7xUGwW9gGfA7yXX1ioMhauUOKHY3Xc16/vdfmQZo10/Pi3tfGdMZo/+C7F9e6mTm8/rtyt25UyaZpdpv7AM9T+ueFafPMIpc1aoOa3DdEJP76n3zv2U/72nYdgq3CwuVz8B3ay2pfooUaCgoJUr149NW3aVDfeeKNOO+00jR8/3oa9d911lxo2bKiwsDCdcMIJ+v3338se9+GHHyo6Otou26FDB7uejRs32mW6dOliH2PuP/HEE7Vhw4ayx7355ptq2bKlAgMD1bZtW3388cdu4zEB8bvvvqsBAwYoNDRUrVu3tr+jYoh89dVXq3nz5goJCbHrePnll/e4jRXbMpifzXj+97//2d9lLllZWYqMjNTXX3/t9rhvv/3WbkdmZvkHUW8Sfkp/ZU2frOyZv6swebMNeV35+Qrt2qvK5V3ZWTbwK70Ete0sV0FeWbjrys3RjjeesNcLt21VwYZVthI4sElL+cXEHeKtQ01E9TlXmX/+ol1/TVbB1kQb8rry8xTR47Qqly/O2mUP+EsvIR2OsstnVQh3YwZcrpxFc5T69WjlJ65T4fYk5SyYVWVYjNrhvD7xGvP9Ns2Yn6n1m3L1/LuJiov2V7djIqt9TEZmkVIzCssuXY6M1JbkPC1akVW2zISpqVq8Mtse1K3ZmKuPvklWnbhA1ami0geec17fBH3+fZL+npehdYm5evadDYqLDlD3Y6KqfYypvEtNLyy7nHBUlN3/C5fvclsuL8/ltlx2LuFubRJ71gVKn/yz0n//RfmbNirpnZdVnJ+nqN59q1w+pG0H5axYooxpv6lge7KyF85R5l+/KbhV27JlsubPVsqYD7VrVvn7Amq3s3vH6MsJOzVrYZY2bM7Xy6OTFBvlrxOOdK+8ryhjV5HSMsovx3cK09Zt+Vq8KsfeHxrsq9O6R+n9sdu1aGWO1iTm6dWPk9S+ZYjaNAs+hFuHmuBzgPfaPvEPrRzxkpK/+7VGyze97hLlrNukZfc8o13L12rDG58qaexENb/9yrJlmt9xlRLf+1KbRo/TrmVrtOimESrKzlXjKy84iFsCoKYIdw8TJjDNz8/XLbfcor///ltjxozRwoULNXDgQFvlu2pV+enY2dnZeuaZZ2wYu2TJElsha3rdnnzyyfYx5vHXXXedDVCNb775RrfffruGDRumxYsX6/rrr9dVV12l3377zW0Mjz76qC666CK7jjPPPFOXXXaZdu4s+RavuLhYjRo10ldffaWlS5fq4Ycftm0kvvzyyxq3aDCPf+yxx7R161Z7MQHuJZdcYiuYKzLXL7zwQkVERMjr+PkpoHEL5a2scHqMy2WvBzZrXaNVhHXtpZy50224Vx3f4FC5iotVnJ39X4wa/yU/fwU2bancpQvKb3O5lLtsgYJalB+o70l4j9OUNevP8teAj49COh+nguQttgK48QujVf/+5xR61AkHaSNwoOolBNjTJecvLQ/lTIXVirXZat8ytEbr8PfzUa+u0fplWvXtV4ICfdSnR4y2bs9Xyk6quGsL01rBBLlzl7jv/+Vm/7cKq/H+7909RhP/2LHbfb26xejL147Q20+01VUD69vXAWoJf38Ft2itrIXzym9zuZS9cJ5C2rSv8iGmWtc8pjTMDahTT2FHd1HW3FmHatT4j9WNC7BB7sLl5Z/TzJcwK9fnqm2LmoWw/n7SyV0iNfnv8rO+WjYJsq0YKq53c3KBDflqul4cGnwOwL6I7nqUUqb87Xbb9knTFNP1KPuzT0CAoo7pqJTJFdrxuFxKmTJd0V2PPtTDBVAF2jIcBqXzkydP1sSJEzVo0CAbbJpK3AYNGtj7TRXvhAkT7O1PPvmkva2goEBvvPGGjjzySHvdBLDp6ek666yzbHWu0b59+QHAqFGjbJ/fm266yV6/8847NWPGDHt7r17l1aBmGTMGw/yuV155RbNmzbLhsmkZYcLfUqaC14TIJtw1gfDemADaz8/PBramYrnUNddco+7du9uwt379+tq2bZttU/Hrr9V/S2mqm82lIlPBfDjwDYuUj5/fbtWURaYit07Ja2JPApq0tKfap37+VvUL+Qco8pxLSwLgvJJKDtQefuElr4HKp96a6wH1Gu318YHNWyuwUTOljH6tfJ0RUfINDlHUGRco7dtPlTp2tEKOOEYJN92npFEPKm/lkoOyLdh/MZElPRNN1U1FaRmFiomq2Vu/qewxvVp//Wv3g7r+vWI1dGA9hQT7KXFrrh4YtU6FRZzKVVuYUMdIS3c/0E7LKCi7b2+6Hxtl9/8v09xPtfxtRqq2peRrR1qBmjcO0dUX1VejekEa+er6/3ALsL/8I0reAwrT3f/fmuuhDRtX+RhTsWv+zjcd+YI5hJePv79Sf/leO74Zc4hGjf9adJRf2d/8itIzihQTWbO/AabC1/TqnTyj/DOleWxBQbGyctyr9dMya75eHBp8DsC+CKobr7xk9zk0zPWAqAj5BgcpICZKvv7+ytvm/oVvXvIOhbVtcYhHC6AqvAs71A8//KDw8HAb1Jqq2EsvvdRWq5q2C23atHFb1gSZcXHlp8+b1gqdO3d2C05NMNu3b1/16dPHtngwgasJS41ly5bZSt6KTNuGym0VKq7TVNWalgkmbC31+uuv6/3337fhc05Ojq00Puqokm8D95dpJdGxY0c7wdx9992nTz75xLaq6NmzZ7WPeeqpp9yCZmPEiBG69oBGcngI69rb9tWtbvI1M7la7JWmVYaPbfeAw49p3ZC/ab375Gs+JSd5ZM+fqYxJJe1WTGuGoJbtFHFyP8LdWuCUrtG6dXD5FzgjXipvq7O/Tj8pRv8sytTONPcDQ+O3GWmat2SXYqP9dX7fBA2/sYnuenJNtT38cHCZStrbryz/8uahF9Ye8Dr79ozV7IUZu+3/n38vP7Azp/nuTCuwk6zVrxNoT9+G84R26Ky48y9R0v+9qtzVyxVQr6HqXnWjCi/YqR1jP/X08FADPY+P0I2D6pZdf/zNkgkQD4RpvzB3aZZS05kozQn4HADgQJlcCc5FuOtQpmLW9ME1Qa2p0vX399cXX3xhq1vnzJlj/63IBMEVWziUtlwoZSp7b7vtNlvla9bz4IMPatKkSeratWuNx2Sqcysyv6P0D4RpE2GqiJ9//nl169bNVuA+99xzmjlzpg6Uqd41wbEJd812mJYRlbevIjPpnKk+rly5m3LPYDldcVaGXEVF8o1w76loKnKKMnefRKUin8AghRzTXRk/f1l9sHvVHfKPTVDKa49RtVtLFe0qeQ34RUa73W6uF1Wq5KrqNRB2/ElK/e6z3ddZWKiCLe6TpZh+vkGtO/yHo8f+mjk/w55qWcqcNmuYSirTE7VUdKS/1m7M3ev6zGzpR3UI1xOvVX1waE7tzM7JtzNuL1+zUV++1kHdj43U1Jn0YPaEGfPStWJNeT/EgICSL2SiowK0023/B2jNxpwa7f+jO0Zo5Cvr9rrs8jUlr7sGdYIId2uBwsyS9wD/qBi32831wrSqJ7yJv2SI0v+YrPQpE+z1vI3r7QRq9a6/XTvGfWZPvUXtNmvhLttyofJ7gPmbn5pRHs5GRfpp3abq226VSoj1V+d2oXrmnS1ut5sqUPP3xVT0VqzejY7w261CFIcWnwNwIEyVrqnerchcL0jPVHFunvJTUlVcWKigOu7zrQTVjVNeknvFLwDPoOeuQ5nK2FatWqlJkyY22DWOPvpoO3GZqZY191W8VGxlUB3zeBN8Tp8+XUcccYQ+++yzshYNf/3lPoGGuW4mZKsps7xpn2BaO5jfY8a0Zk011aHVMEG22b7KLr/8cjvZmmkDYfr5DhkyZI/rMUGuqSqueDlc2jKoqEgFiWsV1KZT+W0+Pgpqc4Ty11eoxKxCyFFd7amYObP/rD7YTaivlNdHqjjbfXId1CJFhcrfsEbB7Tu7vQaC23VW3toVe3xo2HEn2p5aWTOm7rbOvPWrbTVXRf51G6pwR3l1PjwnJ7fYBmull41b8mxF5ZEdKnyxF+yrti1CtezfMG5PTP+89IxCzVpYg4kpfdwPJOGZ/W8OsEsvGzbn2rYJR1fY/2YipHZm/68uD4Grc/pJcfbU3ZkLynttVqdl0xD7785KLSDgIYWFyl27SmGdKpwZ5eOj0E5HKWflsiofYoJcVarWcRX/+3lrD1+Wo/bIzXMpaXtB2SVxa779Yqdz21C39wAz6dmKtXsP9k7tFmUnWPxnsfvfizUb82xlZsX1NqgTYIPAmqwXBw+fA3Ag0mbMV1xv96Ku+FO7K3XGfPuzq6BA6XOXKL53t/IFfHwU16ub0mZU6PEOwGOo3D2MmHYMZhKzwYMH2wpZE6Ju377d9uQ1LRP69+9f5ePWrVund955R+ecc46tAl6xYoWdgM2sx7j77rttmwazPtOy4fvvv7cTnO2pr21lrVu31kcfffT/7d0JuI1l98fxu8GQZKZMUZlnSoSKKPMckmTIrBRCpopkiFIqQ4aEokxJmZOxqMwUQilj5pmU53/91vt/9rvPQa+Ktmef7+e6XMfZZx/trme673Wvey2n2sCqtzt27Fj3zTff2N8vVebMmd2iRYusiZqCsalS/Wd1MXny5K5GjRr2OR966CFrvBaXHV/wmUter5WVVvjt560u8f0VLCPz5PIF9vPk9Vq7P44cdEc/HR/j9xKpkdq6b88P3Cqw27iti5fhNnfgnVecu/baUGawvfcCAXdE1pG501zqxk+7M9u3WHmFJGUqu2sSJHTHlv7nmk3V+Bn3++ED7vCUsec1Uju5ark7d+L8gfzR2VNd6ubPutObN7jTm9a5G3IXconyF3Z7+nf91/6/8Nd8PHe/e6RSGutyvXffb65+9ZvdgcO/u69W/jdg1/vZ29yXK4+6T+f/d6u9YjkPFk/u5n15KHa8xxq03Fc4mVu54ZhN/FMlj+dqVUjtfjt7zn1zKRNA/Gs+nr3P1a1ys9u594zbs+8316BGWgv4frnyv1lVfTveYd9/Mm9/jOP/0L0p3LwlB887/iq9UKpocvf12qPu2PE/3G0ZE7rmj6Z3azcedz/+QmDnanHw08kubesO7tTWH6zMQvKKNSyAe+SL2fbztE92cL8fPOD2fTDKvj/+7TKXvFINd/rHrf9fliGdS/1IA3d8xbJQ0PeahAld/Fv+u+VbTdcSZL7d/XH8mPt9/74I/Z/iz0yff8jVKp/CFnzU8OzRyqks4Lt8zX/HeT3bZHDL1hx3MxYejnEPeKBoEvfFsqPn3QPUlG3el0dco5qp3bGTf7hTp865pnXSuI3bTsXIHMbVgXFA3HXdjYncjVluDX2f6LYMLkn+HO63g0fc6V92u+y92rmE6W92axp1sp9vf2eCy9SqnsvRp4P7ZfRkl6pUUZe2Vnn3TZXmoX/jx9ffdflH9XOHV6x3R75Z6zK3aeCuv/EG98t7UyLy/wggJoK7UUZlCXr16uXat2/vdu7caQFQlVZQs7SLSZQokdu4caPVrT1w4IDV2m3durVr3vw/N/Nq1apZfV01UHv66actIKv/TsmSJS/5c+nfWrVqlatTp46VTFDjNWXxzpw585L/jZ49e9q/o6ZvqiOsZnK+J554wjKNGzdu7OK6U6u+ctcmTuJuqlDbtuKf3fGT2z+0T6jJ2nXJUzrPizlSuz5NWpfgjpxu/+Be5/171yVL4W7IW9j+fnOnV2L8bN+bPdxvW767ov8/+OtOfrPEHUycxCWv+qi7Lklyq4+79/Ue7tzR/5wD16dMpbSs87JwE2bL7fa89vyF/81Vy9yBsUNc0goPuxR1m7rf9+x0vw7p685suXAmGCJv0sz9LmGCa91TDdJbQ5QNP5x0z7/2Y4x6eArWJb0pZhkfbcNMkyq+m7v4/DIev531XO5sN7qqD6Z0iW+8zrI712866dr33mqTPFw9Pprxqx3/pxtm/P/jf8J1HbDNnT0bfvwTuCSJYw4FVY7h5lTx3exF52/h//13z35evWxqlzD+tW7fwbNuyTeH3fhP9v4r/0+4NMe+XOiuS5LUpa7zuLsuWXJ35qdt7peXu7o/jvwngBcvVZoYpRb2T37fxlSp6zZw16dI5f44esQCvvvGvxt6zw23Z3O39hgQ+v7mhi3s65EFc9zut//7Oq4eU+cesntAq0dvdjcmutZ9v/WU6/nWzhjPAAXqkiSO+QzInyORZeJ+/tWFt9ePmrTPTp9OTdNZpuaq70+4YRPYxXM1YhwQdyW9M4+75/P/JnHkGtDFvv4yZopb+0RnlyBtandDxv/015FTP+2wQG6uVzu7zE897k7v2OPWNe/m9s9dEnrP7okzXfzUKVy2F9q4BLekdkfXfO++rtTE/RaryRqCyztHGaYgu8YLj5ABAaVM4LZt27pdu3ZZ+Ya/Y+fTdS7750JwpH/jQ/dTk6qR/hiIkMwjprkKjddF+mMggmaMyuvKNvjP9kPETbPfK+A21noo0h8DEZJj4hxXrdXmSH8MRNDHg7MxFojj44DP4mWP9MdABFU8++cl7KJdpabRkbT16fC42ROGzF0E2smTJ93u3btd3759Lav37wZ2AQAAAAAAgKChoRoC7ZVXXnE5cuSwhnFqBgcAAAAAAADEFWTuItBefPFF+wMAAAAAAIC/LnZfHgQLmbsAAAAAAAAAEEAEdwEAAAAAAAAggAjuAgAAAAAAAEAAUXMXAAAAAAAAiKO8c16kPwL+ATJ3AQAAAAAAACCACO4CAAAAAAAAQAAR3AUAAAAAAACAAKLmLgAAAAAAABBHUXM32MjcBQAAAAAAAIAAIrgLAAAAAAAAAAFEcBcAAAAAAAAAAojgLgAAAAAAABBHnfPORcWfK+ngwYOuXr16LkmSJC5ZsmTuiSeecMePH7/o+3/66Sd3zTXXXPDPxIkTQ++70M8nTJjwlz4bDdUAAAAAAAAA4CIU2N29e7ebO3euO3v2rGvUqJFr1qyZ++CDDy74/owZM9r7w73zzjuuf//+rnz58jFef/fdd125cuVC3yt4/FcQ3AUAAAAAAAAQaGfOnLE/4RIkSGB//onvv//ezZo1y33zzTfurrvustfefPNNV6FCBTdgwACXLl26837nuuuuc7fcckuM16ZOnepq167tEidOHON1BXNjv/evoCwDAAAAAAAAgEDr06ePS5o0aYw/eu2f+uqrrywA6wd2pUyZMu7aa691y5cvv6R/Y8WKFW716tVWziG21q1bu1SpUrm7777bjRo1ynme95c+H5m7AAAAAAAAQBzlnftrwcSrVefOnV27du1ivPZPs3Zlz549Lk2aNDFeu/76612KFCnsZ5di5MiRLmfOnK5YsWIxXu/Zs6d74IEHXKJEidycOXNcq1atrJZvmzZtLvnzEdwFAAAAAAAAEGgJ/mIJhueee87169fvf5Zk+KdOnTpltXm7d+9+3s/CXytYsKA7ceKE1eUluAsAAAAAAAAAF9G+fXvXsGFD92duv/12q4f766+/xnj9999/dwcPHrykWrmTJk1yJ0+edI8//vj/fG+RIkXcSy+9ZLWDLzVQTXAXAAAAAAAAiKO8c+dcXJQ6dWr787/cc8897vDhw1Y3984777TX5s+f786dO2fB2EspyVClSpVL+m+pLm/y5Mn/UgYywV0AAAAAAAAAuADVyi1Xrpxr2rSpGzp0qDt79qx78skn3SOPPOLSpUtn79m5c6crXbq0GzNmjDVG823ZssUtWrTIzZgx47x/d/r06W7v3r2uaNGiLmHChG7u3Lmud+/e7tlnn3V/BcFdAAAAAAAAALiI999/3wK6CuBee+21rmbNmm7QoEGhnyvgu2nTJiu/EG7UqFEuQ4YM7qGHHjrv34wXL557++23Xdu2bZ3neS5LlizutddesyDyX0FwFwAAAAAAAAAuIkWKFNYU7WIyZ85sAdrYlImrPxeibGD9+acI7gIAAAAAAABxlHfu/KAkguPaSH8AAAAAAAAAAMBfR3AXAAAAAAAAAAKI4C4AAAAAAAAABBA1dwEAAAAAAIA4yvPORfoj4B8gcxcAAAAAAAAAAojgLgAAAAAAAAAEEMFdAAAAAAAAAAggau4CAAAAAAAAcdS5c16kPwL+ATJ3AQAAAAAAACCACO4CAAAAAAAAQAAR3AUAAAAAAACAAKLmLgAAAAAAABBHeefORfoj4B8gcxcAAAAAAAAAAojgLgAAAAAAAAAEEMFdAAAAAAAAAAggau4CAAAAAAAAcZR3zov0R8A/QOYuAAAAAAAAAAQQwV0AAAAAAAAACCCCuwAAAAAAAAAQQNTcBQAAAAAAAOIozzsX6Y+Af4DMXQAAAAAAAAAIIIK7AAAAAAAAABBABHcBAAAAAAAAIICouQsAAAAAAADEUd45L9IfAf8AmbsAAAAAAAAAEEAEdwEAAAAAAAAggAjuAgAAAAAAAEAAUXMXAAAAAAAAiKO8c+ci/RHwD5C5CwAAAAAAAAABRHAXAAAAAAAAAAKI4C4AAAAAAAAABNA1nud5kf4QACLrzJkzrk+fPq5z584uQYIEkf44+Jdx/ME5ELdx/ME5ELdx/ME5AM4BINgI7gJwR48edUmTJnVHjhxxSZIkifTHwb+M4w/OgbiN4w/OgbiN4w/OAXAOAMFGWQYAAAAAAAAACCCCuwAAAAAAAAAQQAR3AQAAAAAAACCACO4CsKL5L7zwAsXz4yiOPzgH4jaOPzgH4jaOPzgHwDkABBsN1QAAAAAAAAAggMjcBQAAAAAAAIAAIrgLAAAAAAAAAAFEcBcAAAAAAAAAAojgLgAAAAAAAAAEEMFdAAAAAAAAAAgggrsAAAAAAAAAEEAEd4E4wPO8SH8ERMC5c+ci/REARPi+H37/51kAAHELY0EAiBsI7gJxYCB3zTXXROyzIHKuvfY/t/iOHTu6adOmEdiJYwjuxe1ngH/f/+2339zZs2ft73qNcyDuIKgDH9d93OWPBVesWGFfORfiltjHm+MPRC+Cu0AUTub8gdyYMWPcs88+61q3bu2mT58e6Y+GCEzo586d69566y2XKlUqgvxxNLh35MgRd/jwYfs750Dcega88cYbrnbt2q5ChQquadOm7vfff+cciEP882Dq1Klu69atkf44+BexyI9wy5Ytc4ULF3YrV67kXIhj/OPdu3dvN3v2bI4/EMUI7gJRnK3ZrVs3d+DAARc/fnxXtWpVm+iTyRN3zoFRo0a5devWuT59+rjixYtH+mPhX6KsDP8c6Nu3r6tSpYq77777XOnSpd2aNWtCWZyITv6x79y5s137999/v2vWrJkbPXq0q1atmjtx4kSkPyKusPDn/C+//OJq1qxp94Iff/wxop8L//4Cz6RJk9zLL7/s+vXr5xYvXhzpj4YIyZ07tytXrpybMWOGjRGYC8Qt2sGjzG3NC06fPh3pjwPgCiG4C0QhrcxOmDDBffTRR+7dd991ZcuWtdeTJUsWGvAjuv3888/u9ddft8ztgwcP2mvK2kP087Myunfv7gYOHOieeOIJN378eLd582bL3ty/f3+kPyKugPDJ+oYNG2y3ho57u3btXOLEid0NN9zgKleu7G688cbQ+9ieGd2LO88//7wbOXKky5gxowX3teC7ffv2SH9E/IuL/O3bt3dff/21W79+vS30aFyI6HahwO1NN93k8ufP7957773QPYL7f9yhJB/NBVetWhUaAxLgB6IPUR4gCu3atcsVKlTIFS1a1E2ePNnVqlXLDR061DVo0MC2aGuQj+iWPn16C+zde++9Vp5Dx/366693f/zxR6Q/Gv4FO3bscLNmzbIsDV33O3fudEePHrVAb9q0aUPvY3IXfI0bN7Zgribr/mRNkzdl55QqVcp98sknVpqhf//+rnnz5nYefPDBB/Y+tmdGH/+Y6nirJI8y9j/88ENb8FV5BgX8CPBGvylTprj333/fgrmqua/SLHLy5MlIfzT8S8H9TZs22djP16NHD/vZSy+9ZN9z/49OFxvXaQePgvxa9BOSfYDow1UNRKEECRLY1lsF9Ro1amSTPD3U5fPPP7ftmfv27Yv0x8RlcqHV9+uuu86ydHr27GkZ2/q7Bvl6nQBv9FON3b1797qKFSu6mTNn2rZsbctVcO/YsWNu8ODB9j4md8GmsjsK7JYpU8Yys/3JWpYsWVyGDBns+n/sscfcq6++asfen/CPGzfOrV69OsKfHle6xuajjz5qC3xa6NU9YN68eRbsV1b/tm3bIv0RcQUbaOr4KrBfpEgRC/RqDDhs2DDXsGFDW+DR/QLRG9TTMS9ZsqSVZdJC76+//mrZm7oPKHtT2/QR3f0WNM6bOHGi2717d+jnLVu2dBs3brTdfcICPxBdCO4CAXaxLTWa2Cu4o8l8165dXYsWLUIZG8rkS5QokTXYQnTV1hs7dqxtwVRmloL4ytQtUaKEZfAq4P/AAw/YpE4BXrZjRY/wY6nAreTMmdNlypTJ7gF16tRxr732Wug+oCxeBffmz58fsc+MyyNFihQ2iS9YsKBd637ARte4SjGo1qYmc/7inrJ5X3zxRSvRkC9fvgh/elyp+4HqaiuYc+rUqdAEXsGcYsWKuQ4dOtj1r+Y6WhxA8GnB1g/o+OWXdA/Q2EDBHe3e0CK/yvKIFvwU6A3P6kT0BPV07deoUcO98847Voqhbt26tmtnyJAhrnr16u6zzz6z2ruILrrv+/MB/V0l+nTd33PPPZbss2XLFle/fn2rva5dHMICPxBdrvFYsgECSZeu/1BWLT2tzCqAp/qKokytAQMGuHr16ln2ngZ+r7zyituzZ48V1VfgL/zfQLB16tTJ6muqG7JqamorpibwDz/8sE38lixZ4p577jlrrqMAkAL8iK7g/qBBg6y+so55jhw57Hir5raaKWpRxw/u6ee69lWTlW15waUgju7jsnbtWgvgKlinSXvWrFnd8uXLLaijIL8mdyrHoe352rWhjunx4sWLcf4gmC52DBW802KfSjOp1qL/vH/zzTfdl19+aZN71WTv1atXRD43Lv/xf/vtt23xTtvuFcDTeFBjQzVWbNOmTWgBUAt+2bNnt4VfRNc5oGOv0mta2NWCvmj8p2te8wKVbFu4cKH9TOV5tE2feUDwKZB76NAh98gjj1ggX4kcWthRlq7mBmqsqPGCgv4aAyxdutTKtdx6662R/ugALicFdwEEy7lz50J/79y5s3fTTTd5pUqV8m644Qb7unPnTvtZr169vJIlS3rXXnutV6xYMa9SpUreb7/9Zj/7/fffI/b5cXmNGDHCu/XWW72vv/7avv/www+9a665xv7oZ/7xnjVrltekSROOfRTq0KGDlypVKm/cuHHe9u3b7bVt27Z5lStX9goWLOg99thjdq+47777vLx584buA3/88UeEPzn+qW7dunllypTx7rnnHrvm06ZN63333Xf2s8WLF3stW7b0smTJ4pUtW9Zr3Lixd/bsWfuZ/xXBFX79zpkzxxs/fry3ceNG79SpU97hw4e9Bg0aeFmzZvU+++wze8+RI0dsHDBp0iRv2LBhXrJkyew+ET6mQDCPf9u2be36z5YtW+j+3r59ey9evHjekCFDvG+//db+6D6gZ4J//XPso4ee8SlTpvSmTZvm7dq167yfHzt2zBswYIBXtWpVL0GCBN6GDRvsdc6BYNOYXtd1rly5bMync2DVqlUx3vP99997U6ZM8XLmzGnzBd0r/OcC40AgehDcBQJMg7fy5cvbQ/zMmTPejz/+6GXOnNkrWrSot2PHDnvP8ePHvXXr1nn79u0LDeCY1EePEydOeN27d/eGDh1q30+fPt1LkiSJ9/rrr9vETgM4BXtjD+AI8EaPTz75xAbry5YtC73mX+tbtmyxc6FEiRJe7dq1vWeffZbgXhTRdZ84cWJv6dKl3s8//+zNnz/fFvRSp05tkzlRoEf3ifBrnmMffOEBGd3rb7nlFi9FihQ2eX/ppZfsmCtw27RpU1vgzZ07t3fbbbfZV50LkydP9rJnz+4dOnQoov8f+HvCr+d27drZ4p6C9gUKFLCxoK9Zs2b22nXXXWcLQKVLl2aRPwotX77cAvsLFiyI8bo/7vOPtX/f0CJPrVq1OAcCrHfv3t6mTZtC3+t+rnv9K6+8Enot9vHVc2HevHl2/HVf8O8FAKIDe/GAgNL2qkqVKtnf1ThHjRIyZ85sW23USEnd0VVXSVv08+TJYzV2tfVK27f8rbwIftMUlVdQwyQ1VFIDFW2z1ba8p59+2pUvX97eo21aaqITvnVX9fgQHXSda8t97ty5Q6/558cdd9xh58LixYttS77qr+n6V6kO7gPBopp5sStp/fDDD65y5cpWSzVjxoyuVKlSVmfxtttuc+XKlXNbt2618guqsetf8/o3OPbRU19T262//vpr9/HHH9sWXI0LdL9XM700adLY+aBGak2aNHHdunWzRno6F3RPuOWWW9iSHTA6buJfz6qlPmLECDvGqruta171NsPLc6gEh7biq1TTnDlz7J6gsi6MA6LH8ePHrZGyxgLhNO5TvW1//OfX6NeYUSU6KMsTTCq7smbNGhvjicowaA6oe8CECROsFMOZM2diNFHWV80Z1GixS5cudg9QCQ8A0YM7OhBQqqGopgnffPNNqCmGBm3p0qWz+lr6mYJ7qr8WjoFcdEzoNYjXgF2TuGzZstkAb9OmTdZESR3SJUmSJFaHUxO6ChUqRPjT43LzB+yqo63zQMfef13Xuc4XTQA2bNhw3u8yqQ8W1cZTU7zYwV1Nzr799tsYr6nerhZ81A1bjfX0NTyARzAvuL777rsYz3HVVlfwLm/evK5IkSIuderUVltfgX01TFSAV3WYFfR/5plnXOPGje18aN26tdXjVp3upEmTRvj/CpdKdXMVtPHvA6qxrka5CxYssMZZuq+ryaLGB+EUxC9evLi7/fbbQ88GFniCK/w54P9dTZR1LmghTzQ+9Cmwrxr74c/+7du32+KggsIIHvVSURNlHU8dW9XbnTVrlh1rXe/9+vWzRR31WfCPefizX01Ydf/Q8wBA9CDKAwSAv9IeTplaytTRwE7drxXg1aBd3yvAq4mdJnx6yCO6GmYoa1vZuMq8aNiwoWVq++9Ro6RVq1ZZExVN7DXJU7BXEzm/izai4z7gD9iVualjrkBN+OvK5Bg5cqRldyDY1BRP17buAdqd4Qf21RxFk/m+ffvaJM6nzF3dGzp27OjSp08fwU+Oy6Vt27Zu8ODBoXuB7udqmDNlypTzrnHd+7W4qyxPZWgpQ08UyFEgUM+HRYsWuXz58kXk/wV/z5NPPuneeOMNC9IoMKdArjL6FagR7dDSPUIZ3KLxoJoqKns7HIv80bHIH/53PQu0i0/N8kS7+UQBXzXOU8a+T9e/gsHazaOGaggONcrt0aOH/V0Z+Br7PfXUU+6FF16wMYJo54bOBe3U0jHev3+/K1mypC36+vQeBYS1sxNA9LhGtRki/SEAXFpQTw9uPaRz5MhhWXoa2C9btsyyMrXNRlvzlIUTu3u2AgFk6gWTsi/8Qbp07tzZAnbqfq3tVZq4K7ijDG5RdpZ+rkxe/VxZfRoA+p3SEUzhx0+D9Z9++smyMgsXLmzbMJ9//nkL8GnbdfXq1S3Qp8G+JnE6B7j+o4OeAXfddZcF73SsNXHv1KmTTdzvvfde165dO3tNmZmZMmVyb731lv0ez4Dg++KLL2zLre7nO3bssMm7rnMF8GfMmGG7NDTJ9zP3/ICwFviU3evfPxTg1f2EoE5wnwHajaNrW4GeatWq2Wv+4q0W9XVP0OKOxoYK9G7evJlM3Sg7B3T8tXijsZ4y8x988EFbsGnUqJHdA7p3727XuhaAtINPQcDwc+DUqVMx7hW4+mkXhp7tyrZV6T2N92XUqFF2j1egVj8vVKiQzQP1nnXr1tm9IVmyZO6rr74KzSdmzpxp5452/gGIIpEu+gvg0hqmdOzY0cuYMaOXJk0aa5xSs2ZNa6AgX331lXVHrVOnDs1Roog6nfvdbEWNE9QAwW+YoUZaSZMm9d5+++0Yv6emSvo9v5ECzZOi5z7QoUMHa5alpklqnqImaT/99JP9bPDgwV7y5Mm9tGnTWmONUqVK0Tgn4MKbIPp/1/UeP358a5olR48e9Tp16uTlz5/fmiZlzZrVy5s3L41SokTsTvbjxo3zihUr5i1ZssS+P3nypNe4cWOvSJEi3quvvuqdOnXqgr9PR/Tgin3sNPa77777vIoVK3off/xxjJ9pbKiGSlWqVLFnBM+A6LsP9OrVy0uWLJmNEfPkyWON8kaPHh1qolqhQgUbAxQsWNCapnEORA81Tm3ZsqXd7/v37x96/d133/UKFSpkz4IVK1aEzhnNEyZOnBg69mq+DSB6EdwFAjCYHzJkiHVC/vzzz71ff/3VGzNmjFe5cmUb3K9cuTI02L/mmmu8rl27RvBT43KpV6+edTYPpyC+Avsyffp0L3HixHZu+AGe4cOH20Q/HIP56LF27VqbuGvgruP63nvvWQC3fPny3tatW0MD/2+++cZbvXp16B5CcD/4z4AJEyZ4kydP9k6fPm3fDxs2zLpi9+zZ077X5F0Le1OmTPHmzp3Lwk4UiX0P172/ZMmSNgZYunTpeQHegQMHnvcciB0gRjDvAzNnzvT2799vf9c9/oEHHvDKlSvnTZs2LfSeunXr2lgwV65coaAe94Hooed7mzZtvIULF9r33333ndesWTNb+NcY0Ldz507vyJEjoWufcyD4/GOpcV6LFi3+NMDrzw3DMR8Aoh/BXeAqM2PGjNDfNRjTwL5+/fpeq1atYrxvzpw5Ftx97rnnQq9pkMfDO/j27dtnk3cF8WXkyJHesWPHvF27dllGhrI2FNhVgMengJ8Cf19//XUEPzmulPHjx3v333+/BXTCM/MU9FOAV+fFxo0bz/s9svWiY9dG+vTpvVGjRtk9wKeFHQV4dT+4UPCOZ0HwhV+/ut/7uzSUrfnQQw/ZdR8e4G3SpIktCuq+gOALv667dOni3XHHHRa897Pv/ABv2bJlvalTp9pr+qqMTj+YR1AvemjxTjs0tDNDAT7f999/7zVv3twCe0OHDj3v9xgHRMd9IPx+oB1bOuYXCvAWLlzYq169umVxA4hbCO4CVxFtq9JWq7feeivG6w0bNrQHdewBmrbiaiLnZ3P5GMwHX40aNezYavCmLJzt27d7J06csAm9vu/WrVvovZrUK3tT2zAZxEenl19+2Uox3HrrreeVXvnwww+9Bx980Lv77ru9HTt2ROwz4vLTNntl6ytrP5yfkadnRbx48bzOnTuTnRllwu/l7du3t/t+jhw5QkF7BXh13YcHePWM6N27N4H9KNO9e3fbvfXll196Bw8etNf8633NmjVe6dKlbQzgB3jJ1oxOX3zxhVepUiVb3P/ggw9i/EwBXm3Xz5AhQ4xMbkTPc+D48eN2bfvP/23btl0wwKtFwEaNGjEfAOIgGqoBVxE1vVBXYzVHadWqlXVGlt69e1vzhKlTp7oiRYqE3q/GSuqcrML4aqSG4Atvhpc6dWprhqNu6OXKlbPX1FDvnnvucSlTpnT333+/NdOaNm2ava5mS2q2E7uhHoLlYs3vhg4d6gYNGmQNtV555RV3yy23hH42evRoa5iirtgc++DyG5/pHFAzRTVEKViwoHvxxRfdtm3b3Nq1a+1YqymKjnX69Ondq6++6j7++GNrpkPTxOgQ3gBPTfLGjBljx1lNc6ZPn273f9G9f8iQIXY+6H3qiH6hfwPB9csvv9h9QE0zy5cv7/bu3WsNlT744AP3wAMPuMqVK1vTpPr161tjLd0XEHwXG8dpnKfngZprdejQIdRQT9avX2/zAd0LuPaj6xzQdb1w4UJ38OBBa57XuHFje/7/+OOPrl+/fjY2ePjhh+3Yh48jmQ8AcQvBXeAqown822+/7T777DML8LZp08Ze16D9p59+csOHD3c5cuSwTtc1atSwrwr6MqmPLnPnzrVu15rEnz171gbsmTNntp9pcqeJngZzCuqr462C/OqErK64dMUOrvCB+O7du+1YKnDjL95ogD958mTrcNynTx938803/+m/geA4evSoS5Ikif39+++/dzlz5nSPPvqoO336tN3/9UyQG2+80e3atcslSJDAzZ492776E7mLLQwgGBSky5s3b+h7dT5XYFddznVu5M6d261Zs8bdfvvtofd88skn7oUXXnClS5d2AwYM4ByIMnoO6Jzo2bOnLe5rgU/ngI6zzpePPvrIgjo//PCDjQW49wdf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QWUVJk2aZJn5CuqqDJMaqi1fvtz179/fJUqUyEq06HcVHCawG3dq8Or461zIkydPpD8OAADAVY/MXQDAFaWt1x9//LHr0KGDK1OmjAV0/lcmbnhdztOnT7uECRP+q58ZwOWn2roqv6DmWaVKlbIg7v33329lWBo1ahR6nzJ0Dx065FKlSmX3ATJ24zbqrAMAAPw5RkoAgCtK2XfVqlVzr7zyips3b55r0KDBn2bwhgd2R48e7UaMGOF+++23f/1zA7i8FKBTkFaB3cmTJ9tiz+uvv26BXTVPmzp1qgV19Z7UqVPbfYCMXRDYBQAA+HOMlgAAl52/KcT/qgBvlSpV/meANzyw+84777jGjRu7TJkyWd1NAMFxoY1hCtLt2bPHvfjii1aLW/eDFi1a2M/Wr1/vhg0b5rZu3Xre7wAAAAC4OEbMAIDLSpl2foBWgRxl4ikr76abbnKVKlW6YIBX267DA7sK8qiMg+pxVq5cOaL/PwD+/j3gyJEjodeyZMniHnvsMde7d29rotayZctQbe5evXq5ePHiuUKFCkX0swMAAABBwz43AMAVqY3Yp08fq7WrmrkpUqSwzveZM2cOBWs7depk27H1evi2awV2O3bs6EaNGmVNlwAEhxZp/HtA37593dy5cy1oq4aKVatWda1bt3Y///yzGzdunN0X1EhNtXd3797tVq1aFWqeRsYuAAAAcGkYOQMALntQp1u3blZLs02bNpape+zYMet8vm7dOpckSRIL8Or1MWPGWMaeb/DgwRb0VWC3Zs2aEfy/AfBXhWffv/32265fv36uXLly1lRxwIABlrF7yy23uIEDB7p27dpZZr7uCblz53arV6+2ILCy+AnsAgAAAJfuGu9CRdEAALhE3333ncuVK1fo+y+++MJKKii4W6JECTd9+nRXv359d/PNN7v9+/e7BQsWuLx589p2bWXslS5d2kozKIOvdu3a7tFHH3W1atWK6P8TgL/v22+/tWaIFSpUsD/SpUsXK8fy4IMPuueee87KtBw/ftwlTpw49Huqv617AQAAAIBLR2oEAOBvq1Onjhs5cmSM1xImTGjbrxXYnT17tnviiScsY2/mzJkWyNHPVqxY4ZImTeoeeuihUGBXWXsTJ04ksAsEiBZytMDj++STT6ye7qeffuqSJ08eev2ll16ywO7nn39u94ODBw/GCOwq14DALgAAAPDXEdwFAPxtzz//vNXWlZ07d9rXe+65xzVt2tTqZr7xxhuucePGrlWrVi59+vQue/bs7sCBA5bFF06BXQmvvQvg6rZw4UJ39OhRly1bttBrpUqVcsWKFbPMfNXcVrM0UeDWD/B+9NFH9iecX84BAAAAwF/DLBoA8LcoeKtamX59TQVyevbsacFd1dVUg6SNGzdacFcU5EmWLJmbM2eOK1y4cIQ/PYB/6v7777da2grMfvjhh7aAo4z9QYMG2c/nz59vr7Vo0cLFjx/faun26NHDZcyY0TL6AQAAAPxz1NwFAPxlsbvZL1682LZi33333a59+/b2VcqWLeu2bNniOnfubM3TVH5hyZIllsUX+98AEMzmaZs2bXKPPfaYS5UqlQVvdf2rnu6TTz5pCzyqo+0HeMNRYxcAAAD455hVAwD+kvCg7Geffeb27Nnj7r33XquXu3LlSvfKK6+4ZcuW2c9fffVVlzNnTjd48GDL2l20aBGBXSAKhJdRULmVjh07WsBXpRfUKFH1dN966y27/pXV279/f1vcCUdgFwAAAPjnyNwFAPytbD1l444fP962V6upkhqpffPNN5ally9fPte1a1dXqFAhe+/evXtdmjRp7Hd///13ausCAfVnCzOqozt8+HC7F3Tr1s0VKVLEMnjr1avnbr75Zjds2DBq6wIAAACXGcFdAMBf1q9fP8vEmzVrlrv99ttdihQpQkGfFStWWIA3b968rk2bNlaT80LBYQDBDeyOHTvWMvWVoasa2lWqVLHXlcGvAG+CBAlCAd7Tp0+Hau5yDwAAAAAuL/bEAgD+kpMnT1rd3BdffNHdddddVm5B/LXCO++8040bN87NnTvXzZ49O8bvEtQBgssP7Hbq1MnKMBw4cMCtWrXK7gUDBgywn9WqVcs1bdrUSjC0bdvWbdiwwTJ59bsKDnMPAAAAAC4v9sUCAP4SZeF9/fXXrmTJkjECPqqfqcDvmTNnLJPvq6++slqcAKKHSitMmjTJTZs2zRqnjR492jVv3tzq6544ccK98MILFuA9deqUZfaq5q6POtsAAADA5ccoGwBwUX42bngFn3jx4llQZ/PmzZa5F041d5Wtd+jQIZcrVy4L+P7xxx//+ucGcHko2zbc7t27XYMGDeweoACvrncFdCtWrGgBXj+D9/HHH3evv/56KGMXAAAAwJVBzV0AwP+sr3n48GH76pdgGDJkiAV1VHv3kUcesWZJek/Dhg3db7/95j799FOy9IAoomtejRLVJHHPnj12fZcrV85KMLRr184tXrzYVapUyRomvvbaa5bNCwAAAODKoywDAOA8Wvfzg7Mvv/yymz59ugVv06ZN6/r27etatmzpjh075vr06eMmT57sbrjhBvu5tmKroZqfrUeAFwim8OtXGbk9e/a0Gtq61m+77TbL2r3++uvdY489Zu/Rex966CFXtWpVV7du3Qh/egAAACDuYNYNADiP3/RIjZIGDhxo27A7d+5sQV/V01TNTTVUGj58uGXr3Xrrrfa6amyqbIOy9wjsAsHlX79qmLZr1y73xhtvuIIFC4ZKtNx4443u4MGDtvCj8iy9e/d2qVKlcvXq1aMcCwAAAPAvoiwDACBEzdASJEhgf9fW67Jly7oOHTqEsvNEWXlLlixxS5cutaBubArqKLgDINjUOLFo0aIW6B0xYoSVXfHt2LHDFn+UwZsoUSKXIkUKe78WdzS09BeIAAAAAFxZpFUBAMycOXPcoEGDLEDjB2mVmZcyZUr7/vTp0/Z1/PjxLnHixFZXU2KvERLYBYJJCzrr1q1z48aNc+vXr7emaSq7ohINixYtcvv27Qu9N0OGDK5Hjx5WX1uN07799ttQ1j6BXQAAAODfQ3AXAODeffdd17hxY/fjjz+GAjPp06d3yZMnd2PHjrXvEyZMaM3SJHv27KGgLoEcIPimTJninnjiCaub27p1a3fnnXda/dzChQtbGZbRo0e7d955xx05ciT0O7pHFClSxFWvXj1UikF1eAEAAAD8ewjuAkAcN2HCBPfkk09aJq6apSmYo0w9eeGFF6yO7tNPP23fx48f377u3bvXJUmSJKKfG8DlodrZTZo0cQ888IBl7W7fvt1169bNff/996506dKWwavXu3fv7gYPHuyOHj16wX+HrH0AAADg30fNXQCIw7TNunbt2u7hhx+2bD3f8ePH3ZYtW6yR0ubNm92oUaMsczdfvnxu48aNVq5h7dq1ZOkBURDY1eKOyq3UqFEjxs8mTpzoevbsaRn8CxcudEOHDnVPPfWU69Spk+vSpYs1VQMAAAAQWczKASCO+/XXX217tW/IkCFu/vz5VmvzjjvusPq6w4YNcyNHjrSGa8rs7d+/vwV2aZ4GBNeCBQtc8+bNrTGaArv+er9fXqFWrVp2f2jfvr2VbWjZsqU7cOCAmzlzpuvVq1ekPz4AAAAAMncBIG5T5m6hQoVcuXLlXN26dW3LtTJ1S5Qo4apVq2b1NZWhp6zeZ555JsbvqnESmbtAcP3www9WZzdFihQWwL333ntDP1Nplmuv/U/1LmXsFy9e3BZ+RENH1dr2vwIAAACIHGruAkAcljp1amuUpO3XTZs2tVIM6nz/0ksvWWOlMmXKWOausvViI7ALBFvWrFlDGfkvv/yyW7JkSehnftBW9XVPnTrl0qVLF+NnBHYBAACAqwPBXQCI49QwSRl88+bNc6tXr7amSilTpgz9XI3TMmbMGNHPCODKBXgHDRpkgVqVWli6dGmMn2/bts1lyJDBFS1a1L73N3wR2AUAAACuDpRlAABctGRDo0aN3P79+y3gQ21dIHppgadNmzYWvO3atauVaFDplapVq1p5hmnTpoXKNAAAAAC4ehDcBQDEoGDuiBEjbIu2mikpsBsvXjyapwFxJMCrIK5qbb/22mtu48aNltGve0B4HV4AAAAAVwdG6ACAGHbs2GEB3SxZsrgvv/zSgjrK4COwC8SdEg2lSpVyGzZsCAV2dQ8gsAsAAABcfcjcBQCc5/Dhwy5p0qQW5CFjF4hblK07ePBgy9xV40QFdmmgCAAAAFydCO4CAC5KjwgaJwFxF4FdAAAA4OpGcBcAAAAAAAAAAojiaQAAAAAAAAAQQAR3AQAAAAAAACCACO4CAAAAAAAAQAAR3AUAAAAAAACAACK4CwAAAAAAAAABRHAXAAAAAAAAAAKI4C4AAAAAAAAABBDBXQAAAAAAAAAIIIK7AAAAAAAAAOCC5/8ANFMKIK5PDSYAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 1500x1200 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Make a copy of the original dataframe\n",
    "df_encoded = df.copy()\n",
    "\n",
    "label_enc = LabelEncoder()\n",
    "\n",
    "# Loop through all object columns and encode them\n",
    "for col in df_encoded.select_dtypes(include='object').columns:\n",
    "    df_encoded[col] = label_enc.fit_transform(df_encoded[col])\n",
    "\n",
    "# Calculate the correlation matrix\n",
    "corr_matrix = df_encoded.corr()\n",
    "\n",
    "# Plot heatmap\n",
    "plt.figure(figsize=(15, 12))\n",
    "sns.heatmap(corr_matrix, annot=True, fmt=\".2f\", cmap='coolwarm', linewidths=0.5)\n",
    "plt.title(\"Correlation Matrix of All Features\")\n",
    "plt.xticks(rotation=45, ha='right')\n",
    "plt.yticks(rotation=0)\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " **Top Features Associated with Human Personality**\n",
    " **Positively Associated Features**\n",
    "1. **Time_spent_Alone**\n",
    "   → Time Spent Alone give gave correlation with human personality and it's have effect to determine Introvert or Ekstovert person.\n",
    "\n",
    "2. **Stage_fear**\n",
    "   → Fear of stage or showing up at the stage is strong correlative with human personality.\n",
    "\n",
    "3. **Drain_after_socializing**\n",
    "   → Drain after sociallizing is one of the strong influences in determining personality.\n",
    "\n",
    "---\n",
    "\n",
    " **Negatively Associated Features**\n",
    "\n",
    "1. **Social_event_attendance**\n",
    "   → Attending the event social have less correlative with the personality, because either introvert or ekstrovert can attending the event.\n",
    "\n",
    "2. **Going_outside**\n",
    "   → Going outside have less correlative with the personality, because introvert can going outside without fear.\n",
    "\n",
    "3. **Friends_circle_size**\n",
    "   → Ekstrovert or Introvert maybe can have same circle size.\n",
    "\n",
    "4. **Post_frequency**\n",
    "   → Social media post have less correlative with personality.\n",
    "\n",
    "---\n",
    "\n",
    " **Key Insight**\n",
    "\n",
    "> human personality is most influenced by quality time and how they are communicate not their activity.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Detecting Outliers for Top Positive and Negative Associated Features"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-25T04:46:26.046734Z",
     "start_time": "2025-05-25T04:46:25.375460Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['Time_spent_Alone', 'Social_event_attendance', 'Going_outside',\n",
      "       'Friends_circle_size', 'Post_frequency'],\n",
      "      dtype='object')\n"
     ]
    },
    {
     "data": {
      "image/png": "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Zdy4cTJw4ECzrnDhwvLyyy9L7969fdFGAAAAAEnQ4Pc333wjTz/9tE8/R0fAOtM5oEqWLCkNGjRI8j0abNdSOAAAAEB65HHwXTvQOuGqLufOnTPrNBgPAAAAIO2VKlXKJMj89NNPUrFiRcmcObPL675IkLl69aq8++67ZuRrctns58+fl5iYGDMJ7O233y6jR4+W8uXLJ7vvK1eumMV29uxZr7YdAAAACNjguzOC7gAAAIB/zZw5U3LkyCGrV682izMNjPsi+L506VI5ffq0PP7440luc+utt8rs2bOlUqVKcubMGXn99ddN2crff/9dihYtmuT7xowZI8OGDfN6mwEAAICADL5XrVo1xfUZvTmpEwAAAIDk7d27N80/8+2335YWLVqY8pNJqVWrlllsGni/7bbbZMaMGTJixIgk36elLZ3nktLM9+joaC+2HgAAAAig4HubNm183xIEtCNHjpiMJQDwxL59+1z+BQBPRUVFSYECBfzdjKCgpWA0EK912DNluqkBrsnS/6YvX75clixZ4tH7tByOJvXs2rUr2e0iIiLMAgAAAAS7FPXKhw4dmqKdxcXF3Wx7EKCB90cf6yTXrv6v9iYAeGLUqFH+bgKAIJU5PELefWc+AfhkXLx4UXr16iXz5s0zz//66y8pUaKEWVekSBEZMGCAVz9vzpw5kj9/fmnVqpVH79N7ha1bt0rLli292h4AAAAgUHklJUY7+Dr0dP78+XLo0CFv7BIBRDPeNfB+qUQDic8S5e/mAACAdCLs8hmRPatNX4TguyRbpmXLli2yatUqufvuux3rmzRpIi+//LJXg+86caoG3zt37pwou75Tp04m2K8129Xw4cPlzjvvNBPCan341157zWTNP/nkk15rDwAAABCSwXfNsPnwww/NJErr1q2T6tWru9RmROjRwHt89nz+bgYAAAASTH6q/XINdDvP01S+fHnZvXu3Vz9Ly83s379fnnjiiUSv6fqwsDDH81OnTkm3bt3k8OHDkjt3bqlWrZqsXbtWypUr59U2AQAAACETfP/pp5/krbfekkWLFkmxYsXkjz/+kJUrV0q9evV80sDixYu7rRX8n//8R6ZOnZpo/dy5c6VLly4u67Rm5OXLl33SPgAAAMCfjh07ZsrAJHThwgWXYLw3NGvWTCzLcvuaZt47mzBhglkAAACA9Op/qSk3MG7c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AAAAQKgJqLIzS5cuNUH2O++801GHUmkW/O7duz3a1z333GMWAAAAAP+X2a5JKdmzZzePkzN+/Pg0axcAAAAQqgIq+H7s2DHJnz9/ovUXLlxwCcYDAAAA8MymTZvk2rVrjsdJod8NAAAAhGDwvXr16vLFF1+YGu/OHX+dAKpWrVp+bh0AAAAQ3HXe3T0GAAAAkA6C7zpBaosWLWT79u1y/fp1mTRpknm8du1aWb16tb+bBwAAAISks2fPynfffSdly5Y1CwAAAIAQm3C1bt26snnzZhN4r1ixonzzzTemDM26deukWrVq/m4eAAAAEBIeeughmTJlinl86dIlMwJV12kf/KOPPvJ38wAAAICQEFCZ76pkyZIya9YsfzcDAAAACFlr1qyRQYMGmccff/yxWJYlp0+flnnz5snIkSPlgQce8HcTAQAAgKCXKRCGuKZUZGSkT9sCAAAApAdnzpyRPHnymMfLli0zwfZs2bJJq1at5IUXXvB38wAAAICQ4Pfge65cuRwTq95IXFycz9sDAAAAhLro6GhT2lED8Bp8X7BggVl/6tQpyZIli7+bBwAAAIQEvwffV65c6Xj8999/y4ABA+Txxx+XWrVqmXV6U6DDX8eMGePHVgIAAACh49lnn5VHHnlEcuTIITExMdKwYUNHORqt+w4AAAAgBILvDRo0cDwePny4jB8/Xjp27OhYd++995obgJkzZ0rnzp391EoAAAAgdPznP/+RmjVryv79+6Vp06YSFhZm1pcoUcLUfAcAAABw8/6vlx0gNMu9evXqidbrul9++cUvbQIAAABCUbVq1eT+++832e82rflep04dlzmX9uzZ46cWAgAAAMEtLNBqT86aNSvR+rfeesu8BgAAACDtWJbl7yYAAAAAQcvvZWecTZgwQR544AH56quvzDBYpRnvO3fulI8++sjfzQMAAAAAAAAAIPiC7y1btpS//vpLpk2bJjt27DDrWrduLU8//TSZ73525MgROXPmjL+bASDI7Nu3z+VfAPBUVFSUFChQwN/NAAAAAIDgDr4rDbKPHj3a381AgsD7o491kmtXr/i7KQCC1KhRo/zdBABBKnN4hLz7znwC8AAAAACCjt+D77/99ptUqFBBwsLCzOPkVKpUKc3ahf/RjHcNvF8q0UDis0T5uzkAACCdCLt8RmTPatMXIfjuHxkyZPB3EwAA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BQAAAAhZAZX5rsNdM2fOnGi9rks4FBYAAABA6oSHh0upUqX83QwAAAAgpAVU8P2uu+4yw18PHjzoWPfvv/9K3759pXHjxn5tGwAAABAqnnvuOZk0aRIjRgEAAID0UnZmypQpcu+990rx4sUlOjrarNu/f79UrFhR3n33XX83DwAAAAgJP/zwg6xcuVK++uorKV++fKLRp0uWLPFb2wAAAIBQEVDBdw24b9y4UVasWCF//PGHWaf135s0aeLvpgEAAAAhI1euXHL//ff7uxkAAABASAuI4PulS5dMwP2ee+6RDBkymMdXrlwxr+3du1e++eYbGT58uGTJksXfTQUAAACC3pw5c/zdBNyksMtn/N0EAACQTtDvCPLg+7x58+SLL74wwXe7/IwOf82aNat5vmPHDilUqJCp/Q4AAADg5l2/fl1WrVolu3fvlocfflhy5sxp5l6KjIyUHDly+Lt5SEJUVJRkDo8Q2bPa300BAADpiPY/tB+CIAy+v/fee9K/f3+Xde+//76UKFHCPNZ671OnTiX4DgAAAHjBvn375O677zbzK+mI06ZNm5rg+6uvvmqeT58+3d9NRBIKFCgg774zX86cIQMNgOf/7R81apQMGjRIYmJi/N0cAEFGA+/aD0EQBt937dplJlW1aXmZsLAwx/MaNWpIz549/dQ6AAAAILT06dNHqlevLlu2bJG8efM61msd+G7duvm1bbgxvfHl5hdAamngvUyZMv5uBgCkCwERfD99+rSjxrs6duyYy+vx8fEurwMAAABIve+//17Wrl0r4eHhLuuLFy8u//77r9/aBQAAAISS/6WX+1HRokVl27ZtSb7+22+/mW0AAAAA3DxNbomLi0u0/p9//jHlZwAAAACESPC9ZcuWMmTIELl8+XKi1y5duiTDhg2TVq1a+aVtAAAAQKhp1qyZTJw40fE8Q4YMcv78eRk6dKjpmwMAAAAIkbIzL774oixcuFBuvfVWeeaZZxy1x/7880+ZMmWKXL9+3WwDAAAA4OaNGzdOmjdvLuXKlTMJMA8//LDs3LlT8uXLJx988IG/mwcAAACEhIAIvutkQVpzskePHjJgwACxLMuRgdO0aVN58803mVAoAIRdPuPvJgAAgHSEvofvaElHnWx1wYIFpsSjZr137dpVHnnkEcmaNau/mwcAAACEhIAIvqvY2FhZtmyZnDx5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8BTBdwBBr0WLFlK9enXH865du0qBAgXkgw8+COrgu68cPXrU/JsrV64Uv6devXomIK66dOkiZcqUMQH5efPmycCBAyWQjq1cuXI33O7y5csSHh4uYWEMAAMAAAAAAL5B1AFAyNGgctasWSVTJtffFy9cuCDPPfecREdHS0REhNx6663y+uuvm4x5denSJSlbtqxZ9LFNy7MUKlTI1EiPi4sz6x5//HHJkSOHKb3SvHlzUztdM8A1C9/eX3I2bdpkfjSIjIw0+2ncuLH89NNPjtc1e19Lwygto2OXfdEyMDfK/NZAubZHz8N9990nf/zxh+N1bXeDBg3MY92/7lMz6z111113mX/37t3rWPfmm29K+fLlzbnVc9GzZ085ffq0y/t27twpDzzwgKnJniVLFilatKh06NBBzpw5Y17X9uj3pEF9+5i1zTdil8fR9mhGvv1eLdljv7ZgwQJ56aWXpEiRIpItWzY5e/asee/PP/8sd999t0RFRZn1en5+/PHHRJ/xww8/mOx/bXfJkiVlxowZpiyQ7tumn6fP9ftLSe3/f//9V5544gnzY5GeNz1/s2fPdntsCxculFGjRplzpm3Qa2bXrl2JPkePR0d+5M6d21wHlSpVkkmTJpnX5syZY/al15+7EQcZM2Y0bQIAAAAAADePzHcAQU8Dt8ePHzdBb818fuONN8zEm48++qhjG33t3nvvlZUrV5rM+CpVqsjXX38tL7zwggk2au1zDdhr0LdOnToyaNAgGT9+vHmvBpH1MzSgqsFJmwbiNWirZU7Gjh0ry5YtM+VOrl+/boLwSfn9999NgFwD7/379zd11DWQq0Hw1atXS82aNaV+/foms3zy5Mny4osvym233Wbea//rzvLly01AX2uya5BXf0DQc6HHo6VitHTNU089ZYLPGmi1S8lo4Dc1pWtU3rx5zb/6eVoip0mTJqbe+p9//inTpk0zE7tqIFuP8erVq+aHiitXrkivXr1MAF7P/eeff26C9Br81jrtWgqnRo0a0r17d7NvDXTfiJ4XfW/fvn1NcFp/ZFG33HKLo2b+iBEjTLb7888/b9qgj/XHCj1n1apVM9+dZsJrgFp/XPj+++9NO5SW12nWrJnZnx6rfse6fWrOnU1LJOm1o8HwZ555xuxb5yrQ61N/GEg4Wewrr7xi2qft1+tRr7lHHnnEBNtt3377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/fDDD087zmtK7969o6CgIB5//PH/+pkNGzZEly5d0k795C8Mqut8T47Nks73JIBfuXJlOj8egB3/f8Qll1wS9957b3Tq1Km2ywHYrSXfUZNGEd9RAQBgD5/5vlkSpuyKQKW0tDRmzZoV06dP367nGjRoEEcddVQsXry42nsKCwvTAwAAAAAAajV8T2a8T548OWbPnh0ff/xxOt5lS8n89yxNmjQp3eT1zDPP3O46X3/99SguLs60HgAAAAAAyDx8TzZWTcL3JAzv1q3bN26AurOSYD8J3wcNGhT161cteeDAgbHffvulc9sTN910Uxx33HHRsWPHdD78mDFj0q75iy++uMbqAwAAAACATML3adOmxUMPPbRLOsqTcTNlZWUxdOjQra4l6/n5/9o3dsWKFTFs2LBYvnx5tGjRIrp37x7z5s2Lrl271nidAAAAAACwU+F7svFp0l2+K/Tq1Suq2xf22WefrXJ+++23pwcAAAAAANSWf7WMb6crr7wyxo8fX20oDgAAAAAAuWqHO9+fe+65mDNnTjzxxBNx2GGHRYMGDapcnz59ehb1AQAAAABA7oTvzZs3j3POOSfbagAAAAAAIJfD90mTJmVbCQAAAAAA5PrM98TGjRtj1qxZcc8998Tq1avTtWXLlsWaNWuyqg8AAAAAAHKn8720tDT69OkTZWVlsW7dujjjjDOiSZMmcdttt6XnEydOzLZSAAAAAADY0zvfhw8fHsccc0ysWLEiGjVqVLmezIGfPXt2VvUBAAAAAEDudL7/9a9/jXnz5kVBQUGV9QMPPDA++OCDLGoDAAAAAIDc6nwvLy+PTZs2bbW+dOnSdPwMAAAAAADkqh0O33v16hV33HFH5XleXl660er1118fxcXFWdUHAAAAAAC5M3Zm7Nix0bt37+jatWusXbs2zj///Hj77bejZcuW8bvf/S7bKgEAAAAAIBfC9/333z9effXVmDZtWrz22mtp1/tFF10UF1xwQZUNWAEAAAAAINfU36mH69ePCy+8MLtqAAAAAAAgl8P3KVOmfOP1gQMH7uhHUwd99NFHsXLlytouA9jNlJaWVnkF2F7NmjWL1q1b13YZAAAA2y2voqKiYvsfi2jRokWV8w0bNsRXX30VBQUFsddee8Xnn38eu6tVq1alv+glYXPTpk0j1yXB+4X/MzA2rF9X26UAADmmQUFhTP2/KQJ431EBACB3Ot9XrFix1Vqy4eqPf/zjGDly5M7WRR2S/IKXBO9fH9wzyhs2q+1yAIAckb92ZcS7c9PvIsJ3AAAgp2a+/7tDDjkkRo8enc6BX7hwYZYfTR2QBO/ljVvWdhkAAAAAAHVeftYfmGzCumzZsqw/FgAAAAAA9vzO98cee6zKeTI6/sMPP4wJEybECSeckEVtAAAAAACQW+F7v379qpzn5eVFq1at4tRTT42xY8dmURsAAAAAAORW+F5eXp5tJQAAAAAAsIfIfOY7AAAAAADkuh3ufB8xYsR/fe+4ceN29McAAAAAAEDuhO+vvPJKemzYsCE6d+6cri1atCjq1asXRx99dJVZ8AAAAAAAkEt2eOzM2WefHSeffHIsXbo05s+fnx5LliyJU045Jc4666yYM2dOejzzzDM7VeANN9yQBvhbHoceeug3PvPwww+n9zRs2DAOP/zwmDlz5k7VAAAAAAAAuyR8Hzt2bIwaNSpatGhRuZa8/9///d/0WpYOO+yw+PDDDyuP5557rtp7582bFwMGDIiLLroo7czv169feixYsCDTmgAAAAAAIPPwfdWqVfHJJ59stZ6srV69OrJUv379aNOmTeXRsmXLau8dP3589OnTJ0aOHBldunSJm2++OR2DM2HChExrAgAAAACAzMP3c845J4YMGRLTp09PR88kxyOPPJJ2nPfv3z+y9Pbbb0e7du3i4IMPjgsuuCDKysqqvff555+P008/vcpa796903UAAAAAAKjTG65OnDgxrrrqqjj//PPTTVfTD6tfPw3fx4wZk1mBxx57bEyePDnd1DUZOXPjjTfGSSedlI6RadKkyVb3L1++PFq3bl1lLTlP1quzbt269Niyqx8AAAAAAHZ5+L7XXnvFXXfdlQbt77zzTrrWoUOHaNy4cWTpe9/7XuX7I444Ig3j27dvHw899FAa9GchmV2fhPoAAAAAAFCrY2c227wJ6iGHHJIG7xUVFVGTmjdvHp06dYrFixdv83oyE/6jjz6qspacJ+vVufrqq2PlypWVx5IlSzKvGwAAAACA3LHD4ftnn30Wp512WhqEFxcXpwF8IulGv/LKK6OmrFmzJu20b9u27TavH3/88TF79uwqa08//XS6Xp3CwsJo2rRplQMAAAAAAHZ5+P7zn/88GjRokG5+moyg2ey8886LJ598MrKS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",
      "text/plain": [
       "<Figure size 1500x800 with 5 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# List of numeric features to check\n",
    "features_to_check = df.select_dtypes(include=\"number\").columns\n",
    "print(features_to_check)\n",
    "\n",
    "# Boxplot visualization\n",
    "plt.figure(figsize=(15, 8))\n",
    "for i, col in enumerate(features_to_check):\n",
    "    plt.subplot(4, 2, i+1)\n",
    "    sns.boxplot(y=df_encoded[col])\n",
    "    plt.title(f'Boxplot of {col}')\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Insight**\n",
    "* All numeric column don't have outliers, and don't need special attention to fix it"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "cpgHfgnSK3ip"
   },
   "source": [
    "# **5. Data Preprocessing**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-25T04:46:26.051814Z",
     "start_time": "2025-05-25T04:46:26.047516Z"
    }
   },
   "outputs": [],
   "source": [
    "df_processed = df.copy()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Handling Missing Values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['Time_spent_Alone', 'Social_event_attendance', 'Going_outside',\n",
      "       'Friends_circle_size', 'Post_frequency'],\n",
      "      dtype='object')\n",
      "\n",
      "Index(['Stage_fear', 'Drained_after_socializing'], dtype='object')\n"
     ]
    }
   ],
   "source": [
    "# Get numeric column that have missing values \n",
    "missing_cols_numeric = df_processed.select_dtypes(include=\"number\").columns[df.select_dtypes(include=\"number\").isnull().any()]\n",
    "print(missing_cols_numeric)\n",
    "print()\n",
    "\n",
    "# Get object column that have missing values \n",
    "missing_cols_object = df_processed.select_dtypes(include=\"object\").columns[df.select_dtypes(include=\"object\").isnull().any()]\n",
    "print(missing_cols_object)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\ThinkPad\\AppData\\Local\\Temp\\ipykernel_20000\\2233039039.py:3: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.\n",
      "The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.\n",
      "\n",
      "For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.\n",
      "\n",
      "\n",
      "  df_processed[col].fillna(df_processed[col].median(), inplace=True)\n",
      "C:\\Users\\ThinkPad\\AppData\\Local\\Temp\\ipykernel_20000\\2233039039.py:3: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.\n",
      "The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.\n",
      "\n",
      "For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.\n",
      "\n",
      "\n",
      "  df_processed[col].fillna(df_processed[col].median(), inplace=True)\n",
      "C:\\Users\\ThinkPad\\AppData\\Local\\Temp\\ipykernel_20000\\2233039039.py:3: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.\n",
      "The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.\n",
      "\n",
      "For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.\n",
      "\n",
      "\n",
      "  df_processed[col].fillna(df_processed[col].median(), inplace=True)\n",
      "C:\\Users\\ThinkPad\\AppData\\Local\\Temp\\ipykernel_20000\\2233039039.py:3: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.\n",
      "The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.\n",
      "\n",
      "For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.\n",
      "\n",
      "\n",
      "  df_processed[col].fillna(df_processed[col].median(), inplace=True)\n",
      "C:\\Users\\ThinkPad\\AppData\\Local\\Temp\\ipykernel_20000\\2233039039.py:3: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.\n",
      "The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.\n",
      "\n",
      "For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.\n",
      "\n",
      "\n",
      "  df_processed[col].fillna(df_processed[col].median(), inplace=True)\n",
      "C:\\Users\\ThinkPad\\AppData\\Local\\Temp\\ipykernel_20000\\2233039039.py:8: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.\n",
      "The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.\n",
      "\n",
      "For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.\n",
      "\n",
      "\n",
      "  df_processed[col].fillna(df_processed[col].mode()[0], inplace=True)\n"
     ]
    }
   ],
   "source": [
    "# Impute numerical columns with the median\n",
    "for col in missing_cols_numeric:\n",
    "    df_processed[col].fillna(df_processed[col].median(), inplace=True)\n",
    "\n",
    "# Impute categorical columns with the mode\n",
    "for col in missing_cols_object:\n",
    "    if col in df_processed.columns:\n",
    "        df_processed[col].fillna(df_processed[col].mode()[0], inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Time_spent_Alone             0\n",
       "Stage_fear                   0\n",
       "Social_event_attendance      0\n",
       "Going_outside                0\n",
       "Drained_after_socializing    0\n",
       "Friends_circle_size          0\n",
       "Post_frequency               0\n",
       "Personality                  0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_processed.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-25T04:46:26.085809Z",
     "start_time": "2025-05-25T04:46:26.058015Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Time_spent_Alone</th>\n",
       "      <th>Stage_fear</th>\n",
       "      <th>Social_event_attendance</th>\n",
       "      <th>Going_outside</th>\n",
       "      <th>Drained_after_socializing</th>\n",
       "      <th>Friends_circle_size</th>\n",
       "      <th>Post_frequency</th>\n",
       "      <th>Personality</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>2900.000000</td>\n",
       "      <td>2900</td>\n",
       "      <td>2900.000000</td>\n",
       "      <td>2900.000000</td>\n",
       "      <td>2900</td>\n",
       "      <td>2900.000000</td>\n",
       "      <td>2900.000000</td>\n",
       "      <td>2900</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>unique</th>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>top</th>\n",
       "      <td>NaN</td>\n",
       "      <td>No</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>No</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Extrovert</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>freq</th>\n",
       "      <td>NaN</td>\n",
       "      <td>1490</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1493</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1491</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>4.494828</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.942759</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>6.235172</td>\n",
       "      <td>3.552069</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>3.441971</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.875987</td>\n",
       "      <td>2.221597</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.237255</td>\n",
       "      <td>2.894794</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>2.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>4.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>7.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>10.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>11.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>10.000000</td>\n",
       "      <td>7.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>15.000000</td>\n",
       "      <td>10.000000</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Time_spent_Alone Stage_fear  Social_event_attendance  Going_outside  \\\n",
       "count        2900.000000       2900              2900.000000    2900.000000   \n",
       "unique               NaN          2                      NaN            NaN   \n",
       "top                  NaN         No                      NaN            NaN   \n",
       "freq                 NaN       1490                      NaN            NaN   \n",
       "mean            4.494828        NaN                 3.942759       3.000000   \n",
       "std             3.441971        NaN                 2.875987       2.221597   \n",
       "min             0.000000        NaN                 0.000000       0.000000   \n",
       "25%             2.000000        NaN                 2.000000       1.000000   \n",
       "50%             4.000000        NaN                 3.000000       3.000000   \n",
       "75%             7.000000        NaN                 6.000000       5.000000   \n",
       "max            11.000000        NaN                10.000000       7.000000   \n",
       "\n",
       "       Drained_after_socializing  Friends_circle_size  Post_frequency  \\\n",
       "count                       2900          2900.000000     2900.000000   \n",
       "unique                         2                  NaN             NaN   \n",
       "top                           No                  NaN             NaN   \n",
       "freq                        1493                  NaN             NaN   \n",
       "mean                         NaN             6.235172        3.552069   \n",
       "std                          NaN             4.237255        2.894794   \n",
       "min                          NaN             0.000000        0.000000   \n",
       "25%                          NaN             3.000000        1.000000   \n",
       "50%                          NaN             5.000000        3.000000   \n",
       "75%                          NaN            10.000000        6.000000   \n",
       "max                          NaN            15.000000       10.000000   \n",
       "\n",
       "       Personality  \n",
       "count         2900  \n",
       "unique           2  \n",
       "top      Extrovert  \n",
       "freq          1491  \n",
       "mean           NaN  \n",
       "std            NaN  \n",
       "min            NaN  \n",
       "25%            NaN  \n",
       "50%            NaN  \n",
       "75%            NaN  \n",
       "max            NaN  "
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_processed.describe(include='all')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Encoding Categorical Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-25T04:46:26.118486Z",
     "start_time": "2025-05-25T04:46:26.099093Z"
    }
   },
   "outputs": [],
   "source": [
    "label_enc = LabelEncoder()\n",
    "\n",
    "# Dictionary to store encoders\n",
    "encoders = {}\n",
    "\n",
    "# Encode categorical features\n",
    "categorical_features = df_processed.select_dtypes(include='object').columns.tolist()\n",
    "\n",
    "# Get  numerical feature\n",
    "numerical_features = df_processed.select_dtypes(include=['number']).columns.tolist()\n",
    "\n",
    "for col in categorical_features:\n",
    "    label_enc = LabelEncoder()\n",
    "    df_processed[col] = label_enc.fit_transform(df_processed[col])\n",
    "    encoders[col] = label_enc "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Feature Scaling"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-25T04:46:26.127175Z",
     "start_time": "2025-05-25T04:46:26.119184Z"
    }
   },
   "outputs": [],
   "source": [
    "X = df_processed.drop(columns=['Personality'])\n",
    "y = df_processed['Personality']\n",
    "\n",
    "scaler = StandardScaler()\n",
    "X_scaled = scaler.fit_transform(X[numerical_features])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Combine Scaled Features with Encoded Categorical Features"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-25T04:46:26.134851Z",
     "start_time": "2025-05-25T04:46:26.128344Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Features after combination:\n",
      "    Time_spent_Alone  Stage_fear  Social_event_attendance  Going_outside  \\\n",
      "0         -0.143788           0                 0.019907       1.350613   \n",
      "1          1.309119           1                -1.371160      -1.350613   \n",
      "2          1.309119           1                -1.023393      -0.450204   \n",
      "3         -1.306113           0                 0.715440       1.800817   \n",
      "4         -0.434369           0                 1.758740       0.450204   \n",
      "\n",
      "   Drained_after_socializing  Friends_circle_size  Post_frequency  \n",
      "0                          0             1.596787        0.500271  \n",
      "1                          1            -1.471766       -0.190744  \n",
      "2                          1            -0.291553       -0.536251  \n",
      "3                          0             1.832829        1.536793  \n",
      "4                          0             0.416574        0.500271  \n"
     ]
    }
   ],
   "source": [
    "# Convert scaled features back to DataFrame\n",
    "X_scaled = pd.DataFrame(X_scaled, columns=numerical_features)\n",
    "\n",
    "# Add encoded categorical features to the scaled DataFrame\n",
    "for col in categorical_features:\n",
    "    X_scaled[col] = df_processed[col].values\n",
    "   \n",
    "# Reorder columns to match original DataFrame\n",
    "X_scaled = X_scaled[X.columns]\n",
    "\n",
    "# Display the first few rows\n",
    "print(\"Features after combination:\\n\", X_scaled.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Split Data 80:20"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-25T04:46:26.146460Z",
     "start_time": "2025-05-25T04:46:26.135893Z"
    }
   },
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(\n",
    "    X_scaled, y, test_size=0.2, random_state=42, stratify=y\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Export Data to CSV"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-25T04:46:26.314979Z",
     "start_time": "2025-05-25T04:46:26.147678Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Preprocessing complete. File saved as 'student_depression_processed.csv'\n"
     ]
    }
   ],
   "source": [
    "# Combine X_scaled and y into a final DataFrame\n",
    "df_final = pd.concat([X_scaled, y.reset_index(drop=True)], axis=1)\n",
    "\n",
    "df_final.to_csv(\"extrovert_introvert_processed.csv\", index=False)\n",
    "\n",
    "print(\"✅ Preprocessing complete. File saved as 'student_depression_processed.csv'\")"
   ]
  }
 ],
 "metadata": {
  "accelerator": "GPU",
  "colab": {
   "gpuType": "T4",
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
