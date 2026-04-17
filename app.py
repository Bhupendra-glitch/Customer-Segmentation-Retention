import streamlit as st

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Customer Segmentation & Retention",
    page_icon="📊",
    layout="wide"
)

# -------------------- IMPORT PAGES --------------------
from pages.Home import show_home
from pages.Data_Overview import show_data_overview
from pages.Customer_Segmentation import show_segmentation
from pages.Churn_Prediction import show_prediction
from pages.Model_Performance import show_model_performance
from pages.Insights_Recommendations import show_insights
from pages.About_Project import show_about
from pages.Business_Insights import show_business_insights
from pages.Business_Helper import show_business_helper

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
if page == "Home":
    show_home()

elif page == "Data Overview":
    show_data_overview()

elif page == "Customer Segmentation":
    show_segmentation()

elif page == "Churn Prediction":
    show_prediction()

elif page == "Model Performance":
    show_model_performance()

elif page == "Insights & Recommendations":
    show_insights()

elif page == "Business Insights":
    show_business_insights()

elif page == "Business Helper":
    show_business_helper()

elif page == "About Project":
    show_about()