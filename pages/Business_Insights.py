import streamlit as st
import pandas as pd
from utils.recommendations import generate_business_recommendations

st.title("🎯 Business Insights & Recommendations")

file = st.file_uploader("Upload Sales Data", type=["csv"])

if file:
    df = pd.read_csv(file)

    st.subheader("Preview")
    st.dataframe(df.head())

    # Column selection
    date_col = st.selectbox("Select Date Column", df.columns)
    product_col = st.selectbox("Select Product Column", df.columns)
    sales_col = st.selectbox("Select Sales Column", df.columns)

    df[date_col] = pd.to_datetime(df[date_col])
    df = df.sort_values(date_col)

    # Generate recommendations
    recommendations = generate_business_recommendations(
        df, date_col, product_col, sales_col
    )

    st.subheader("💡 Smart Recommendations")

    for rec in recommendations:
        st.success(rec)