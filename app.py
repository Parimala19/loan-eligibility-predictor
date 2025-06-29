import streamlit as st
import pickle
import numpy as np

# Load model and encoder
model = pickle.load(open("load_model.pkl", "rb"))
encoder = pickle.load(open("encoder.pkl", "rb"))

st.set_page_config(page_title="🏦 Loan Eligibility Predictor", page_icon="💰")
st.title("🏦 Loan Eligibility Predictor")
st.markdown("Check if you're eligible for a home loan based on basic financial and personal details.")

# User input fields
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income (Monthly)", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income (Monthly)", min_value=0)
loan_amount = st.number_input("Loan Amount (in 1000s)", min_value=0)
loan_term = st.selectbox("Loan Term (in months)", [12, 36, 60, 84, 120, 180, 240, 300, 360])
credit_history = st.selectbox("Credit History", [1.0, 0.0])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Validation checks
if st.button("Check Eligibility"):
    if applicant_income == 0 and coapplicant_income == 0:
        st.error("❌ Income cannot be zero for both applicant and coapplicant.")
    elif loan_amount == 0:
        st.error("❌ Please enter a valid loan amount.")
    elif loan_amount * 1000 > (applicant_income + coapplicant_income) * 60:
        st.warning("⚠️ Loan requested is unusually high compared to income.")
    else:
        # Create input array
        user_input = np.array([[gender, married, dependents, education, self_employed,
                                applicant_income, coapplicant_income, loan_amount,
                                loan_term, credit_history, property_area]])

        # Encode categorical columns
        encoded_input = encoder.transform(user_input)
        prediction = model.predict(encoded_input)

        if prediction[0] == 1:
            st.success("✅ Loan Approved")
        else:
            st.error("❌ Loan Not Approved")
