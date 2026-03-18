import streamlit as st
import pandas as pd

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Insights & Recommendations",
    page_icon="💡",
    layout="wide"
)

st.title("💡 Insights & Business Recommendations")

# -------------------- LOAD DATA --------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/telco_churn.csv")
    return df

df = load_data()

# -------------------- BASIC PREPROCESS --------------------
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df.dropna(inplace=True)

# -------------------- OVERVIEW METRICS --------------------
st.subheader("📊 Key Business Metrics")

churn_rate = (df["Churn"] == "Yes").mean() * 100
avg_monthly = df["MonthlyCharges"].mean()
avg_tenure = df["tenure"].mean()

col1, col2, col3 = st.columns(3)

col1.metric("📉 Overall Churn Rate", f"{churn_rate:.2f}%")
col2.metric("💰 Avg Monthly Charges", f"${avg_monthly:.2f}")
col3.metric("⏳ Avg Tenure", f"{avg_tenure:.1f} months")

st.markdown("---")

# -------------------- KEY INSIGHTS --------------------
st.subheader("🔍 Key Insights")

# Contract insight
contract_churn = df.groupby("Contract")["Churn"].apply(lambda x: (x=="Yes").mean()*100)

# Internet insight
internet_churn = df.groupby("InternetService")["Churn"].apply(lambda x: (x=="Yes").mean()*100)

# Payment insight
payment_churn = df.groupby("PaymentMethod")["Churn"].apply(lambda x: (x=="Yes").mean()*100)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📄 Contract Type Impact")
    st.dataframe(contract_churn.round(2))

    st.info("👉 Customers with **Month-to-Month contracts** show higher churn risk.")

with col2:
    st.markdown("### 🌐 Internet Service Impact")
    st.dataframe(internet_churn.round(2))

    st.warning("👉 **Fiber optic users** tend to churn more due to higher costs.")

st.markdown("### 💳 Payment Method Impact")
st.dataframe(payment_churn.round(2))

st.info("👉 Customers using **Electronic Check** show higher churn probability.")

st.markdown("---")

# -------------------- CUSTOMER RISK SEGMENTATION --------------------
st.subheader("🚦 Customer Risk Segmentation")

def risk_category(row):
    if row["tenure"] < 12 and row["MonthlyCharges"] > 70:
        return "High Risk"
    elif row["tenure"] < 24:
        return "Medium Risk"
    else:
        return "Low Risk"

df["RiskLevel"] = df.apply(risk_category, axis=1)

risk_counts = df["RiskLevel"].value_counts()

col1, col2, col3 = st.columns(3)

col1.metric("🔴 High Risk Customers", risk_counts.get("High Risk", 0))
col2.metric("🟡 Medium Risk Customers", risk_counts.get("Medium Risk", 0))
col3.metric("🟢 Low Risk Customers", risk_counts.get("Low Risk", 0))

st.markdown("---")

# -------------------- RECOMMENDATIONS --------------------
st.subheader("🎯 Business Recommendations")

tab1, tab2, tab3 = st.tabs(["🔴 High Risk", "🟡 Medium Risk", "🟢 Low Risk"])

with tab1:
    st.error("High Risk Customers – Immediate Action Required")
    st.write("""
    - Offer **discounts or retention plans**
    - Provide **priority customer support**
    - Give **loyalty rewards**
    - Personalized communication (email/SMS)
    """)

with tab2:
    st.warning("Medium Risk Customers – Monitor & Engage")
    st.write("""
    - Improve service quality
    - Offer bundled services
    - Provide engagement offers
    """)

with tab3:
    st.success("Low Risk Customers – Retain & Upsell")
    st.write("""
    - Promote premium plans
    - Upsell additional services
    - Maintain high service quality
    """)

st.markdown("---")

# -------------------- BUSINESS IMPACT --------------------
st.subheader("📈 Business Impact")

st.write("""
- Reducing churn by even **5% can significantly increase revenue**
- Retaining customers is cheaper than acquiring new ones
- Targeted strategies improve customer satisfaction and lifetime value
""")

# -------------------- DOWNLOAD REPORT --------------------
st.subheader("⬇️ Download Insights Report")

report = df[["customerID", "RiskLevel", "MonthlyCharges", "tenure"]]

st.download_button(
    label="Download Report CSV",
    data=report.to_csv(index=False),
    file_name="customer_insights.csv",
    mime="text/csv"
)

# -------------------- SIDEBAR --------------------
st.sidebar.info("""
💡 This section provides business insights and actionable recommendations
based on customer behavior and churn patterns.

Focus:
- Identify risk groups
- Improve retention
- Increase revenue
""")
