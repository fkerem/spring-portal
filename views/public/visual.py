import streamlit as st
import numpy as np

def createPage(session_state):
	df = session_state.sensor_df
	st.subheader("📊 Live demo of the field sensor data:")
	st.bar_chart(df.set_index("Day")[["Soil Moisture (%)"]])
	st.bar_chart(df.set_index("Day")[["Optical Sensor (lux)"]])