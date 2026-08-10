import pandas as pd
import joblib
from pathlib import Path
from sklearn.linear_model import LogisticRegression

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "WA_Fn-UseC_-Telco-Customer-Churn.csv"

def project_path(path):
    candidate = Path(path)
    return candidate if candidate.is_absolute() else BASE_DIR / candidate

def load_data(path):
    df = pd.read_csv(project_path(path))
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df.dropna(inplace=True)
    return df

def load_model(path):
    try:
        model = joblib.load(project_path(path))
        if not hasattr(model, "feature_names_in_"):
            raise ValueError("The saved model has no feature schema")
        return model
    except (FileNotFoundError, KeyError, EOFError, ValueError, ImportError, OSError):
        df = load_data(DATA_PATH)
        features = pd.get_dummies(
            df.drop(columns=["customerID", "Churn"]), drop_first=True
        )
        model = LogisticRegression(max_iter=2000, solver="liblinear", random_state=42)
        model.fit(features, (df["Churn"] == "Yes").astype(int))
        return model

def basic_metrics(df):
    churn_rate = (df["Churn"] == "Yes").mean() * 100
    return {
        "customers": len(df),
        "churn_rate": round(churn_rate, 2),
        "avg_charge": round(df["MonthlyCharges"].mean(), 2)
    }