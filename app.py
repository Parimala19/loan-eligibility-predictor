import streamlit as st
import joblib
import numpy as np

# Load the model pipeline
model = joblib.load("loan_model.pkl")

st.set_page_config(page_title="🏦 Loan Eligibility Predictor", page_icon="🏦")
st.title("🏦 Loan Eligibility Predictor")
st.markdown("Check if you're eligible for a home loan based on your details.")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income (Monthly)", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income (Monthly)", min_value=0)
loan_amount = st.number_input("Loan Amount (in 1000s)", min_value=0)
loan_term = st.selectbox("Loan Term (in months)", [360, 240, 180, 120, 60])
credit_history = st.selectbox("Credit History", [1.0, 0.0])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Predict
if st.button("Check Eligibility"):
    input_data = {
        'Gender': gender,
        'Married': married,
        'Dependents': dependents,
        'Education': education,
        'Self_Employed': self_employed,
        'ApplicantIncome': applicant_income,
        'CoapplicantIncome': coapplicant_income,
        'LoanAmount': loan_amount,
        'Loan_Amount_Term': loan_term,
        'Credit_History': credit_history,
        'Property_Area': property_area
    }

    input_df = [input_data]
    prediction = model.predict(input_df)[0]
    confidence = model.predict_proba(input_df)[0][prediction]

    if prediction == 1:
        st.success(f"✅ Loan Approved\n\nConfidence: {confidence:.2f}")
    else:
        st.error(f"❌ Loan Not Approved\n\nConfidence: {confidence:.2f}")
