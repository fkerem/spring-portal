import streamlit as st
from utils.navigation import render_back_forth_nav
from utils.img_formatting import image_to_base64_str
from utils.link_preview import fetch_link_meta, render_link_card

#Module Structure
from shared_modules import all_modules

def createPage(session_state):
    st.set_page_config(page_title="Farm Data Comparison", layout="wide")

    render_back_forth_nav(session_state, current_module_key="datacomparison", all_modules=all_modules, position="top")

    st.subheader("🚜🌾 Lesson 5: Farm Data Comparison")

    st.markdown("""
    
    Hi students! 👋
    
    Welcome to our lesson  **Farm Data Comparison**.
    
    Today, you will compare real-time data from two farms; Purdue’s corn field in Indiana, and a New York apple orchard to see how location and weather can create totally different growing conditions. You will then connect what you see on the SPRING dashboard to real news events, and think about how those differences affect farming decisions.
     
    By the end of this lesson, you will be able to:
    
    - Compare environmental data from two farms in different states 
    - Connect real-world events to data trends on the dashboard  
    - Suggest farming decisions based on location-specific challenges 
    """)  

    st.image("images/lesson-5.1.png", caption="Data Comparison", use_container_width=True)

    st.markdown("""
    ##### 📚 Key Vocabulary
    You will use these terms as you work today:
    
    - **Impact**: The effect of an event or condition on crops.
    - **Comparison**: Looking at similarities and differences.
    - **Environmental Factor**: A natural condition (temperature, rainfall, frost) that affects plant growth.
    - **Decision-Making**: Choosing an action based on information or data.

    ##### 📰 Activity: Read the Headlines
    
    """)
    
    url = "https://www.brownfieldagnews.com/news/dry-conditions-impacting-corn-as-pollination-approaches/"
    meta = fetch_link_meta(url)
    render_link_card(meta, theme="auto", compact=True)

    url = "https://newyorkagconnection.com/news/new-york-apple-orchards-feel-the-effects-of-may-frost"
    meta = fetch_link_meta(url)
    render_link_card(meta, theme="auto", compact=True)
    # Websites links and preview should be here.

    st.markdown("""
   
    Start by reading these two news stories:
    1. Late Spring Frost Damages Apple Orchards in New York
    2. Purdue Corn Fields Show Steady Growth This Season
    
    As you read:
    - Underline or note any environmental factors mentioned; frost, rainfall, temperature changes, drought, etc.
    - Think about the impact those conditions might have on each crop.
    
    💡 Tip: Apple trees and corn plants respond very differently to changes in temperature and moisture.

    
    ##### 📊 Activity: Dashboard Data Comparison
    1. In the SPRING dashboard, open Farm Data.
    2. Select the Purdue Corn Field dataset for the same week mentioned in the news.
    3. Select the New York Apple Orchard dataset for that same week.
    4. Look closely at the graphs for:
        - Temperature 🌡️
        - Soil Moisture 💧
        - Rainfall 🌧️
    
    Write down:
    - Two key differences you notice between the farms.
    - One similarity they share.
    
    💡 Example: You might notice that the apple orchard had a sharp temperature drop while the corn field stayed steady or that one location had much more rainfall than the other.

    ##### 🔍 Activity: Connect the Dots
    
    Now link the news stories to the dashboard data:
    - Does the dashboard confirm the conditions mentioned in the article?
    - Does the data reveal anything the news didn’t cover?
    - Can you see the impact of the environmental factors in the graphs?
    >Write a short explanation connecting at least one piece of news to one piece of dashboard data.

    ##### 🚜 Activity: Decision Time - Be the Advisor
    """)  

    st.image("images/lesson-5.2.png", caption="Decision-Making", use_container_width=True)

    st.markdown("""        
    Imagine you are:
    - A farmer in the New York apple orchard or
    - A farmer in the Purdue corn field or
    - A scientist advising both farms
    
    For each location, answer:
    1. What action would you take? (e.g., irrigate, harvest early, add frost protection)
    2. Why is this the best choice based on the data?
    3. How could it reduce risk or improve crop health?
    
    💡 Make it clear enough so someone else could follow your reasoning even if they didn’t see the dashboard.

    ##### 📜 Wrap-Up
    Today you saw how the same week can tell two very different stories when comparing farms in different locations. You practiced comparison, identified environmental factors, and applied real data to make informed decisions just like a farmer or agricultural scientist would. In the next lesson, we will turn our focus underground and explore soil properties — testing how different soils absorb, hold, and drain water, and what that means for plant health.
    
    Yay, you worked hard! It's game time now!

    #### 🎮 Activity: Crossword Puzzle

    Enjoy the puzzle solo or team up with a friend by creating an invite code inside the puzzle.
    Toggle the button to start the timer and reveal the board.
    You can restart or save your progress anytime using the options button in the top-left corner of the game.

    """)

    if st.toggle("🧩 Show Puzzle", value=False, key="toggle-puzzle5"):
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
            src="https://puzzleme.amuselabs.com/pmm/crossword?id=184d79fe&set=6fd209c1b707d2ea7d9a73fff6d267b361bf1cc2d39099da8f73fd4fd346d1c1"
            aria-label="Puzzle Me Game">
        </iframe>
        """, unsafe_allow_html=True)

    st.markdown("""
    Here are the answers if you need them!
    """)

    if st.toggle("Show Answers", key="answers5"):
        st.markdown("""
        1. FROST
        2. TEMPERATURE
        3. DECISIONMAKING
        4. IMPACT
        5. ADVISOR
        6. ORCHARD
        7. COMPARISON
        """) 

    
    st.markdown("---")
    st.success("Next up: Lesson 6 - Soil Properties")

    render_back_forth_nav(session_state, current_module_key="datacomparison", all_modules=all_modules, position="bottom")