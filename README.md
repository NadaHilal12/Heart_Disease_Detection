# ❤️ Heart Disease Detection System

## 📌 Overview

This project predicts heart disease using two approaches:

* 🧠 Machine Learning (Decision Tree Classifier)
* 👨‍⚕️ Rule-Based Expert System (Experta)

The goal is to compare prediction performance and interpretability.

---

## 🎯 Why This Project Matters

Combining machine learning with expert systems improves decision support by balancing accuracy and explainability.

---

## 📊 Dataset

The dataset includes:

* Age
* Cholesterol
* Blood Pressure
* Max Heart Rate
* Chest Pain Type
* Other clinical features

### Data Preprocessing

* Removed duplicates  
* Handled missing values  
* Removed outliers (IQR method)  
* Applied normalization  

---

## ⚙️ Project Workflow

### 1️⃣ Data Preprocessing
* Cleaning
* Missing values handling
* Outlier removal

---

### 2️⃣ Data Visualization
* Histograms  
* Boxplots  
* Correlation heatmap  

---

### 3️⃣ Expert System
Implemented using Experta.

Features:
* 10+ rules  
* Medical logic decisions  
* Risk scoring  

---

### 4️⃣ Machine Learning Model
* Decision Tree Classifier  
* GridSearchCV for tuning  

#### Evaluation Metrics

* Accuracy: 83.019%  
* Precision: 90.625%  
* Recall: 82.857%  
* F1-score: 86.567%  

---

### 5️⃣ Model Comparison

| Model          | Type             | Strength              | Weakness              |
|----------------|------------------|-----------------------|-----------------------|
| Decision Tree  | Machine Learning | High accuracy         | Sensitive to data     |
| Expert System  | Rule-Based       | Explainability        | Limited flexibility   |

---

## 🧠 Results

* Decision Tree achieved higher accuracy  
* Expert System provided interpretable reasoning  
* Combining both improves reliability  

---

## 🖥️ User Interface

Built with Streamlit:

* User input form  
* ML prediction  
* Expert system diagnosis  
* Risk score visualization  
* Model comparison  

---

## 🚀 How to Run

### 1. Install dependencies

pip install -r requirements.txt


### 2. Run the app

streamlit run ui/app.py

---

## 🧠 Final Insight

Combining Machine Learning with Expert Systems creates a hybrid solution that balances predictive power with interpretability, making it suitable for real-world medical applications.
