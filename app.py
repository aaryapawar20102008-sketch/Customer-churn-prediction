import numpy as np
import pandas as pd
import pickle
import streamlit as st


model = pickle.load(open("customer_churn.pkl", 'rb'))


st.title("Customer Churn Prediction")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
Partner = st.selectbox("Partner", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.number_input("Tenure", min_value=0, max_value=100, value=1)
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
Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
PaymentMethod = st.selectbox(
    "Payment Method",
    [
        "Bank transfer (automatic)",
        "Credit card (automatic)",
        "Electronic check",
        "Mailed check"
    ]
)

# Create dataframe (column names must match your training data)
input_df = pd.DataFrame([[
    gender, SeniorCitizen, Partner, Dependents,
    tenure, PhoneService, MultipleLines,
    InternetService,OnlineSecurity, OnlineBackup,
    DeviceProtection, TechSupport,
    StreamingTV, StreamingMovies,
    PaperlessBilling, MonthlyCharges,
    TotalCharges,Contract,PaymentMethod
    

]], columns=[
     'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
       'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity','OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
       'StreamingMovies', 'PaperlessBilling', 'MonthlyCharges', 'TotalCharges', 'PaymentMethod_Bank transfer (automatic)',
       'PaymentMethod_Credit card (automatic)', 'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check',
       'Contract_Month-to-month', 'Contract_One year', 'Contract_Two year'
])

if st.button("Predict"):
    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.error("Customer is likely to Churn.")
    else:
        st.success("Customer is Not likely to Churn.")
    
