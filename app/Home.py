import streamlit as st

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Customer Churn & Segmentation Dashboard",
    page_icon="📊",
    layout="wide"
)

# -------------------- HEADER --------------------
st.title("📊 Customer Churn & Segmentation Dashboard")
st.markdown("""
### 🔍 Predict. Segment. Retain Customers Effectively
An end-to-end Machine Learning project to analyze customer behavior, predict churn, and generate actionable business insights.
""")

# -------------------- METRICS --------------------
st.markdown("## 📌 Key Metrics Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("👥 Total Customers", "7043")
col2.metric("📉 Churn Rate", "26.5%")
col3.metric("💰 Avg Monthly Charges", "$64.76")
col4.metric("⏳ Avg Tenure", "32 Months")

# -------------------- DIVIDER --------------------
st.markdown("---")

# -------------------- PROJECT OVERVIEW --------------------
st.markdown("## 🧠 Project Overview")

st.write("""
This project focuses on **Customer Churn Prediction and Segmentation** using Machine Learning techniques.  

It helps businesses:
- Identify customers likely to churn  
- Understand customer segments  
- Take proactive retention actions  
""")

# -------------------- FEATURES --------------------
st.markdown("## 🚀 Key Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 🔍 Churn Prediction
    - Predict whether a customer will churn
    - Probability-based risk scoring
    - Real-time prediction
    """)

    st.markdown("""
    ### 🧠 Customer Segmentation
    - Group customers into meaningful clusters
    - Identify high-value & at-risk users
    """)

with col2:
    st.markdown("""
    ### 📊 Interactive Dashboard
    - Dynamic visualizations
    - Filter-based exploration
    - User-friendly interface
    """)

    st.markdown("""
    ### 💡 Business Insights
    - Key churn drivers
    - Actionable recommendations
    """)

# -------------------- TECH STACK --------------------
st.markdown("---")
st.markdown("## 🛠️ Tech Stack")

st.markdown("""
- **Programming:** Python 🐍  
- **Libraries:** Pandas, NumPy, Scikit-learn  
- **Visualization:** Matplotlib, Seaborn, Plotly  
- **ML Models:** Logistic Regression, Random Forest, XGBoost  
- **Deployment:** Streamlit  
""")

# -------------------- NAVIGATION GUIDE --------------------
st.markdown("---")
st.markdown("## 🧭 Navigation Guide")

st.info("""
Use the sidebar to explore different sections of the project:

- 📊 Data Overview  
- 📈 EDA Dashboard  
- 🧠 Customer Segmentation  
- 🤖 Churn Prediction  
- 📊 Model Performance  
- 💡 Insights & Recommendations  
""")

# -------------------- CALL TO ACTION --------------------
st.markdown("---")
st.success("🚀 Start exploring using the sidebar and uncover powerful insights!")

# -------------------- FOOTER --------------------
st.markdown("---")
st.markdown("""
### 👨‍💻 Developed by Bhupendra Sahu  
B.Tech Student | Data Science Enthusiast  

🔗 Connect on LinkedIn | 🌐 View GitHub Project  
""")