# 📊 Telco Customer Churn Classification

## 📌 Project Overview

Customer churn is one of the most important problems in the telecom industry. Customers can easily switch to other providers if they are not satisfied with the services offered.

This project focuses on **predicting customer churn** using machine learning techniques. By identifying customers who are likely to leave, telecom companies can take proactive steps to **improve customer retention and reduce revenue loss**.

The project includes **data analysis, feature engineering, and predictive modeling** to classify customers as churn or non-churn.

---

# 🎯 Aim

- To **classify potential churn customers** based on numerical and categorical features.
- To solve a **binary classification problem** using machine learning.
- To analyze patterns in customer behavior that lead to churn.

---

# 📂 Dataset Description

The dataset contains information about telecom customers including demographic data, services subscribed, billing details, and churn status.

### Dataset Attributes

| Feature | Description |
|------|-------------|
| customerID | Unique ID for each customer |
| gender | Customer gender (Male / Female) |
| SeniorCitizen | Whether the customer is a senior citizen (1 = Yes, 0 = No) |
| Partner | Whether the customer has a partner |
| Dependents | Whether the customer has dependents |
| tenure | Number of months the customer stayed with the company |
| PhoneService | Whether the customer has phone service |
| MultipleLines | Whether the customer has multiple phone lines |
| InternetService | Internet service type (DSL / Fiber / No) |
| OnlineSecurity | Online security service |
| OnlineBackup | Online backup service |
| DeviceProtection | Device protection service |
| TechSupport | Technical support service |
| StreamingTV | Streaming TV service |
| StreamingMovies | Streaming movies service |
| Contract | Contract type (Monthly / One year / Two year) |
| PaperlessBilling | Whether billing is paperless |
| PaymentMethod | Payment method used by customer |
| MonthlyCharges | Monthly bill amount |
| TotalCharges | Total charges paid |
| Churn | Whether the customer left the service (Yes / No) |

---

# 📑 Project Workflow

The project follows the standard **Machine Learning Pipeline**:
Dataset Information
↓
Exploratory Data Analysis (EDA)
↓
Data Cleaning
↓
Feature Engineering
↓
Model Building
↓
Model Evaluation
↓
Result Analysis

---

# 🔍 Exploratory Data Analysis (EDA)

EDA was performed to understand:

- Customer demographics
- Service usage patterns
- Billing behavior
- Factors influencing churn

Common techniques used:

- Distribution plots
- Correlation analysis
- Count plots
- Feature relationship analysis

Libraries used:
--Pandas
--NumPy
--Matplotlib
--Seaborn

---

# ⚙️ Feature Engineering

Feature engineering steps include:

- Handling missing values
- Encoding categorical variables
- Feature scaling
- Removing irrelevant features
- Converting target variable to binary format

---

# 🤖 Machine Learning Models Used

Multiple classification algorithms were applied:

- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Machine
- K-Nearest Neighbors
- Gradient Boosting

These models were compared to find the best performing algorithm.

---

# 📊 Model Evaluation Metrics

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- ROC-AUC Score

---

# 📈 Expected Outcome

The model predicts whether a customer is **likely to churn or stay**.

This can help telecom companies:

- Identify high-risk customers
- Improve customer retention strategies
- Reduce revenue loss
- Improve customer satisfaction

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

---

# 📁 Project Structure
Telco-Customer-Churn-Classification
│
├── dataset
│ └── telco_churn.csv
│
├── notebooks
│ └── churn_analysis.ipynb
│
├── models
│ └── trained_model.pkl
│
├── images
│ └── visualizations
│
└── README.md
