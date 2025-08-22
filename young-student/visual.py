import streamlit as st
import numpy as np

st.subheader("📊 Visual")
st.write("Let’s see how the plant is feeling today:")

df = st.session_state.sensor_df

soil_moisture = df["Soil Moisture (%)"].tolist()
optical_intensity = df["Optical Sensor (lux)"].tolist()

soil_level = int(np.clip(np.interp(soil_moisture[-1], [0, 100], [0, 10]), 0, 10))
light_level = int(np.clip(np.interp(optical_intensity[-1], [0, 500], [0, 10]), 0, 10))

def draw_bar(level):
    color = f"hsl({int(np.interp(level, [0, 10], [0, 120]))}, 85%, 45%)"
    return f"<span style='color:{color}; font-size: 24px; letter-spacing: 2px;'>" + ''.join(['█' if i < level else '░' for i in range(10)]) + "</span>"

col1, col2 = st.columns(2)
with col1:
    st.metric("💧 Soil Moisture", f"{soil_moisture[-1]}%")
    st.markdown(draw_bar(soil_level), unsafe_allow_html=True)

with col2:
    st.metric("☀️ Sunlight Level", f"{optical_intensity[-1]} lux")
    st.markdown(draw_bar(light_level), unsafe_allow_html=True)

st.success("😊 The plant is doing great!")

with st.container():
    st.markdown("<br>", unsafe_allow_html=True)  # Optional spacing
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("./images/happy-plant.png", width=200, caption="Happy Plant ☀️")