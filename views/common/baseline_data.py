import streamlit as st
import numpy as np

def createPage(session_state):
	st.subheader("📉 Sensor Data Over the Week")

	df = session_state.sensor_df

	st.line_chart(df.set_index("Day"))
	st.write("Try analyzing relationships between soil moisture and sunlight!")