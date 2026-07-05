import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("customer_churn.pkl", "rb"))

st.title("Customer Churn Prediction")

# -------------------- Inputs --------------------

gender = st.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
Partner = st.selectbox("Partner", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.number_input("Tenure", min_value=0, value=1)
PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No"])
InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
OnlineSecurity = st.selectbox("Online Security", ["Yes", "No"])
OnlineBackup = st.selectbox("Online Backup", ["Yes", "No"])
DeviceProtection = st.selectbox("Device Protection", ["Yes", "No"])
TechSupport = st.selectbox("Tech Support", ["Yes", "No"])
StreamingTV = st.selectbox("Streaming TV", ["Yes", "No"])
StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No"])
PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
MonthlyCharges = st.number_input("Monthly Charges", value=50.0)
TotalCharges = st.number_input("Total Charges", value=100.0)

Contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

PaymentMethod = st.selectbox(
    "Payment Method",
    [
        "Bank transfer (automatic)",
        "Credit card (automatic)",
        "Electronic check",
        "Mailed check"
    ]
)

# -------------------- Label Encoding --------------------

gender = 1 if gender == "Male" else 0
Partner = 1 if Partner == "Yes" else 0
Dependents = 1 if Dependents == "Yes" else 0
PhoneService = 1 if PhoneService == "Yes" else 0
MultipleLines = 1 if MultipleLines == "Yes" else 0
OnlineSecurity = 1 if OnlineSecurity == "Yes" else 0
OnlineBackup = 1 if OnlineBackup == "Yes" else 0
DeviceProtection = 1 if DeviceProtection == "Yes" else 0
TechSupport = 1 if TechSupport == "Yes" else 0
StreamingTV = 1 if StreamingTV == "Yes" else 0
StreamingMovies = 1 if StreamingMovies == "Yes" else 0
PaperlessBilling = 1 if PaperlessBilling == "Yes" else 0

# IMPORTANT:
# Change these mappings if your LabelEncoder produced different numbers.

internet_map = {
    "DSL": 0,
    "Fiber optic": 1,
    "No": 2
}

InternetService = internet_map[InternetService]

# -------------------- One Hot Encoding --------------------

bank = 1 if PaymentMethod == "Bank transfer (automatic)" else 0
credit = 1 if PaymentMethod == "Credit card (automatic)" else 0
electronic = 1 if PaymentMethod == "Electronic check" else 0
mailed = 1 if PaymentMethod == "Mailed check" else 0

month = 1 if Contract == "Month-to-month" else 0
one = 1 if Contract == "One year" else 0
two = 1 if Contract == "Two year" else 0

# -------------------- DataFrame --------------------

input_df = pd.DataFrame([[
    gender,
    SeniorCitizen,
    Partner,
    Dependents,
    tenure,
    PhoneService,
    MultipleLines,
    InternetService,
    OnlineSecurity,
    OnlineBackup,
    DeviceProtection,
    TechSupport,
    StreamingTV,
    StreamingMovies,
    PaperlessBilling,
    MonthlyCharges,
    TotalCharges,
    bank,
    credit,
    electronic,
    mailed,
    month,
    one,
    two
]], columns=[
    'gender',
    'SeniorCitizen',
    'Partner',
    'Dependents',
    'tenure',
    'PhoneService',
    'MultipleLines',
    'InternetService',
    'OnlineSecurity',
    'OnlineBackup',
    'DeviceProtection',
    'TechSupport',
    'StreamingTV',
    'StreamingMovies',
    'PaperlessBilling',
    'MonthlyCharges',
    'TotalCharges',
    'PaymentMethod_Bank transfer (automatic)',
    'PaymentMethod_Credit card (automatic)',
    'PaymentMethod_Electronic check',
    'PaymentMethod_Mailed check',
    'Contract_Month-to-month',
    'Contract_One year',
    'Contract_Two year'
])

# -------------------- Prediction --------------------

if st.button("Predict"):

    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.error("Customer is likely to Churn.")
    else:
        st.success("Customer is NOT likely to Churn.")