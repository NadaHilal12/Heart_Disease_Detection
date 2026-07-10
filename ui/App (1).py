import streamlit as st

import pandas as pd

import joblib

import matplotlib.pyplot as plt

import sys
import os
sys.path.append(os.path.abspath(".."))
from rule_based_system.Rules import HeartExpert

from experta import Fact


st.set_page_config(page_title="Heart Disease App", layout="wide")

model = joblib.load("../ml_model/decision_tree_model.pkl")

st.title("❤️ Heart Disease Prediction System")
st.markdown("### Compare Machine Learning vs Expert System")

st.sidebar.title("⚙️ Model Info")
st.sidebar.write("Decision Tree + Expert System")

st.markdown("## 🧾 Patient Data")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.slider("Age", 20, 80)
    sex = st.selectbox("Sex", ["Female", "Male"])
    cp = st.selectbox("Chest Pain Type", [0,1,2,3])
    trestbps = st.number_input("Blood Pressure", 80, 200)

with col2:
    chol = st.number_input("Cholesterol", 100, 400)
    fbs = st.selectbox("Fasting Blood Sugar", [0,1])
    restecg = st.selectbox("Resting ECG", [0,1,2])
    thalach = st.number_input("Max Heart Rate", 60, 200)

with col3:
    exang = st.selectbox("Exercise Angina", [0,1])
    oldpeak = st.number_input("Oldpeak", 0.0, 6.0)
    slope = st.selectbox("Slope", [0,1,2])
    ca = st.selectbox("Number of Vessels", [0,1,2,3])

st.markdown("### Additional Info")
thal = st.selectbox("Thal", [0,1,2,3])

sex = 1 if sex == "Male" else 0

if st.button("🚀 Run Prediction", use_container_width=True):

    columns = [
        'age','sex','cp','trestbps','chol','fbs',
        'restecg','thalach','exang','oldpeak',
        'slope','ca','thal'
    ]

    ml_input = pd.DataFrame([[
        age, sex, cp, trestbps, chol, fbs,
        restecg, thalach, exang, oldpeak,
        slope, ca, thal
    ]], columns=columns)

    ml_pred = model.predict(ml_input)[0]
    ml_prob = model.predict_proba(ml_input)[0][1]

    engine = HeartExpert()
    engine.reset()

    expert_data = {
        "age": age,
        "chol": chol,
        "trestbps": trestbps,
        "exang": exang,
        "thalach": thalach,
        "oldpeak": oldpeak,
        "ca": ca,
        "cp": cp,
        "fbs": fbs
    }

    for key, value in expert_data.items():
        engine.declare(Fact(**{key: value}))

    engine.run()
    expert_pred = engine.get_result()

    tab1, tab2, tab3 = st.tabs(["🧠 ML Model", "👨‍⚕️ Expert System", "📊 Comparison"])

    with tab1:
        st.subheader("Machine Learning Result")
        st.metric("Prediction", "Disease" if ml_pred else "No Disease")
        st.progress(int(ml_prob * 100))
        st.write(f"Risk Score: **{ml_prob:.2f}**")

        fig, ax = plt.subplots()
        ax.bar(["No Disease", "Disease"], [1-ml_prob, ml_prob])
        st.pyplot(fig)

    with tab2:
        st.subheader("Expert System Result")
        if expert_pred:
            st.error("⚠️ High Risk Detected")
        else:
            st.success("✅ Low Risk")

    with tab3:
        st.subheader("Model Comparison")

        colA, colB = st.columns(2)

        with colA:
            st.metric("ML", "Disease" if ml_pred else "No Disease")

        with colB:
            st.metric("Expert", "Disease" if expert_pred else "No Disease")

        if ml_pred != expert_pred:
            st.warning("⚠️ Models Disagree")
        else:
            st.success("✅ Models Agree")

    st.markdown("---")

    if ml_pred or expert_pred:
        st.error("🚨 Final Result: High Risk")
    else:
        st.success("💚 Final Result: Low Risk")