import streamlit as st
import numpy as np
import joblib

# Load model and encoders
model = joblib.load('loan_model.pkl')
le_dict = joblib.load('encoders.pkl')

st.title("🏦 Loan Eligibility Predictor")

# User Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount (in 1000s)", min_value=0)
loan_term = st.selectbox("Loan Term (in months)", [360, 120, 180, 240, 300, 60])
credit_history = st.selectbox("Credit History", [1.0, 0.0])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Prepare input data
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

# Encode input data
encoded_input = []
for col in input_dict:
    if col in le_dict:
        encoded_input.append(le_dict[col].transform([input_dict[col]])[0])
    else:
        encoded_input.append(input_dict[col])

# Predict and Show Result
if st.button("Check Eligibility"):
    prediction = model.predict([encoded_input])
    result = "✅ Loan Approved" if prediction[0] == 1 else "❌ Loan Not Approved"
    st.success(result)
