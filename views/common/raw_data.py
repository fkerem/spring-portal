import streamlit as st
import pandas as pd

def createPage(session_state):
	df = session_state.sensor_df

	st.subheader("📄 Raw Sensor Data (Week)")
	st.dataframe(df)
	st.download_button("📥 Download CSV", df.to_csv(index=False).encode(), "sensor_data.csv")