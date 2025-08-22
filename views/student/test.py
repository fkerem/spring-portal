import streamlit as st
from utils.navigation import render_module_nav
from shared_modules import all_modules

st.set_page_config(page_title="Learn", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    .dropdown-container {
        display: flex;
        gap: 2rem;
        margin-bottom: 1rem;
    }
    .dropdown {
        background-color: #e8f5e9;
        border-radius: 8px;
        padding: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .dropdown h4 {
        color: #2e7d32;
        margin-bottom: 0.5rem;
    }
    .stButton>button {
        background-color: #66bb6a;
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("## 🌱 Learn: Explore Levels")

from shared_modules import all_modules

pg = st.navigation([
    # Optional overview pages
    st.Page("pages/student/level1/level1.py", title="Level 1", icon="🌿"),
    st.Page("pages/student/level2/level2.py", title="Level 2", icon="🌳"),
    st.Page("pages/student/level3/level3.py", title="Level 3", icon="🍀"),

    # Modules (register for linking, but we'll hide from sidebar in CSS)
    st.Page("pages/student/level1/module1_iot.py", title="IoT Intro (L1M1)", icon="📚"),
    st.Page("pages/student/level1/module2_sensors.py", title="Sensors (L1M2)", icon="📚"),
    #st.Page("pages/student/level2/module1_lorawan.py", title="LoRaWAN (L2M1)", icon="📚"),
    st.Page("pages/student/level2/module1_modern_tech_apps.py", title="Modern Tech Apps in Agriculture (L2M1)", icon="📚"),
    st.Page("pages/student/level2/module2_gateways.py", title="Gateways (L2M2)", icon="📚"),
    st.Page("pages/student/level3/module1_analysis.py", title="Data Analysis (L3M1)", icon="📚"),
    st.Page("pages/student/level3/module2_forecasting.py", title="Forecasting (L3M2)", icon="📚"),
], position="hidden")

render_module_nav(current_module_key="iot", all_modules=all_modules)

pg.run()