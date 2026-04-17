import streamlit as st
import pandas as pd
import numpy as np
import joblib

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Churn Prediction",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Customer Churn Prediction")

# -------------------- LOAD MODEL --------------------
@st.cache_resource
def load_model():
    model = joblib.load("models/churn_model.pkl")  # update path if needed
    return model

model = load_model()

# -------------------- INPUT SECTION --------------------
st.subheader("📝 Enter Customer Details")

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior = st.selectbox("Senior Citizen", [0, 1])
    partner = st.selectbox("Has Partner", ["Yes", "No"])
    dependents = st.selectbox("Has Dependents", ["Yes", "No"])

with col2:
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    phone = st.selectbox("Phone Service", ["Yes", "No"])
    internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])

with col3:
    monthly = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
    total = st.number_input("Total Charges", 0.0, 10000.0, 1000.0)
    payment = st.selectbox("Payment Method", [
        "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
    ])
    paperless = st.selectbox("Paperless Billing", ["Yes", "No"])

# -------------------- PREPROCESS INPUT --------------------
def preprocess_input():
    data = {
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone,
        "InternetService": internet,
        "Contract": contract,
        "MonthlyCharges": monthly,
        "TotalCharges": total,
        "PaymentMethod": payment,
        "PaperlessBilling": paperless
    }

    df = pd.DataFrame([data])

    # Encoding similar to training
    df = pd.get_dummies(df)

    return df

# -------------------- PREDICTION --------------------
if st.button("🔍 Predict Churn"):

    input_df = preprocess_input()

    # Align columns with model
    model_features = model.feature_names_in_
    input_df = input_df.reindex(columns=model_features, fill_value=0)

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    st.markdown("---")
    st.subheader("📊 Prediction Result")

    col1, col2 = st.columns(2)

    # -------------------- RESULT --------------------
    if prediction == 1:
        col1.error("⚠️ High Risk of Churn")
    else:
        col1.success("✅ Low Risk of Churn")

    # -------------------- PROBABILITY --------------------
    col2.metric("Churn Probability", f"{probability*100:.2f}%")

    st.progress(float(probability))

    # -------------------- INTERPRETATION --------------------
    st.markdown("### 💡 Insights")

    if probability > 0.7:
        st.error("🔴 Customer is highly likely to churn. Immediate action required.")
    elif probability > 0.4:
        st.warning("🟡 Moderate churn risk. Monitor closely.")
    else:
        st.success("🟢 Customer is likely to stay.")

    # -------------------- RECOMMENDATIONS --------------------
    st.markdown("### 🎯 Recommended Actions")

    if probability > 0.7:
        st.write("""
        - Offer discounts or special plans  
        - Provide dedicated customer support  
        - Engage with personalized offers  
        """)
    elif probability > 0.4:
        st.write("""
        - Improve service quality  
        - Provide loyalty benefits  
        - Send engagement emails  
        """)
    else:
        st.write("""
        - Maintain service quality  
        - Upsell premium services  
        """)

# -------------------- SIDEBAR INFO --------------------
st.sidebar.info("""
🤖 This module predicts whether a customer is likely to churn.

- Uses trained ML model
- Provides probability score
- Suggests business actions
""")
