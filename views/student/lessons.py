import streamlit as st
from utils.navigation import render_module_nav
from shared_modules import all_modules

import importlib
import inspect

def createPage(session_state):

    # Sync selected module from query param if it exists
    module_param = st.query_params.get("lesson")
    if module_param:
        for level, modules in all_modules.items():
            for m in modules:
                if m["key"] == module_param:
                    session_state.selected_module_path = f"views.{m['target']}"
                    session_state.selected_module_key = m["key"]

    st.set_page_config(page_title="Lessons", layout="wide", initial_sidebar_state="expanded")

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
        </style>
    """, unsafe_allow_html=True)

    st.markdown("## 🌱 Explore the Lessons")


    render_module_nav(session_state, all_modules=all_modules)

    # After rendering the Learn page content and dropdowns
    if "selected_module_path" in session_state:
        module_path = session_state.selected_module_path
        page_module = importlib.import_module(module_path)
        create_page_func = getattr(page_module, "createPage")
        sig = inspect.signature(create_page_func)

        #st.markdown("---")  # Optional separator
        #st.markdown("### 📘 Module Preview")

        if len(sig.parameters) == 1:
            create_page_func(session_state)
        else:
            create_page_func()



    """
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
    """