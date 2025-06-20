# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CPrb2tpTrUnyuaIzoQszIj9ZsV7Je6xF
"""

# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# Load the trained model
model = pickle.load(open("churn_model.pkl", "rb"))

# Title
st.title("📊 Customer Churn Prediction Dashboard")

# Tabs
tab1, = st.tabs(["🔮 Predict Churn"])

# --- TAB 1: Predict Churn ---
with tab1:
    st.header("Predict Churn for a New Customer")

    # User Input Form
    with st.form("churn_form"):
        tenure = st.number_input("Tenure (months)", min_value=0, value=12)
        phone = st.selectbox("Phone Service (1 = Yes, 0 = No)", [1, 0])
        contract = st.selectbox("Contract Type (0 = M2M, 1 = One year, 2 = Two year)", [0, 1, 2])
        billing = st.selectbox("Paperless Billing (1 = Yes, 0 = No)", [1, 0])
        payment = st.selectbox("Payment Method (0 = E-check, 1 = Mailed, 2 = Bank, 3 = Credit Card)", [0, 1, 2, 3])
        monthly = st.number_input("Monthly Charges", value=70.0)
        total = st.number_input("Total Charges", value=500.0)

        submit = st.form_submit_button("Predict")

        if submit:
            # Ensure column names and order match training data
            expected_cols = ['tenure', 'PhoneService', 'Contract', 'PaperlessBilling',
                             'PaymentMethod', 'MonthlyCharges', 'TotalCharges']

            input_df = pd.DataFrame([[
                tenure, phone, contract, billing, payment, monthly, total
            ]], columns=expected_cols)

            # Predict using the loaded model
            pred = model.predict(input_df)[0]
            prob = model.predict_proba(input_df)[0][1]

            if pred == 1:
                st.error(f"⚠️ This customer is likely to churn! (Confidence: {prob:.2%})")
            else:
                st.success(f"✅ This customer is likely to stay. (Confidence: {1 - prob:.2%})")
