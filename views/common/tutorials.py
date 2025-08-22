import streamlit as st

def createPage(session_state=None):
    st.subheader("🎥 IoT4Ag Spring Tutorial Videos")
    st.write("Get started with your IoT4Ag journey using these quick and informative tutorials:")

    videos = [
        ("Choosing Pot & Soil", "https://www.youtube.com/watch?v=Q1TwgE-qCsk"),
        ("Choosing Seeds", "https://youtube.com/watch?v=pOzvgP2Xo3U"),
        ("Gateway Connection", "https://youtu.be/tJQfac8_WnI"),
        ("Sensor Setting", "https://youtu.be/k58u59hUNHY"),
        ("Setting the Pod", "https://youtu.be/1yUj0yPxQHg"),
        ("Planting the Seed", "https://youtube.com/watch?v=QwZk4ZHlJcA"),
        ("Sensor Placement", "https://youtu.be/5W27X5b0tQ0"),
        ("Question For You", "https://youtu.be/dFI0a9dRKpw"),
    ]

    for title, url in videos:
        st.markdown(f"### {title}")
        st.video(url)
        st.markdown("---")