import streamlit as st
import joblib
import pandas as pd

# Load model and encoders
model = joblib.load("loan_model.pkl")
encoders = joblib.load("encoders.pkl")

st.set_page_config(page_title="🏦 Loan Eligibility Predictor", page_icon="🏦")
st.title("🏦 Loan Eligibility Predictor")
st.markdown("Check if you're eligible for a home loan based on your details.")

# User Inputs
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

# Prediction logic
if st.button("Check Eligibility"):

    # Validate inputs
    if applicant_income == 0 and coapplicant_income == 0:
        st.warning("⚠️ Please enter at least one valid income value.")
    elif loan_amount == 0:
        st.warning("⚠️ Loan Amount must be greater than 0.")
    else:
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

        # Encode categorical fields using encoders.pkl
        encoded_values = []
        for key, value in input_dict.items():
            if key in encoders:
                encoder = encoders[key]
                try:
                    encoded_val = encoder.transform([value])[0]
                except:
                    st.error(f"Encoding failed for: {key} - {value}")
                    st.stop()
                encoded_values.append(encoded_val)
            else:
                encoded_values.append(value)

        # Calculate Loan to Income Ratio
        total_income = applicant_income + coapplicant_income
        if total_income > 0:
            loan_to_income_ratio = loan_amount / (total_income + 1)
        else:
            loan_to_income_ratio = 999  # Force rejection if no income

        # Predict
        prediction = model.predict([encoded_values])[0]
        confidence = model.predict_proba([encoded_values])[0][prediction]

        # Override logic if income is clearly sufficient
        if total_income > 500000 and loan_to_income_ratio < 2 and credit_history == 1.0:
            st.success(f"✅ Loan Approved (Overridden based on high income)\n\nConfidence: 0.99")
        else:
            if prediction == 1:
                st.success(f"✅ Loan Approved\n\nConfidence: {confidence:.2f}")
            else:
                st.error(f"❌ Loan Not Approved\n\nConfidence: {confidence:.2f}")
