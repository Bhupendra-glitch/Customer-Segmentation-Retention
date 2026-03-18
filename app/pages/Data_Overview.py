import streamlit as st
import pandas as pd

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Data Overview",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Data Overview")

# -------------------- LOAD DATA --------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/telco_churn.csv")  # change path if needed
    return df

df = load_data()

# -------------------- TABS --------------------
tab1, tab2, tab3, tab4 = st.tabs(
    ["📄 Dataset Preview", "📋 Column Details", "❗ Missing Values", "📊 Data Types"]
)

# -------------------- TAB 1: DATA PREVIEW --------------------
with tab1:
    st.subheader("📄 Dataset Preview")

    st.write("Shape of dataset:", df.shape)

    st.dataframe(df.head(50), use_container_width=True)

    st.download_button(
        label="⬇️ Download Dataset",
        data=df.to_csv(index=False),
        file_name="telco_data.csv",
        mime="text/csv"
    )

# -------------------- TAB 2: COLUMN DETAILS --------------------
with tab2:
    st.subheader("📋 Column Descriptions")

    column_info = {
        "customerID": "Unique Customer ID",
        "gender": "Male or Female",
        "SeniorCitizen": "Whether customer is senior citizen (1, 0)",
        "Partner": "Has partner (Yes/No)",
        "Dependents": "Has dependents (Yes/No)",
        "tenure": "Number of months with company",
        "PhoneService": "Has phone service (Yes/No)",
        "MultipleLines": "Multiple lines or not",
        "InternetService": "DSL, Fiber optic, No",
        "OnlineSecurity": "Has online security",
        "OnlineBackup": "Has online backup",
        "DeviceProtection": "Has device protection",
        "TechSupport": "Has tech support",
        "StreamingTV": "Has streaming TV",
        "StreamingMovies": "Has streaming movies",
        "Contract": "Contract type",
        "PaperlessBilling": "Paperless billing or not",
        "PaymentMethod": "Payment method used",
        "MonthlyCharges": "Monthly bill amount",
        "TotalCharges": "Total bill amount",
        "Churn": "Customer churn (Yes/No)"
    }

    col_df = pd.DataFrame(list(column_info.items()), columns=["Column", "Description"])
    st.dataframe(col_df, use_container_width=True)

# -------------------- TAB 3: MISSING VALUES --------------------
with tab3:
    st.subheader("❗ Missing Values Analysis")

    missing = df.isnull().sum().reset_index()
    missing.columns = ["Column", "Missing Values"]

    st.dataframe(missing, use_container_width=True)

    total_missing = missing["Missing Values"].sum()

    col1, col2 = st.columns(2)
    col1.metric("Total Missing Values", total_missing)
    col2.metric("Columns with Missing Data", (missing["Missing Values"] > 0).sum())

# -------------------- TAB 4: DATA TYPES --------------------
with tab4:
    st.subheader("📊 Data Types")

    dtype_df = pd.DataFrame(df.dtypes, columns=["Data Type"])
    dtype_df.reset_index(inplace=True)
    dtype_df.columns = ["Column", "Data Type"]

    st.dataframe(dtype_df, use_container_width=True)

    # Count types
    num_cols = df.select_dtypes(include=['int64', 'float64']).shape[1]
    cat_cols = df.select_dtypes(include=['object']).shape[1]

    col1, col2 = st.columns(2)
    col1.metric("🔢 Numerical Columns", num_cols)
    col2.metric("🔤 Categorical Columns", cat_cols)

# -------------------- SIDEBAR INFO --------------------
st.sidebar.info("""
📌 This section provides a complete overview of the dataset,
including structure, missing values, and feature descriptions.
""")