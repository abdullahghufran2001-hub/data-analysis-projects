# 🏦 Loan Approval Prediction

A beginner-friendly **Machine Learning project** that predicts whether a loan application is likely to be **Approved or Rejected** using applicant and loan-related information.

The project uses **Python, Pandas, NumPy, Matplotlib, and Scikit-Learn** to perform data preprocessing, feature encoding, model training, prediction, and evaluation.

---

## 📌 Project Overview

Loan approval decisions depend on several factors such as applicant information, income, loan amount, credit history, and other application details.

This project demonstrates how Machine Learning can be used to analyze historical loan application data and predict the loan approval status.

### 🎯 Main Objective

To build a **Logistic Regression classification model** that predicts:

```text
Loan Approved
       OR
Loan Rejected
```

---

# 🧠 Machine Learning Algorithm

### Logistic Regression

The project uses **Logistic Regression**, a supervised Machine Learning algorithm commonly used for binary classification problems.

In this project, the model predicts two possible outcomes:

```text
1 → Loan Approved
0 → Loan Rejected
```

---

# 🛠️ Technologies Used

* 🐍 Python
* 🐼 Pandas
* 🔢 NumPy
* 📊 Matplotlib
* 🤖 Scikit-Learn
* 📄 CSV Dataset

---

# 📦 Python Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
```

Install the required libraries using:

```bash
pip install pandas numpy matplotlib scikit-learn
```

---

# 📂 Dataset

The project uses a CSV file named:

```text
loan_data.csv
```

The dataset contains loan application information used to train the Machine Learning model.

Typical loan datasets can contain applicant-related and loan-related attributes such as:

* Applicant information
* Income
* Loan amount
* Loan term
* Credit history
* Property information
* Loan status

The exact columns depend on the provided `loan_data.csv` dataset.

---

# 🔄 Machine Learning Workflow

```text
Loan Dataset
     ↓
Load CSV File
     ↓
Explore Dataset
     ↓
Check Data Types
     ↓
Check Missing Values
     ↓
Handle Missing Values
     ↓
Remove Loan_ID
     ↓
Convert Categorical Data
     ↓
Define Features & Target
     ↓
Train-Test Split
     ↓
Train Logistic Regression
     ↓
Make Predictions
     ↓
Calculate Accuracy
     ↓
Generate Confusion Matrix
     ↓
Loan Approval Prediction
```

---

# 🧹 Data Preprocessing

## 1️⃣ Load Dataset

The CSV dataset is loaded using Pandas:

```python
df = pd.read_csv(file_path)
```

---

## 2️⃣ Explore the Dataset

The project displays the first five rows:

```python
print(df.head())
```

It also checks the data types:

```python
print(df.dtypes)
```

---

## 3️⃣ Handle Missing Values

Missing numerical values are replaced with their corresponding column mean:

```python
df.fillna(
    df.mean(numeric_only=True),
    inplace=True
)
```

This helps prevent missing numerical values from interfering with model training.

---

## 4️⃣ Remove Loan ID

`Loan_ID` is an identifier rather than a meaningful predictive feature, so it is removed:

```python
if 'Loan_ID' in df.columns:
    df.drop('Loan_ID', axis=1, inplace=True)
```

---

## 5️⃣ Convert Categorical Data

Machine Learning models require numerical input.

Categorical columns are converted into numerical dummy variables using:

```python
df = pd.get_dummies(
    df,
    drop_first=True
)
```

---

# 🎯 Features & Target

The target variable is:

```python
y = df['Loan_Status_Y']
```

This represents the loan approval outcome.

The remaining columns are used as input features:

```python
X = df.drop(
    'Loan_Status_Y',
    axis=1
)
```

---

# ✂️ Train-Test Split

The dataset is divided into:

* **80% Training Data**
* **20% Testing Data**

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

The training dataset is used to train the model, while the testing dataset is used to evaluate its predictions.

---

# 🤖 Model Training

A Logistic Regression model is created:

```python
model = LogisticRegression(
    max_iter=1000
)
```

The model is then trained using:

```python
model.fit(
    X_train,
    y_train
)
```

---

# 🔮 Prediction

The trained model predicts loan approval status for the test dataset:

```python
y_pred = model.predict(X_test)
```

The prediction result represents whether the loan is predicted to be:

```text
Approved
```

or

```text
Rejected
```

---

# 📊 Model Evaluation

## Accuracy

The project calculates model accuracy using:

```python
accuracy = accuracy_score(
    y_test,
    y_pred
)
```

The accuracy is displayed as a percentage:

```python
print(
    f"Accuracy : {accuracy * 100:.2f}%"
)
```

The actual accuracy depends on the contents and preprocessing of the dataset.

---

# 📉 Confusion Matrix

A confusion matrix is generated to understand the model's classification results.

```python
cm = confusion_matrix(
    y_test,
    y_pred
)
```

The matrix is visualized using Matplotlib.

### Confusion Matrix Helps Identify

* Correct loan approvals
* Correct loan rejections
* Incorrect approvals
* Incorrect rejections

This provides more information than accuracy alone.

---

# 👤 Single Loan Prediction

The project also demonstrates prediction for an individual sample from the dataset.

```python
sample_data = X.iloc[0:1]

