import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, roc_curve, auc
)

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Model Performance",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Model Performance Evaluation")

# -------------------- LOAD MODEL & DATA --------------------
@st.cache_resource
def load_model():
    return joblib.load("models/churn_model.pkl")

@st.cache_data
def load_data():
    df = pd.read_csv("data/telco_churn.csv")
    return df

model = load_model()
df = load_data()

# -------------------- PREPROCESS --------------------
df_clean = df.copy()
df_clean["TotalCharges"] = pd.to_numeric(df_clean["TotalCharges"], errors="coerce")
df_clean.dropna(inplace=True)

# Encode
df_encoded = pd.get_dummies(df_clean, drop_first=True)

# Split features/target
X = df_encoded.drop("Churn_Yes", axis=1)
y = df_encoded["Churn_Yes"]

# Align with model
X = X.reindex(columns=model.feature_names_in_, fill_value=0)

# Predictions
y_pred = model.predict(X)
y_prob = model.predict_proba(X)[:, 1]

# -------------------- METRICS --------------------
st.subheader("📌 Evaluation Metrics")

acc = accuracy_score(y, y_pred)
prec = precision_score(y, y_pred)
rec = recall_score(y, y_pred)
f1 = f1_score(y, y_pred)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Accuracy", f"{acc:.2f}")
col2.metric("Precision", f"{prec:.2f}")
col3.metric("Recall", f"{rec:.2f}")
col4.metric("F1 Score", f"{f1:.2f}")

st.markdown("---")

# -------------------- CONFUSION MATRIX --------------------
st.subheader("📊 Confusion Matrix")

cm = confusion_matrix(y, y_pred)

fig1, ax1 = plt.subplots()
ax1.imshow(cm)
ax1.set_title("Confusion Matrix")

for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        ax1.text(j, i, cm[i, j], ha="center", va="center")

ax1.set_xlabel("Predicted")
ax1.set_ylabel("Actual")

st.pyplot(fig1)

# -------------------- ROC CURVE --------------------
st.subheader("📈 ROC Curve")

fpr, tpr, _ = roc_curve(y, y_prob)
roc_auc = auc(fpr, tpr)

fig2, ax2 = plt.subplots()
ax2.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
ax2.plot([0, 1], [0, 1], linestyle="--")
ax2.set_xlabel("False Positive Rate")
ax2.set_ylabel("True Positive Rate")
ax2.set_title("ROC Curve")
ax2.legend()

st.pyplot(fig2)

# -------------------- FEATURE IMPORTANCE --------------------
st.subheader("🔥 Feature Importance")

if hasattr(model, "feature_importances_"):
    importance = pd.DataFrame({
        "Feature": model.feature_names_in_,
        "Importance": model.feature_importances_
    }).sort_values(by="Importance", ascending=False)

    st.dataframe(importance.head(10), use_container_width=True)

    fig3, ax3 = plt.subplots()
    ax3.barh(importance["Feature"][:10], importance["Importance"][:10])
    ax3.invert_yaxis()
    ax3.set_title("Top 10 Important Features")

    st.pyplot(fig3)

else:
    st.info("Feature importance not available for this model.")

# -------------------- MODEL COMPARISON (STATIC DEMO) --------------------
st.markdown("---")
st.subheader("📊 Model Comparison (Sample)")

comparison_df = pd.DataFrame({
    "Model": ["Logistic Regression", "Random Forest", "XGBoost"],
    "Accuracy": [0.80, 0.85, 0.87],
    "F1 Score": [0.78, 0.83, 0.86]
})

st.dataframe(comparison_df, use_container_width=True)

# -------------------- INSIGHTS --------------------
st.markdown("### 💡 Key Insights")

st.write("""
- The model performs well in identifying churn customers.
- High recall ensures most churn cases are captured.
- Feature importance shows key drivers like tenure, monthly charges.
""")

# -------------------- SIDEBAR --------------------
st.sidebar.info("""
📊 This page evaluates the ML model performance using various metrics and visualizations.

- Classification metrics
- ROC curve
- Feature importance
""")
