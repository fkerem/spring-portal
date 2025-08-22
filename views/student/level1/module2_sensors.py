import streamlit as st
from utils.navigation import render_back_forth_nav
from utils.img_formatting import image_to_base64_str

# Define module structure
from shared_modules import all_modules  # or define inline if not importing

def createPage(session_state):
    # ─── PAGE CONFIG ──────────────────────────────────────────────
    st.set_page_config(page_title="Using Sensors", layout="wide")

    # ─── MODULE NAVIGATION UI ─────────────────────────────────────
    render_back_forth_nav(session_state, current_module_key="sensors", all_modules=all_modules, position="top")

    # ─── MODULE CONTENT ───────────────────────────────────────────
    st.title("🔎 Lesson 2: Using Sensors")

    st.markdown("""
    Sensors are electronic devices that detect and measure physical properties such as:

    - 🌡️ **Temperature**
    - 💧 **Soil Moisture**
    - ☀️ **Light Intensity**
    - 🌬️ **Humidity**
    - 📍 **Location (GPS)**

    These sensors play a key role in **smart agriculture**, where real-time data helps farmers make informed decisions.

    ### 💡 Example Use Case
    Imagine a soil moisture sensor placed in the ground that detects when the soil is dry. It sends a signal to the system, which automatically turns on irrigation — saving water and boosting crop health.
    """)

    se01_b64 = image_to_base64_str("images/se01-lb.jpg")

    st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="data:image/png;base64,{se01_b64}" width="300"><br>
                <div><strong>SE01-LB: Soil Moisture & Temperature Sensor [1]</strong></div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.success("Up next: Module 3 - Connecting Sensors with the Internet (in Level 2)")

    render_back_forth_nav(session_state, current_module_key="sensors", all_modules=all_modules, position="bottom")