import streamlit as st
from utils.navigation import render_back_forth_nav

# Define module structure
from shared_modules import all_modules  # or define inline if not importing

def createPage(session_state):
	st.set_page_config(page_title="Data Analysis", layout="wide")

	render_back_forth_nav(session_state, current_module_key="analysis", all_modules=all_modules, position="top")

	st.title("📊 Lesson 1: Data Analysis")

	st.markdown("""
	In this module, you’ll learn how to **analyze sensor data** using basic statistics and graphs.

	### 📈 Key Concepts:
	- **Trends**: Changes over time (e.g. rising soil moisture)
	- **Averages**: Mean, median values
	- **Thresholds**: Alerts when values go beyond a range

	### 🛠️ Tools You’ll Use:
	- Pandas DataFrames
	- Line charts
	- Summary statistics

	""")

	st.line_chart({"Soil Moisture (%)": [45, 43, 41, 38, 50, 53, 48]})

	st.markdown("---")
	st.success("Final module: Forecasting environmental conditions")

	render_back_forth_nav(session_state, current_module_key="analysis", all_modules=all_modules, position="bottom")