import streamlit as st
from utils.navigation import render_back_forth_nav

# Define module structure
from shared_modules import all_modules  # or define inline if not importing

def createPage(session_state):
    st.set_page_config(page_title="What is IoT?", layout="wide")

    # Render full navigation UI (pass the current module's key)
    render_back_forth_nav(session_state, current_module_key="iot", all_modules=all_modules, position="top")

    # Module content
    st.title("🌐 What is IoT?")
    st.markdown("""
    The **Internet of Things (IoT)** is a system of interconnected devices that can collect and exchange data.

    In agriculture, IoT helps monitor conditions like **soil moisture**, **temperature**, and **sunlight** using sensors connected to the internet.
    """)
    st.video("https://www.youtube.com/embed/6mBO2vqLv38")

    st.markdown("""
    **Why Technology in Agriculture?**
    > Using data helps reduce waste, increase yield, and protect the environment. Precision farming uses sensor data to water only when needed.

    **What is Internet?**
    > The Internet is a global network that connects millions of computers and devices.

    **What is Internet-of-Things (IoT)?**
    > A system where devices like soil sensors, weather stations, and drones collect and send data via the internet.

    📺 **Video: What is IoT?**
    """) # close previous markdown
    st.markdown(
        """
        <div style="position: relative; padding-bottom: 28.125%; height: 0; overflow: hidden; max-width: 50%;">
            <iframe 
                src="https://www.youtube.com/embed/6mBO2vqLv38" 
                frameborder="0" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                allowfullscreen 
                style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;">
            </iframe>
        </div>
        """,
        unsafe_allow_html=True
    )

    # enter markdown again
    st.markdown(
        """

        <br>

        **Introduction to IoT**
        >

        **Why LoRaWAN?**
        > LoRaWAN is a low-power, long-range wireless network. It's perfect for farms where WiFi or cell signals are weak.

        **Basics of LoRaWAN Communication**

        **Data Science Concepts (mean, variance, trends)**

        **Forecasting with Linear Regression**

        📘 Challenge: Can you write a mini-report using this data applying the linear regression techniques you learned?
        """,
        unsafe_allow_html=True
    )


    render_back_forth_nav(session_state, current_module_key="iot", all_modules=all_modules, position="bottom")