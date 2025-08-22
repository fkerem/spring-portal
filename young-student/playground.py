import streamlit as st
import numpy as np

st.subheader("🎮 Adjust the Conditions!")

st.write("Change the sunlight and moisture to see how your plant feels!")

df = st.session_state.sensor_df
soil_moisture = df["Soil Moisture (%)"].tolist()
optical_intensity = df["Optical Sensor (lux)"].tolist()

sm_input = st.slider("Soil Moisture (%)", 0, 100, soil_moisture[-1])
light_input = st.slider("Light Level (lux)", 0, 500, optical_intensity[-1])

sm_level = int(np.interp(sm_input, [0, 100], [0, 10]))
light_level = int(np.interp(light_input, [0, 500], [0, 10]))

def predict_health(sm, light):
    if sm >= 5 and light >= 5:
        return "🌱😊 The plant is happy!"
    elif sm < 3 or light < 3:
        return "🥀😟 The plant is sad!"
    else:
        return "🌾😐 The plant is okay."

st.markdown(f"**Your Prediction:** {predict_health(sm_level, light_level)}")