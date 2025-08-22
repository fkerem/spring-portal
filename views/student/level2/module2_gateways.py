import streamlit as st
from utils.navigation import render_back_forth_nav

# Define module structure
from shared_modules import all_modules  # or define inline if not importing

def createPage(session_state):
	st.set_page_config(page_title="Gateways", layout="wide")

	render_back_forth_nav(session_state, current_module_key="gateways", all_modules=all_modules, position="top")

	st.title("🌐 Lesson 2: Gateways")

	st.markdown("""
	**Gateways** act as bridges between local sensor networks (like LoRaWAN) and the internet.

	### 🔧 What They Do:
	- Receive data from sensors (via LoRa)
	- Forward it to cloud servers via Wi-Fi, Ethernet, or LTE
	- Enable real-time monitoring and analytics

	### 💡 Example
	A soil sensor sends a reading via LoRa. The gateway collects it and uploads it to a web dashboard farmers can view.

	""")

	st.image("https://store.rokland.com/cdn/shop/files/antennasshownfordemoonly_notincludedinsale.png?v=1703106537&width=610", use_container_width=False, caption="A LoRaWAN Gateway Device")

	st.markdown("---")
	st.success("Continue your journey in Level 3: Data Analysis")

	render_back_forth_nav(session_state, current_module_key="gateways", all_modules=all_modules, position="bottom")