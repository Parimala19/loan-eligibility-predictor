import streamlit as st
import numpy as np
import joblib

# Load model and encoders
model = joblib.load('loan_model.pkl')
le_dict = joblib.load('encoders.pkl')

st.set_page_config(page_title="🏦 Loan Eligibility Predictor", page_icon="💰")
st.title("🏦 Loan Eligibility Predictor")
st.markdown("Check if you're eligible for a home loan based on your details.")

# --- Input Fields ---
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income (Monthly)", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income (Monthly)", min_value=0)
loan_amount = st.number_input("Loan Amount (in 1000s)", min_value=0)
loan_term = st.selectbox("Loan Term (in months)", [360, 300, 240, 180, 120, 60])
credit_history = st.selectbox("Credit History", [1.0, 0.0])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# --- Input Dictionary ---
input_dict = {
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

# --- Encode Inputs ---
encoded_input = []
for col in input_dict:
    if col in le_dict:
        encoded_input.append(le_dict[col].transform([input_dict[col]])[0])
    else:
        encoded_input.append(input_dict[col])

# --- Validation + Prediction ---
if st.button("Check Eligibility"):
    if applicant_income == 0 and coapplicant_income == 0:
        st.error("❌ Income cannot be zero for both applicant and coapplicant.")
    elif loan_amount == 0:
        st.error("❌ Please enter a valid loan amount.")
    elif loan_amount > (applicant_income + coapplicant_income) * 0.3:
        st.warning("⚠️ The loan amount seems unusually high compared to the income.")
    else:
        prediction = model.predict([encoded_input])[0]
        if prediction == 1:
            st.success("✅ Loan Approved")
        else:
            st.error("❌ Loan Not Approved")
