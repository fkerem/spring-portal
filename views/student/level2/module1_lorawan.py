import streamlit as st
from utils.navigation import render_back_forth_nav

# Define module structure
from shared_modules import all_modules  # or define inline if not importing

def createPage(session_state):
	st.set_page_config(page_title="LoRaWAN Basics", layout="wide")

	render_back_forth_nav(session_state, current_module_key="lorawan", all_modules=all_modules, position="top")

	st.title("📡 Lesson 1: LoRaWAN Basics")

	st.markdown("""
	**LoRaWAN** stands for *Long Range Wide Area Network*.

	It is a wireless communication protocol designed for:

	- Low power consumption 🌱
	- Long range transmission 📶
	- Connecting many low-data-rate sensors 📡

	### 📘 Use in Agriculture
	- Send data from fields up to 15 km away
	- Devices like soil sensors or weather stations can operate on batteries for years

	""")

	st.image("https://www.thethingsnetwork.org/docs/_images/LoRaWAN.svg", use_container_width=True, caption="LoRaWAN Communication Structure")

	st.markdown("---")
	st.success("Next up: Module 2 - Gateways and Their Role")

	render_back_forth_nav(session_state, current_module_key="lorawan", all_modules=all_modules, position="bottom")