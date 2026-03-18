import pandas as pd
import joblib

def load_data(path):
    df = pd.read_csv(path)
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df.dropna(inplace=True)
    return df

def load_model(path):
    return joblib.load(path)

def basic_metrics(df):
    churn_rate = (df["Churn"] == "Yes").mean() * 100
    return {
        "customers": len(df),
        "churn_rate": round(churn_rate, 2),
        "avg_charge": round(df["MonthlyCharges"].mean(), 2)
    }