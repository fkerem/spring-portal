import streamlit as st
from utils.navigation import render_back_forth_nav
from utils.img_formatting import image_to_base64_str
from utils.link_preview import fetch_link_meta, render_link_card

#Module Structure
from shared_modules import all_modules

def createPage(session_state):
    st.set_page_config(page_title="Seed Germination & Planting", layout="wide")

    render_back_forth_nav(session_state, current_module_key="germination", all_modules=all_modules, position="top")
 
    st.subheader("🫘 Lesson 2: Seed Germination & Planting")

    st.markdown("""
    Hi students! 👋
                
    Welcome to our lesson  **Seed Germination & Planting**.

    Seeds may look small and simple, but inside each one is a tiny plant waiting for the right moment to start growing. This process is called germination, and it is the very first stage of a plant’s life. Today, we will explore what germination is, why it is important, how to plant a seed, and how to start tracking your plant’s growth using the SPRING system or your own manual soil moisture sensor.

    By the end of this lesson, you will be able to:

    - Explain what germination is and why it matters for plants 
    - Plant a seed correctly and prepare it for healthy growth 
    - Use a sensor or dashboard to start collecting soil moisture data 
    """)
    
    st.image("images/lesson-2.3.png", caption="Germination Process", use_container_width=True)

    st.markdown("""
    ##### 📚 Key Vocabulary

    Before we start, read through these words so you will recognize them during the activities.
    
    - **Germination**: When a seed begins to grow into a plant
    - **Seed**: A small object that can grow into a plant
    - **Soil**: Material that plants grow in
    - **Moisture**: Water in the soil
    - **Data**: Information we collect to track changes
    - **Sensor**: A tool that measures things like moisture and temperature

    ##### 🧠 Let's Think
    
    👉 What’s the very first thing a plant needs to wake up and start growing?
    
    >Share your ideas with the class or write them down. There is no wrong answer!

                
    ##### 📋 Activity: Planting Together
    """)
    url = "https://www.youtube.com/watch?v=Q1TwgE-qCsk&list=PLuMwvf1ttAYNGtSxeQTtoIQGokrGxxFXJ&pp=gAQB"
    meta = fetch_link_meta(url)
    render_link_card(meta, theme="auto", compact=True)

    st.markdown("""                        
    This is our SEED to SPRING YouTube channel and the Classroom Setup/Planting playlist.
    
    That playlist will help you:
    
    - Get your planting space ready
    - Follow step-by-step planting instructions
    - Learn tips to keep your seed healthy as it grows

    ##### 🪴 What You Need to Plant
    
    - Pot or container with soil
    - A seed (we use corn 🌽)
    - Water
    - Soil moisture sensor
    
    📢 Don't forget taking picture of your plant daily!

    ##### 🌱 Learn About Germination

    """)

    st.video("https://youtu.be/ro8Z9qIlWjM")
    # Toggle for transcript

    if st.toggle("Show Video Transcript", key="v1-transcript"):
        st.markdown("""
        > what is germination when a seed is sewn into moist soil it begins to grow this process is called germination it occurs in the following steps the seed coat splits tiny root grows downward and a shoot grows upward [Music] this produces a Seedling of a plant which ultimately grows into a new plant [Music] after some time the plant Bears flowers produce fruits and the fruits have seeds in them [Music] all seeds can germinate when sewn in moist soil under suitable conditions to produce new plants [Music] by natural or man-made processes these seeds are sewn into the soil again and that is how new plants are born foreign [Music] 
        """)

    st.markdown("""
    
    **This video explains**:
    
    - What happens inside a seed as it starts to grow
    - The conditions a seed needs to germinate
    - Why roots grow down and shoots grow up

    
    ##### 🗂️ Start Collecting Your Data
                
    If you are in class:
    - Watch how we use the SPRING Soil Moisture Sensor connected to the SPRING Gateway to measure soil moisture

    If you are at home:
    - Use your own manual soil moisture sensor, or
    - Check the dashboard Farm data

    If you are collecting your own data:
    - Use the Data Collection Worksheet to record soil moisture readings
    """)
   


    with open("documents/lesson-2.1.pdf", "rb") as file:
        st.download_button(
            label="Download the Data Collection Worksheet(PDF)",
            data=file,
            file_name="lesson-2.1.pdf",
            mime="application/pdf",
            key="download-pdf-2"
        )
    
    st.image("images/lesson-2.1.png", caption="Data Collection Worksheet", width=600)

    st.markdown("""
    
                
    ##### 📝 Activity: Planting Diagram

    Use the Planting Diagram Worksheet to show what is happening under the soil:
       
    - Label each step of the planting process in order
    - Draw the seed coat splitting, roots growing downward, and a small shoot growing upward
    - Use today’s vocabulary words in your labels so your diagram is clear and accurate
    - Add color so each part is easy to see.
    """)

    with open("documents/lesson-2.2.pdf", "rb") as file:
        st.download_button(
            label="Download the Planting Diagram(PDF)",
            data=file,
            file_name="lesson-2.2.pdf",
            mime="application/pdf",
            key="download-pdf-2.2"
        )

    
    st.image("images/lesson-2.2.png", caption="Planting Diagram", width=600)

    
    st.markdown("""
    ##### 📜 Wrap-Up
    
    - Today you planted your seed and learned how germination begins. You also started collecting data to track your plant’s growth. In our next lesson, we will explore how modern technology helps farmers monitor and care for plants.

    Yay, you worked hard! It's game time now!

    #### 🎮 Activity: Crossword Puzzle

    Enjoy the puzzle solo or team up with a friend by creating an invite code inside the puzzle.
    Toggle the button to start the timer and reveal the board.
    You can restart or save your progress anytime using the options button in the top-left corner of the game.

    """)

    if st.toggle("🧩 Show Puzzle", value=False, key="toggle-puzzle2"):
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
            src="https://puzzleme.amuselabs.com/pmm/crossword?id=e106278f&set=6fd209c1b707d2ea7d9a73fff6d267b361bf1cc2d39099da8f73fd4fd346d1c1"
            aria-label="Puzzle Me Game">
        </iframe>
        """, unsafe_allow_html=True)

    st.markdown("""
    Here are the answers if you need them!
    """)

    if st.toggle("Show Answers", key="answers2"):
        st.markdown("""
        1. TEMPERATURE
        2. STEM
        3. NUTRIENTS
        4. GERMINATION
        5. ROOT
        6. MOISTURE
        7. LEAF
        """)

                
    st.markdown("---")
    st.success("Next up: Lesson 3 - Modern Tech Apps")

    render_back_forth_nav(session_state, current_module_key="germination", all_modules=all_modules, position="bottom")