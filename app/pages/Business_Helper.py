import streamlit as st
import pandas as pd

st.title("🛒 Small Business Helper Dashboard")

file = st.file_uploader("Upload Sales Data", type=["csv"])

if file:
    df = pd.read_csv(file)

    st.subheader("📊 Data Preview")
    st.dataframe(df.head())

    # User selects columns
    date_col = st.selectbox("Select Date Column", df.columns)
    product_col = st.selectbox("Select Product Column", df.columns)
    sales_col = st.selectbox("Select Sales Column", df.columns)

    df[date_col] = pd.to_datetime(df[date_col])

    # 🔥 1. Best Selling Product
    best_product = df.groupby(product_col)[sales_col].sum().idxmax()

    # 🔻 Low Performing Product
    worst_product = df.groupby(product_col)[sales_col].sum().idxmin()

    st.subheader("🏆 Product Insights")
    col1, col2 = st.columns(2)

    col1.success(f"Best Selling Product: {best_product}")
    col2.error(f"Low Performing Product: {worst_product}")

    # 📅 When to Restock (based on peak sales day)
    df['day'] = df[date_col].dt.day_name()
    peak_day = df.groupby('day')[sales_col].sum().idxmax()

    st.subheader("📦 Restock Recommendation")
    st.info(f"Highest sales occur on: {peak_day} → Keep more stock before this day")

    # 📊 Sales by Product
    st.subheader("📊 Sales by Product")
    st.bar_chart(df.groupby(product_col)[sales_col].sum())