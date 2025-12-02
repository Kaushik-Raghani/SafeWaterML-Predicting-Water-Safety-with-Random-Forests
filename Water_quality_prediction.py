import streamlit as st
import numpy as np
import joblib

# ---------------- Load Model ---------------- #
# Make sure you trained and saved a RandomForest (or any classifier) before
# Example: joblib.dump(model, "water_quality_classifier.joblib")
model = joblib.load("random_forest_classifier(water).joblib")

# ---------------- Streamlit UI ---------------- #
st.set_page_config(page_title="Water Quality Prediction", layout="centered")
st.title("💧 Water Quality Prediction App")
st.write("This app uses a trained machine learning model to predict whether the water is **Safe** or **Not Safe** for drinking based on chemical parameters.")

st.markdown("---")

# ---------------- User Inputs ---------------- #
st.header("⚗️ Water Chemical Properties")

col1, col2 = st.columns(2)
with col1:
    aluminium = st.number_input("Aluminium (mg/L)", min_value=0.0, value=0.1)
    ammonia = st.number_input("Ammonia (mg/L)", min_value=0.0, value=0.05)
    arsenic = st.number_input("Arsenic (mg/L)", min_value=0.0, value=0.01)
    barium = st.number_input("Barium (mg/L)", min_value=0.0, value=0.2)
    cadmium = st.number_input("Cadmium (mg/L)", min_value=0.0, value=0.005)
    chloramine = st.number_input("Chloramine (mg/L)", min_value=0.0, value=1.0)
    chromium = st.number_input("Chromium (mg/L)", min_value=0.0, value=0.05)
    copper = st.number_input("Copper (mg/L)", min_value=0.0, value=0.2)
    flouride = st.number_input("Fluoride (mg/L)", min_value=0.0, value=0.7)
    bacteria = st.number_input("Bacteria (cfu/mL)", min_value=0.0, value=0.0)
with col2:
    viruses = st.number_input("Viruses (cfu/mL)", min_value=0.0, value=0.0)
    lead = st.number_input("Lead (mg/L)", min_value=0.0, value=0.01)
    nitrates = st.number_input("Nitrates (mg/L)", min_value=0.0, value=5.0)
    nitrites = st.number_input("Nitrites (mg/L)", min_value=0.0, value=0.1)
    mercury = st.number_input("Mercury (mg/L)", min_value=0.0, value=0.002)
    perchlorate = st.number_input("Perchlorate (mg/L)", min_value=0.0, value=0.01)
    radium = st.number_input("Radium (pCi/L)", min_value=0.0, value=1.0)
    selenium = st.number_input("Selenium (mg/L)", min_value=0.0, value=0.01)
    silver = st.number_input("Silver (mg/L)", min_value=0.0, value=0.05)
    uranium = st.number_input("Uranium (µg/L)", min_value=0.0, value=5.0)

st.markdown("---")

# ---------------- Prediction ---------------- #
if st.button("🔍 Predict Water Safety"):
    input_data = np.array([[aluminium, ammonia, arsenic, barium, cadmium, chloramine,
                            chromium, copper, flouride, bacteria, viruses, lead,
                            nitrates, nitrites, mercury, perchlorate, radium,
                            selenium, silver, uranium]])
    
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][prediction] * 100

    if prediction == 1:
        st.success(f"🟢 Safe for Drinking! (Confidence: {probability:.2f}%)")
    else:
        st.error(f"🔴 Not Safe for Drinking! (Confidence: {probability:.2f}%)")
