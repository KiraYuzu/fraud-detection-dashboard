import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

from pathlib import Path

st.set_page_config(page_title="Fraud Detection Dashboard", layout="wide")

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / 'data' / 'transactions.csv'

st.title("Fraud Detection Dashboard")
st.markdown("#### A Random Forest-based fraud detection dashboard using transaction amount and transaction hour.")

df = pd.read_csv(DATA_PATH)

total_transactions = len(df)
fraud_count = int(df['is_fraud'].sum())
fraud_rate = fraud_count / total_transactions if total_transactions else 0

metric_col1, metric_col2, metric_col3 = st.columns(3)
metric_col1.metric('Total Transactions', f"{total_transactions:,}")
metric_col2.metric('Fraudulent Transactions', f"{fraud_count:,}")
metric_col3.metric('Fraud Rate', f"{fraud_rate:.2%}")

st.markdown("---")

country_fraud = df.groupby('country')['is_fraud'].sum().reset_index()
fig = px.bar(country_fraud, x="country", y="is_fraud", labels={"country": "Country", "is_fraud": "Fraud Count"}, title="Fraud Cases by Country")
fig.update_layout(margin=dict(l=20, r=20, t=50, b=20), template='plotly_white')

left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("Sample Transaction Data")
    st.dataframe(df.head(10), use_container_width=True)
    st.markdown("### Fraud Distribution")
    st.plotly_chart(fig, use_container_width=True)

with right_col:
    st.subheader("Live Fraud Prediction")
    st.markdown("Enter transaction details to see whether the model predicts fraud.")
    amount = st.number_input('Transaction Amount', min_value=0.0, step=1.0, value=50.0)
    hour = st.slider('Transaction Hour', 0, 23, value=12)

    model_path = BASE_DIR / 'models' / 'fraud_detection_model.pkl'
    try:
        model = joblib.load(model_path)
    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.info("The model file may be missing or incompatible. Retrain and save the model if needed.")
        model = None

    if model:
        if st.button('Predict Fraud'):
            prediction = model.predict([[amount, hour]])
            result = 'Fraudulent' if prediction[0] == 1 else 'Legitimate'
            st.success(f"Prediction: {result}")
    else:
        st.warning("Model unavailable. Please check the model file in /models.")