import streamlit as st
from utils.navigation import render_back_forth_nav
from utils.img_formatting import image_to_base64_str

#Module Structure
from shared_modules import all_modules

def createPage(session_state):
    st.set_page_config(page_title="What We Learned", layout="wide")

    render_back_forth_nav(session_state, current_module_key="whatwelearned", all_modules=all_modules, position="top")

    st.subheader("📝 Lesson 8: What We Learned")

    st.markdown("""
    Hi students! 👋
    
    Welcome to our lesson **What We Learned**.
                
    Over the past seven lessons, you’ve planted seeds, tested soils, used sensors, explored the SPRING dashboard, and learned how farmers make decisions based on data.
    
    Today, you will pull everything together, using your own experiment results and dashboard data to explain how soil properties, plant needs, and technology all work together to help crops grow.
    
    By the end of this lesson, you will be able to:
                
    - Explain how soil properties affect plant growth 🌱
    - Use dashboard data and experiment results as evidence 📊
    - Suggest soil and technology choices for a successful crop 🌾
    """)  

    #st.image("images/lesson-8.1.png", caption="", use_container_width=True)
    st.image("images/lesson-8.1.png", caption="", use_container_width=True)

    st.markdown("""
    ##### 📚 Key Vocabulary
    
    You will see these words today. Make sure you know them!
                
    - **Germination**: When a seed begins to grow into a plant
    - **Fertility**: The ability of soil to provide nutrients plants need
    - **Absorption**: How much water soil can take in
    - **Drainage**: How quickly water moves through soil
    - **Retention**: How well soil holds water
    - **Nutrients**: Elements in soil that plants need to grow
    - **Soil Texture Triangle**: Chart that classifies soil by sand, silt, and clay percentages
    - **Agricultural Technology**: Tools and systems (like sensors, dashboards, automated irrigation) that make farming more efficient

    ##### 🌟 Activity: Then and Now
    
    Look at two photos:
    - The first day you plant🌱
    - Our plant today 🌽
   
    Discuss or write down:
    - What helped our plant grow this far?
    - What challenges did it face?
    
    Your teacher will list ideas on the board and circle anything connected to soil or technology.

    ##### 📊 Activity: Dashboard & Soil Connection
                
    1. Open the SPRING dashboard and review the trends from our class plant.
    2. With a partner, compare:
        - Dashboard data trends
        - Day 6 soil test results
        - Day 7 soil classification
    3. Fill in the Plant Growth & Soil Connection Worksheet with:
        - Soil property
        - Effect on plant growth
        - Evidence from data or your own observations
    💡 Example: If your soil had slow drainage, you might connect that to a higher moisture level shown on the dashboard.

    ##### 📚 Activity: Plant Growth Stages Review
      
    Let’s quickly revisit the plant growth stages:
    1.	Germination → seed waking up, roots start growing
    2.	Seedling → first leaves appear, needs steady water and nutrients
    3.	Mature plant → preparing to produce seeds or crops, needs balanced conditions
    
    ##### 🌱 Activity: From Soil to Plant Growth – Data Connection
    """)  

    st.image("images/lesson-8.2.png", caption="", use_container_width=True)

    st.markdown("""
    - Check the trends from our class plant.
    - Compare your results:
        - Day 6 soil tests (texture, drainage, water retention)
        - Day 7 soil classification (sand, silt, clay)
        - Dashboard plant data (moisture, growth trends)
                
    - Fill in the Plant Growth & Soil Connection Worksheet with:
        - Soil property
        - Effect on plant growth at different stages (germination, seedling, mature)
        - Evidence from your soil tests, dashboard data, or observations
    
    💡 Example: Slow drainage soil → higher moisture on dashboard → seedlings risk root rot.
    """)
    with open("documents/lesson-8.1.pdf", "rb") as file:
        st.download_button(
            label="Download the Plant Growth & Soil Connection Worksheet(PDF)",
            data=file,
            file_name="lesson-8.1.pdf",
            mime="application/pdf",
            key="download-pdf-8"
        )
    
    st.markdown("""
    
    - Think like an advisor: In small groups, create a short action plan for a farmer who wants to grow the same crop in a new location. Include:
    - The soil properties they should check
    - Which tech tools (sensors, dashboard) would help most
    - How you’d monitor and adjust care over time

    ##### 📜 Wrap-Up
    Today you pulled together everything from Day 1 to now—plant needs and germination, soil testing and classification, and tech tools like sensors and the SPRING dashboard—to show how soil, plants, and data drive real farm decisions. Next, we’ll take it into the field to meet a farmer and see these tools in action so you can compare their data with ours and ask informed questions.

   
    Yay, you worked hard! It's game time now!

    #### 🎮 Activity: Crossword Puzzle

    Enjoy the puzzle solo or team up with a friend by creating an invite code inside the puzzle.
    Toggle the button to start the timer and reveal the board.
    You can restart or save your progress anytime using the options button in the top-left corner of the game.

    """)

    if st.toggle("🧩 Show Puzzle", value=False, key="toggle-puzzle8"):
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
            src="https://puzzleme.amuselabs.com/pmm/crossword?id=2fc927ce&set=6fd209c1b707d2ea7d9a73fff6d267b361bf1cc2d39099da8f73fd4fd346d1c1"
            aria-label="Puzzle Me Game">
        </iframe>
        """, unsafe_allow_html=True)

    st.markdown("""
    Here are the answers if you need them!
    """)

    if st.toggle("Show Answers", key="answers8"):
        st.markdown("""
        1. GERMINATION
        2. ABSORPTION
        3. SENSORS
        4. DRAINAGE
        5. NUTRIENTS
        6. FERTILITY
        7. CROP
        8. RETENTION
        9. LOAM
        10. SEEDLING
        11. TEXTURE
        """)

    
    st.markdown("---")
    st.success("Next up: Lesson 9 - Field Trip")

    render_back_forth_nav(session_state, current_module_key="whatwelearned", all_modules=all_modules, position="bottom")