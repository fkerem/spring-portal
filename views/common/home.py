import streamlit as st
from utils.img_formatting import image_to_base64_str

def createPage():
    st.markdown("## 👋 Welcome to the SPRING Portal")
    st.markdown("""
    The **SPRING Portal** is an interactive learning environment designed for students, teachers, and public audiences to explore agricultural sensor data, conduct hands-on experiments, and access educational content developed through the IoT4Ag initiative.

    """)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""

        Use the sidebar to:
        - 📚 Navigate to **Lessons** and **Module**
        - 🌾 Explore real-time **Farm Data** and **Weather Data**
        - 🪴 Monitor **Pot Data** from classroom sensors
        - 🎯 Watch **Tutorials** or try the interactive **Playground**

        ### 🌱 What can you do here?

        - Access level-based learning lessons
        - Visualize soil sensor, weather, and pot data
        - Download educational materials and raw data
        - Explore data from multiple farms and a weather station
        """)

    with col2:
        #st.video("https://www.youtube.com/embed/ZGJcF7oyUIQ")  # Replace with actual video
        st.video("https://youtu.be/lFApWFH5u1o")
        #st.video("https://www.youtube.com/embed/lFApWFH5u1o")
        st.markdown("⬆️ Watch a quick overview of how to use the portal!")

    st.markdown("---")
    st.markdown("### 🗺️ Sitemap by User Role")

    sitemap = {
        "🧑‍🎓 Student": {
            "Home": "Landing page with tutorials and resources.",
            "Lessons": "Hands-on lessons designed around real sensor data.",
            "Pot Data": "Classroom corn pot dashboard with live sensor readings.",
            "Farm Data": "Live and historical soil and light sensor data from multiple farms.",
            "Weather Data": "Weather station data and environmental conditions.",
            "Photos": "Farm images to support data understanding.",
            "Location": "Interactive map showing sensor locations.",
            "Tutorials": "Short guides and walkthroughs.",
            "Playground": "Modify and experiment with sensor data freely."
        },
        "👩‍🏫 Teacher": {
            "Home": "Landing page with tutorials and teaching resources.",
            "Module": "Comprehensive teacher module guide with lesson plans.",
            "Pot Data": "Classroom corn pot dashboard for instructional use.",
            "Farm Data": "Use real-time farm data in the classroom.",
            "Weather Data": "Weather station data for lesson integration.",
            "Photos": "Visual documentation for teaching context.",
            "Location": "Map-based sensor tracking.",
            "Tutorials": "How-to videos for educators.",
            "Notes": "Save and organize teaching notes."
        },
        "🕵️‍♂️ Public Audience": {
            "Home": "Landing page with an overview of the portal.",
            "Pot Data": "Public view of classroom corn pot sensors.",
            "Farm Data": "Explore public agricultural sensor data.",
            "Weather Data": "Public weather station information.",
            "Photos": "Farm images and outreach visuals.",
            "Location": "Sensor deployment map.",
            "Tutorials": "Introductory videos about the platform."
        }
    }

    for role, pages in sitemap.items():
        with st.expander(f"{role} Sitemap"):
            for page, description in pages.items():
                st.markdown(f"**{page}** – {description}")

    st.markdown("---")
    st.markdown("""
    <div style='text-align:center; font-size:0.9rem;'>
        Need help? Contact your instructor or visit <a href='https://iot4ag.us' target='_blank'>iot4ag.us</a>
    </div>
    """, unsafe_allow_html=True)