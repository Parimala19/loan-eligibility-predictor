

📘 `README.md` — *Loan Eligibility Predictor*

🏦 Loan Eligibility Predictor

This project is a Machine Learning-based web application that predicts whether a loan will be approved based on user input. Built using **Python**, **Streamlit**, and **scikit-learn**, it helps demonstrate your skills in data preprocessing, model building, and web deployment.

🔍 Problem Statement

Given applicant details such as income, education, credit history, etc., predict whether the loan application will be approved (`Y`) or not (`N`). This project uses the publicly available dataset from Kaggle: [Loan Prediction Dataset](https://www.kaggle.com/datasets/ninzaami/loan-predication).

---

 🚀 Tech Stack

- **Python**
- **Pandas & NumPy** – Data handling
- **scikit-learn** – Model training (Logistic Regression)
- **LabelEncoder** – Categorical encoding
- **Joblib** – Saving and loading model/encoders
- **Streamlit** – Web app interface
- **Streamlit Cloud** – Deployment

---

📊 Features

- Takes user inputs via Streamlit UI
- Preprocesses inputs using saved encoders
- Predicts loan eligibility using a trained Logistic Regression model
- Shows result in an interactive way (`✅ Approved` or `❌ Not Approved`)
- Fully deployed and shareable via public link



🧠 ML Model

- Model Used: Logistic Regression
- Target Variable: Loan_Status
- Accuracy Achieved: ~80% on test data


🛠️ How to Run

1. Clone this repo or download the files
2. Install dependencies:  
   pip install -r requirements.txt


3. Run the app locally:

   streamlit run app.py
  

🌐 Live Demo

👉 https://loan-eligibility-predictor-chvlkxctam4tyzuukvbyed.streamlit.app/



 📂 File Structure


loan_eligibility_predictor/
│
├── app.py               # Streamlit app UI
├── train_model.py       # (Optional) Training script
├── loan_model.pkl       # Trained ML model
├── encoders.pkl         # Saved label encoders
├── requirements.txt     # For deployment
└── README.md            # Project info




🤝 Credits

* Dataset: [Kaggle - Loan Prediction Dataset](https://www.kaggle.com/datasets/ninzaami/loan-predication)
* Built by: Parimala Tejaswi (https://github.com/Parimala19)

---

📬 Contact

Feel free to connect with me on www.linkedin.com/in/parimala-tejaswi for feedback or collaboration!



