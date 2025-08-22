import streamlit as st

def createPage(session_state):
	df = session_state.sensor_df

	st.subheader("📊 Combined Sensor Trends")
	st.write("Use this data to guide lesson planning and student experiments.")
	st.line_chart(df.set_index("Day"))