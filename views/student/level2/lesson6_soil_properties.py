import streamlit as st
from utils.navigation import render_back_forth_nav
from utils.img_formatting import image_to_base64_str

#Module Structure
from shared_modules import all_modules

def createPage(session_state):
    st.set_page_config(page_title="Soil Properties", layout="wide")

    render_back_forth_nav(session_state, current_module_key="soilproperties", all_modules=all_modules, position="top")

    st.subheader("⛰️ Lesson 6: Soil Properties")

    st.markdown("""
    Hi students! 👋 
    
    Welcome to our lesson **Soil Properties**
                 
    Not all soils are the same. Some act like a sponge and soak up every drop of water, while others let water run straight through without holding much. Some feel rough and sandy, others smooth and sticky.
    
    ❔Why does this matter? The type of soil a plant grows in affects how much water and nutrients it gets, and whether it stays healthy in hot, dry weather or survives after heavy rain. Farmers and scientists study soil properties to decide which crops will grow best in a given location.
    
    Today, you will test three types of soil; sandy, clay, and loam to see how they absorb, hold, and drain water. Then, you will connect what you find to real data from the Purdue farm to see how soil conditions play out in the real world.
    
    By the end of this lesson, you will be able to:
    - Describe the absorption, drainage, texture, retention, and nutrient potential of different soils
    - Record and compare your own soil test results in an organized chart
    - Match experimental results to real-world dashboard data and explain why it matters for plants and farming decisions
    """)  

    st.image("images/lesson-6.3.png", caption="Soil Properties", use_container_width=True)

    st.markdown("""
    ##### 📚 Key Vocabulary
    
    You will use these words throughout today’s activities.
    
    - **Absorption**: How much water something can take in.
    - **Drainage**: How quickly water moves through it.
    - **Texture**: How soil feels (gritty, sticky, smooth).
    - **Retention**: How well soil holds water.
    - **Nutrients**: Elements in soil that plants need to grow.

    ##### 🧪 Activity: Soil Feel Test
    
    Materials: Sandy soil, clay soil, loam soil, cups, water droppers, magnifying glasses, Soil Properties Observation Chart
    1. Feel Test: Rub a pinch of each soil between your fingers — is it gritty, sticky, or smooth? Record it.
    2. Water Test: Add the same amount of water to each soil sample. Time how long it takes to drain. Which drains fastest? Which holds water longest?
    3. Visual Check: Look closely at color, particle size, and smell. Use a magnifying glass for details. Record what you see.
    
    💡 Clue: Texture, drainage, and color give hints about how soil holds water and nutrients.
    """)
   
    with open("documents/lesson-6.1.pdf", "rb") as file:
        st.download_button(
            label="Soil Properties Observation Chart(PDF)",
            data=file,
            file_name="lesson-6.1.pdf",
            mime="application/pdf",
            key="download-pdf-6"
        )
    
    st.markdown("""

    ##### ⛰️ Learn About Different Soil Types                       
    """)

    st.video("https://youtu.be/3NK6ZosNxZo")
    # Toggle for transcript

    if st.toggle("Show Video Transcript", key="v6-transcript"):
        st.markdown("""
        > [Music] take notes as you watch this video and test your knowledge by taking the quiz at the end this video is sponsored in part by blue ring education the makers of Next Generation science methola and kids Health Net soil is a very important part of our planet it forms the top layer of the Earth surface soil can be different in different places but it generally has three main components small rock particles water and spaces that can be filled with air some soils also contain humus which is the remains of dead plants animals and other living things this addition makes the soil richer and more beneficial for plant growth different soils have varying amounts of each of these components but we'll get into that later soil is incredibly important to plants because it is their primary source of water minerals and nutrients which they need to grow this Rich environment doesn't just support plants it's also home to other living things including small animals fungi and microorganisms there are four four main types of soil each with their own special qualities mostly because of the size of the rock particles that make them up which affects the amount of water they can hold and the size of the airspaces they can also differ in the amount of humus they contain one type of soil is sandy soil or sand sandy soil has big particles like the sand you find at the beach these big particles mean that sandy soil can't hold on to water very well because the water just drains right [Music] through this is why sandy soil is often dry but the big spaces between the particles do allow a lot of air to move through sandy soil does not contain much [Music] humus another type is clay soil clay soil has very small particles these tiny particles pack closely together this makes it good at holding water but it doesn't let air through easily because of this clay soil can be hard for plant roots to move through like sand clay does not contain much [Music] humus then there is silt which has qualities that sit between those of Sandy and clay soils silt particles are finer than sand but bigger than clay making silt soil smooth to the touch this mediumsized particle composition allows silt soil to hold more water than sandy soil silt also has some humus usually more than sand or clay which provides minerals and nutrients to plants [Music] the last type of soil we will look at is lomy soil it's made of a mix of sand silt and also some clay particles this gives it the best qualities for growing plants it holds moisture but also drains well so it's not too wet or too dry lomy soil often contains lots of humus which helps the soil hold on to nutrients and moisture and makes the soil very good for growing [Music] plants so there you have it the four main types of soil sandy soil clay soil silt and lomy [Music] soil now that you know a bit more about them why not go outside and take a closer look at the soil around you pay attention to its characteristics is it gritty and quick to dry like sandy soil or does it hold water in shape easily like clay soil or maybe it's rich and crumbly and full of life like lomy soil thanks for learning let's see what you've learned by taking a quick soil quiz e e e e [Music] 
        """)

    st.markdown("""
    
    **This video explains**:
    
    - How sandy, clay, and loam soils look and feel different
    - Which soils drain water quickly and which ones hold onto it
    - Why farmers and gardeners mix soils to give plants the best chance to grow

    ##### 📊 Activity: Connect to Dashboard Data
    
    1. Open the Farm Data view in the SPRING dashboard.
    2. Look at soil moisture data from the Purdue farm for the current week.
    3. Compare your experiment results to what you see in the graphs.
    >👉 Which soil from your experiment behaves most like the soil conditions shown on the dashboard? Why do you think so?
               

    ##### 💭 Activity: Think Like a Farmer
    
    Answer these questions in writing or discuss them in a group:
    - Which soil would be the best home for which crop, and why?
    - What could go wrong if this soil got too much rain? What if it got almost no rain?
    - If you were the farmer, how would you use this information before planting?
    
    💡 Example: A farmer might choose crops that like drier soil for sandy ground, or install drainage systems for clay-heavy fields.

                
    ##### 📝 Wrap-Up
    Today you explored how soils differ in texture, drainage, and water retention — and how these differences impact plant growth and farming. By comparing your tests with the SPRING dashboard, you saw how soil conditions shape real decisions. Next time, you will track soil and plant data over time to spot patterns, predict problems, and plan solutions.    
    
    Yay, you worked hard! It's game time now!

    #### 🎮 Activity: Crossword Puzzle

    Enjoy the puzzle solo or team up with a friend by creating an invite code inside the puzzle.
    Toggle the button to start the timer and reveal the board.
    You can restart or save your progress anytime using the options button in the top-left corner of the game.

    """)

    if st.toggle("🧩 Show Puzzle", value=False, key="toggle-puzzle6"):
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
            src="https://puzzleme.amuselabs.com/pmm/crossword?id=9a9cb191&set=6fd209c1b707d2ea7d9a73fff6d267b361bf1cc2d39099da8f73fd4fd346d1c1"
            aria-label="Puzzle Me Game">
        </iframe>
        """, unsafe_allow_html=True)

    st.markdown("""
    Here are the answers if you need them!
    """)

    if st.toggle("Show Answers", key="answers6"):
        st.markdown("""
        1. NUTRIENTS
        2. RETENTION
        3. TEXTURE
        4. SANDY
        5. DRAINAGE
        6. ABSORPTION
        7. CLAY
        8. LOAM
        """)

    
    st.markdown("---")
    st.success("Next up: Lesson 7 - Soil Layers")

    render_back_forth_nav(session_state, current_module_key="soilproperties", all_modules=all_modules, position="bottom")