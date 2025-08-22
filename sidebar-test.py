import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="SPRING Dashboard", layout="wide")

# Logos
st.markdown(
    """
    <div style="display: flex; align-items: center; gap: 20px; padding-bottom: 10px;">
        <img src="https://erc-assoc.org/sites/default/files/styles/large/public/2024-02/IoT4Ag_Logo_AS_Upd.png?itok=GzTOSWZC.png" alt="IoT4Ag Logo" style="height: 60px;">
        <img src="https://oatscenter.org/OATSCenter/Images/OATS.png" alt="OATS Logo" style="height: 60px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Purdue_Boilermakers_logo.svg/2560px-Purdue_Boilermakers_logo.svg.png" alt="Purdue Logo" style="height: 60px;">
    </div>
    """,
    unsafe_allow_html=True
)

# Simulated sensor data
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
soil_moisture = [45, 50, 47, 49, 55, 60, 58]         # %
optical_intensity = [200, 180, 190, 220, 240, 250, 245]  # lux

df = pd.DataFrame({
    "Day": days,
    "Soil Moisture (%)": soil_moisture,
    "Optical Sensor (lux)": optical_intensity
})

# Global variable for teacher's quiz questions
if "quiz_bank" not in st.session_state:
    st.session_state.quiz_bank = []

# Sidebar with user role and section
with st.sidebar:
    st.markdown("## 👥 Select User Role")
    role = st.selectbox("Choose your role:", ["👶 Young Student", "🧑‍🎓 High School", "👩‍🏫 Teacher", "🕵️‍♂️ Public Display"])

    options_by_role = {
        "👶 Young Student": ["Visual", "Raw Data", "Additional Graphs", "Playground", "Photos", "Learn", "Quiz"],
        "🧑‍🎓 High School": ["Visual", "Raw Data", "Additional Graphs", "Playground", "Photos", "Location", "Learn", "Quiz", "Exercises"],
        "👩‍🏫 Teacher": ["Visual", "Raw Data", "Additional Graphs", "Photos", "Location", "Learn", "Quiz Manager", "Standards", "Assessments", "Notes"],
        "🕵️‍♂️ Public Display": ["Visual", "Raw Data", "Additional Graphs", "Photos", "Location"]
    }

    icon_map = {
        "Visual": "bar-chart",
        "Raw Data": "file-earmark-text",
        "Additional Graphs": "graph-up",
        "Playground": "controller",
        "Photos": "image",
        "Location": "geo-alt",
        "Learn": "book",
        "Quiz": "question",
        "Quiz Manager": "pencil",
        "Standards": "clipboard-check",
        "Assessments": "check-circle",
        "Notes": "pencil-square",
        "Exercises": "file-earmark-check"
    }

    options = options_by_role[role]
    icons = [icon_map[opt] for opt in options]

    section = option_menu(
        menu_title=None,
        options=options,
        icons=icons,
        default_index=0,
        orientation="vertical",
        styles={
            "container": {"padding": "0!important", "background-color": "#0e1117"},
            "icon": {"color": "white", "font-size": "16px"},
            "nav-link": {
                "color": "white",
                "font-size": "14px",
                "text-align": "left",
                "margin": "5px 0",
                "--hover-color": "#44475a"
            },
            "nav-link-selected": {
                "background-color": "#373a40"
            }
        }
    )

# Replace tab structure with role + section logic
st.header(f"{role} View")

# External script(s) can be organized for better modularity
# Here, for simplicity, you can import or paste logic blocks for each role+section combination
st.write(f"This is the **{section}** section.")

# You can now migrate subtab contents into `if role == ... and section == ...` structure,
# similar to how it's already organized in the code you pasted earlier.
# Example:

if role == "👶 Young Student" and section == "Visual":
    st.subheader("📊 Visual")
    st.success("😊 The plant is doing great!")
    soil_level = int(np.clip(np.interp(soil_moisture[-1], [0, 100], [0, 10]), 0, 10))
    light_level = int(np.clip(np.interp(optical_intensity[-1], [0, 500], [0, 10]), 0, 10))

    def draw_bar(level):
        color = f"hsl({int(np.interp(level, [0, 10], [0, 120]))}, 85%, 45%)"
        return f"<span style='color:{color}; font-size: 24px; letter-spacing: 2px;'>" + ''.join(['█' if i < level else '░' for i in range(10)]) + "</span>"

    col1, col2 = st.columns(2)
    with col1:
        st.metric("💧 Soil Moisture", f"{soil_moisture[-1]}%")
        st.markdown(draw_bar(soil_level), unsafe_allow_html=True)

    with col2:
        st.metric("☀️ Sunlight Level", f"{optical_intensity[-1]} lux")
        st.markdown(draw_bar(light_level), unsafe_allow_html=True)

    st.image("./happy-plant.png", width=200, caption="Happy Plant ☀️")

elif role == "👶 Young Student" and section == "Raw Data":
    st.subheader("📄 Raw Sensor Data")
    st.dataframe(df)

# Repeat the rest similarly for each role and section using your existing content blocks.

