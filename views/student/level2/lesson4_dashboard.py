import streamlit as st
from utils.navigation import render_back_forth_nav
from utils.img_formatting import image_to_base64_str
from utils.link_preview import fetch_link_meta, render_link_card

#Module Structure
from shared_modules import all_modules

def createPage(session_state):
    st.set_page_config(page_title="Exploring the Dashboard", layout="wide")

    render_back_forth_nav(session_state, current_module_key="dashboard", all_modules=all_modules, position="top")

    st.subheader("🗺️ Lesson 4: Exploring the Dashboard")

    st.markdown("""
    Hi students! 👋
 
    Welcome to our lesson **Exploring the Dashboard**.
                            
    Farmers today don’t just walk through their fields to check on crops. They also use digital tools to see exactly what’s happening, even from miles away. One of those tools is the SPRING dashboard. It gathers information from sensors, weather stations, and historical records, then turns it into graphs and charts that can guide important decisions.
    
    Today, you will learn how to navigate the SPRING dashboard and explore its features so you can find, understand, and use the data that matters most.

    By the end of this lesson, you will be able to:
    - Navigate the main sections of the SPRING dashboard  
    - Identify key data features such as trends, variables, and weather information 
    - Use dashboard data to make informed farming decisions 
    """)
    
    st.image("images/lesson-4.2.png", caption="Exploring the Dashboard", use_container_width=True)

    st.markdown("""
    ##### 📚 Key Vocabulary
    
    You will see these words in the dashboard and today’s activities:
                
    - **Weather Station**: Collects local weather information like temperature, humidity, and rainfall
    - **Trend**: A pattern in data over time (e.g., soil moisture slowly going down each day)
    - **Variable**: Something that can change and be measured, like soil moisture or air temperature
    - **Data Interpretation**: Understanding what the numbers and graphs mean in context

    ##### 🖱️ Activity: Guided Dashboard Tour
                
    1. Go to the Home Page in your SPRING dashboard 🏠.
    2. Watch the Dashboard Navigation Video to see how the site is organized.
    3. Explore the left-hand menu, including:
        - Farm Data:  Real-time measurements from sensors in the field
        - Weather Station: Local temperature, rainfall, humidity, and more
        - Historical Data: Past data you can compare to today’s conditions by changing date variables on the graphs
    4. Make a note of where each section is located. You will use them again later.
    
    💡 Tip: Think of the dashboard as a map of your farm’s health. Each section tells part of the story.

    ##### 🔍 Activity: Data Detective
    
    Your job today is to look for clues hidden in the dashboard.
    - Check today’s readings, look for patterns in the past few days, and decide what a farmer should do next.
    - Use your Detective Sheet to record your discoveries so other detectives can review your case.    
    """)

    st.image("images/lesson-4.1.png", caption="Dedective Sheet", width=600)

    with open("documents/lesson-4.1.pdf", "rb") as file:
        st.download_button(
            label="Download the Detective Sheet(PDF)",
            data=file,
            file_name="lesson-4.1.pdf",
            mime="application/pdf",
            key="download-pdf-4.1"
        )


    st.markdown("""
                
    ##### 🎮 Activity: Playground Exploration
    
    Hi! In the left sidebar, click Playground. Your mission:
    
    1. Switch the date range to compare short-term vs. long-term data.
    2. Pick two different variables and see how they change over the same time period.
    3. Write down one observation or question the data makes you think about.
   
    📝 Wrap-Up
    Today you explored the SPRING dashboard, learned how to find important information, and practiced making decisions based on real farm data. You also saw how trends, variables, and weather information can all connect to influence farming choices. In the next lesson, we’ll compare real-time data from two very different farms — a Purdue corn field and a New York apple orchard — to see how location and weather can lead to very different strategies.
    
    Yay, you worked hard! It's game time now!

    #### 🎮 Activity: Crossword Puzzle

    Enjoy the puzzle solo or team up with a friend by creating an invite code inside the puzzle.
    Toggle the button to start the timer and reveal the board.
    You can restart or save your progress anytime using the options button in the top-left corner of the game.

    """)

    if st.toggle("🧩 Show Puzzle", value=False, key="toggle-puzzle4"):
        st.markdown("""
        <style>
        .custom-iframe {
            height: 800px;
            width: 100%;
            border: none;
            display: block;
            margin: 0 auto;
        }
        </style>

        <iframe class="custom-iframe"
            allow="web-share; fullscreen"
            sandbox="allow-scripts allow-same-origin"
            loading="lazy"
            src="https://puzzleme.amuselabs.com/pmm/crossword?id=5bf68a26&set=6fd209c1b707d2ea7d9a73fff6d267b361bf1cc2d39099da8f73fd4fd346d1c1"
            aria-label="Puzzle Me Game">
        </iframe>
        """, unsafe_allow_html=True)

    st.markdown("""
    Here are the answers if you need them!
    """)

    if st.toggle("Show Answers", key="answers4"):
        st.markdown("""
        1. DASHBOARD
        2. WEATHERSTATION
        3. OBSERVATION
        4. GRAPH
        5. TREND
        6. DATA
        7. INTERPRETATION
        """)

    st.markdown("---")
    st.success("Next up: Lesson 5 - Farm Data Comparison")

    render_back_forth_nav(session_state, current_module_key="dashboard", all_modules=all_modules, position="bottom")