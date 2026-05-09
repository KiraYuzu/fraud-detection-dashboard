# Fraud Detection Analytics Dashboard

## Project Overview

This project is a simulated real-time fraud detection analytics system built using Python. The goal of the project is to analyze financial transaction data, identify suspicious activities, and visualize fraud-related insights through an interactive dashboard.

The project demonstrates the end-to-end workflow of a real-world data analytics project, including:

- Data cleaning
- Exploratory Data Analysis (EDA)
- Feature engineering
- Fraud detection logic
- Machine learning
- Dashboard visualization

This project was designed to simulate how financial institutions and fintech companies monitor transaction activity to reduce fraud risk.

---

# Business Problem

Financial institutions process millions of transactions daily. Detecting fraudulent activity manually is difficult due to:

- High transaction volume
- Real-time processing requirements
- Sophisticated fraud patterns
- Operational risk

This project explores how analytics and machine learning can help identify suspicious transaction behavior automatically.

---

# Objectives

The objectives of this project are to:

- Analyze transaction patterns
- Detect potentially fraudulent transactions
- Build fraud risk indicators
- Visualize fraud activity trends
- Simulate a financial fraud monitoring dashboard

---

# Dataset

The dataset used in this project is a synthetic transaction dataset generated using Python.

The dataset contains:

| Column | Description |
|---|---|
| transaction_id | Unique transaction identifier |
| user_id | Customer identifier |
| amount | Transaction amount |
| country | Country of transaction |
| merchant | Merchant name |
| transaction_time | Timestamp of transaction |
| is_fraud | Fraud label (0 = normal, 1 = fraud) |

Fraud patterns were simulated using:
- high transaction amounts
- overseas transactions
- unusual transaction timing
- random anomaly injection

---

# Technologies Used

## Programming Language
- Python

## Libraries
- Pandas
- NumPy
- Matplotlib
- Plotly
- Scikit-learn
- Streamlit

## Tools
- Jupyter Notebook
- Git
- GitHub

---

# Project Structure

```text
fraud-detection-project/
│
├── data/
│   └── fraud_transactions_dataset.csv
│
├── notebooks/
│   └── eda.ipynb
│
├── app/
│   ├── dashboard.py
│   ├── preprocessing.py
│   ├── model.py
│
├── models/
│
├── screenshots/
│
├── requirements.txt
├── README.md
├── .gitignore