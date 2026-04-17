import streamlit as st

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="About Project",
    page_icon="📖",
    layout="wide"
)

# -------------------- TITLE --------------------
st.title("📖 About This Project")

# -------------------- PROJECT DESCRIPTION --------------------
st.markdown("## 📊 Project Overview")

st.write("""
The **Customer Churn & Segmentation Dashboard** is an end-to-end Machine Learning project 
designed to analyze customer behavior, predict churn, and generate actionable business insights.

This project combines **data analysis, machine learning, and interactive visualization** 
to help businesses improve customer retention and maximize revenue.
""")

# -------------------- OBJECTIVES --------------------
st.markdown("## 🎯 Objectives")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    - Predict whether a customer will churn  
    - Identify high-risk customers  
    - Segment customers into meaningful groups  
    """)

with col2:
    st.markdown("""
    - Understand key churn drivers  
    - Provide actionable recommendations  
    - Improve customer retention strategies  
    """)

# -------------------- FEATURES --------------------
st.markdown("## 🚀 Key Features")

st.markdown("""
- 📊 Interactive Data Dashboard  
- 🤖 Machine Learning-based Churn Prediction  
- 🧠 Customer Segmentation using Clustering  
- 📈 Model Performance Evaluation  
- 💡 Business Insights & Recommendations  
""")

# -------------------- TECH STACK --------------------
st.markdown("## 🛠️ Tech Stack")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **Programming & Libraries**
    - Python 🐍  
    - Pandas, NumPy  
    - Scikit-learn  
    """)

with col2:
    st.markdown("""
    **Visualization & Deployment**
    - Matplotlib, Seaborn, Plotly  
    - Streamlit  
    - Joblib (Model Saving)  
    """)

# -------------------- WORKFLOW --------------------
st.markdown("## 🔄 Project Workflow")

st.markdown("""
1. Data Collection & Cleaning  
2. Exploratory Data Analysis (EDA)  
3. Feature Engineering  
4. Model Building (ML Algorithms)  
5. Model Evaluation  
6. Deployment using Streamlit  
""")

# -------------------- ABOUT DEVELOPER --------------------
st.markdown("---")
st.markdown("## 👨‍💻 About the Developer")

col1, col2 = st.columns([1, 3])

with col1:
    st.image("https://via.placeholder.com/150", caption="Bhupendra Sahu")

with col2:
    st.markdown("""
    **Bhupendra Sahu**  
    🎓 B.Tech Student (Data Science Enthusiast)  
    📍 Chhattisgarh, India  

    Passionate about:
    - Data Science & Machine Learning  
    - Building real-world AI projects  
    - Problem solving and analytics  

    Currently working on:
    - Customer Churn Prediction  
    - AI-based Projects  
    - Data-driven solutions  
    """)

# -------------------- CONTACT --------------------
st.markdown("## 🔗 Connect With Me")

st.markdown("""
- 💼 LinkedIn: https://linkedin.com/  
- 💻 GitHub: https://github.com/  
- 📧 Email: your-email@example.com  
""")

# -------------------- FINAL MESSAGE --------------------
st.markdown("---")
st.success("🚀 This project demonstrates real-world application of Machine Learning in business problem solving.")

# -------------------- SIDEBAR --------------------
st.sidebar.info("""
📖 Learn more about the project, developer, and technologies used.

This section highlights:
- Project purpose
- Features
- Developer profile
""")