prediction = model.predict(
    sample_data
)
```

The final result is displayed as:

```text
LOAN APPROVED
```

or:

```text
LOAN REJECTED
```

---

# 📊 Project Features

| Feature              | Description                                   |
| -------------------- | --------------------------------------------- |
| 📂 Dataset Loading   | Loads loan data from CSV                      |
| 🔍 Data Exploration  | Displays rows and data types                  |
| 🧹 Data Cleaning     | Handles missing numerical values              |
| 🗑️ ID Removal       | Removes `Loan_ID`                             |
| 🔢 Encoding          | Converts categorical data into numerical data |
| ✂️ Data Splitting    | 80% training / 20% testing                    |
| 🤖 ML Model          | Logistic Regression                           |
| 🔮 Prediction        | Predicts loan approval                        |
| 📈 Accuracy          | Calculates classification accuracy            |
| 📉 Confusion Matrix  | Evaluates prediction results                  |
| 👤 Sample Prediction | Demonstrates individual prediction            |

---

# 📁 Project Structure

```text
Loan-Approval-Prediction/
│
├── 📄 loan_data.csv
│
├── 🐍 loan_prediction.py
│
├── 📖 README.md
│
└── 📊 confusion_matrix.png
```

---

# 🚀 How to Run

## Step 1 — Clone the Repository

```bash
git clone https://github.com/abdullahghufran2001-hub/data-analysis-projects.git
```

## Step 2 — Open the Project

```bash
cd Loan-Approval-Prediction
```

## Step 3 — Install Dependencies

```bash
pip install pandas numpy matplotlib scikit-learn
```

## Step 4 — Add Dataset

Make sure:

```text
loan_data.csv
```

is available in the project folder.

## Step 5 — Update File Path

Change:

```python
file_path = r"C:/Users/user/Downloads/loan_data.csv"
```

to your local dataset location.

## Step 6 — Run the Program

```bash
python loan_prediction.py
```

---

# 📈 Expected Output

The program provides:

```text
================ FIRST 5 ROWS ================

Dataset Preview...


================ DATA TYPES ================

Column information...


================ MISSING VALUES ================

Missing value information...


================ MODEL ACCURACY ================

Accuracy : XX.XX%


================ CONFUSION MATRIX ================

[[... ...]
 [... ...]]


================ SINGLE PREDICTION ================

LOAN APPROVED
```

The actual accuracy and prediction depend on the dataset and train/test split.

---

# 🎯 Project Objectives

* Understand a real-world loan dataset.
* Perform basic data preprocessing.
* Handle missing numerical values.
* Convert categorical variables into numerical features.
* Build a binary classification model.
* Predict loan approval status.
* Evaluate model accuracy.
* Understand confusion matrices.
* Gain practical experience with Scikit-Learn.

---

# 🧠 Skills Demonstrated

### Python

* Pandas
* NumPy
* Matplotlib
* DataFrame operations

### Data Preprocessing

* Missing value handling
* Feature selection
* Categorical encoding
* Data transformation

### Machine Learning

* Supervised Learning
* Binary Classification
* Logistic Regression
* Train-Test Split
* Model Prediction

### Model Evaluation

* Accuracy Score
* Confusion Matrix

---

# 🔮 Future Improvements

The project can be improved by adding:

* 📊 Precision, Recall & F1-Score
* 📈 ROC-AUC evaluation
* 🔍 Feature importance/interpretation
* ⚖️ Class imbalance analysis
* 🤖 Random Forest
* 🌳 Decision Tree
* 🚀 XGBoost
* 🔧 Hyperparameter tuning
* 📊 Interactive dashboard
* 🌐 Streamlit prediction interface
* 👤 Custom user input for new loan applications

---

# 🌟 Key Learning

This project demonstrates the complete basic Machine Learning pipeline:

```text
Data
 ↓
Cleaning
 ↓
Preprocessing
 ↓
Feature Engineering
 ↓
Train-Test Split
 ↓
Model Training
 ↓
Prediction
 ↓
Evaluation
```

It provides practical experience in converting raw loan application data into a **Machine Learning classification solution**.

---

# 👨‍💻 Author

## Abdullah Ghufran

**BCA Student | Data Science & Data Analytics Enthusiast**

### Interests

`Python` `Data Science` `Data Analytics` `Machine Learning` `SQL` `Power BI` `Data Visualization`

---

# ⭐ Support

If you find this project useful, consider giving the repository a ⭐ **Star**.

> **Learn from Data. Build with Machine Learning. Predict with Intelligence. 🚀**

