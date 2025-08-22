import streamlit as st
from utils.navigation import render_back_forth_nav

# Define module structure
from shared_modules import all_modules  # or define inline if not importing

def createPage(session_state):
	st.set_page_config(page_title="Forecasting", layout="wide")

	render_back_forth_nav(session_state, current_module_key="forecast", all_modules=all_modules, position="top")

	st.title("🔮 Lesson 2: Forecasting")

	st.markdown("""
	**Forecasting** means predicting future events based on past data.

	### 🌾 In Agriculture:
	- Predict soil moisture trends to optimize irrigation
	- Anticipate frost or drought conditions
	- Improve crop yield predictions

	### 🔍 Methods:
	- Time series models
	- Linear regression
	- Moving averages

	""")

	st.markdown("---")
	st.success("🎉 You’ve completed Level 3!")

	render_back_forth_nav(session_state, current_module_key="forecast", all_modules=all_modules, position="bottom")