import streamlit as st
from pathlib import Path
import runpy

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Customer Segmentation & Retention",
    page_icon="📊",
    layout="wide"
)

# -------------------- SIDEBAR --------------------
st.sidebar.markdown("## 📊 Customer Intelligence Dashboard")
st.sidebar.markdown("---")

menu = {
    "🏠 Overview": ["Home"],
    "📊 Data & Analysis": ["Data Overview", "Customer Segmentation"],
    "🤖 ML Models": ["Churn Prediction", "Model Performance"],
    "💡 Insights": ["Insights & Recommendations", "Business Insights"],
    "🛠 Tools": ["Business Helper"],
    "📖 Info": ["About Project"]
}

category = st.sidebar.selectbox("Select Category", list(menu.keys()))
page = st.sidebar.radio("Navigate", menu[category])

# -------------------- ROUTING --------------------
page_files = {
    "Home": "Home.py",
    "Data Overview": "Data_Overview.py",
    "Customer Segmentation": "Customer_Segmentation.py",
    "Churn Prediction": "Churn_Prediction.py",
    "Model Performance": "Model_Performance.py",
    "Insights & Recommendations": "Insights_Recommendations.py",
    "Business Insights": "Business_Insights.py",
    "Business Helper": "Business_Helper.py",
    "About Project": "About_Project.py",
}

runpy.run_path(str(Path(__file__).parent / "pages" / page_files[page]))