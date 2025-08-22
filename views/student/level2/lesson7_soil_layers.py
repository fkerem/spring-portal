import streamlit as st
from utils.navigation import render_back_forth_nav
from utils.img_formatting import image_to_base64_str

#Module Structure
from shared_modules import all_modules

def createPage(session_state):
    st.set_page_config(page_title="Soil Layers", layout="wide")

    render_back_forth_nav(session_state, current_module_key="soillayers", all_modules=all_modules, position="top")

    st.subheader("Lesson 7: Soil Layers")

    st.markdown("""
    
    Hi students! 👋
    
    Welcome to our lesson **Soil Layers**
                
    Yesterday, you tested how different soils absorb, hold, and drain water. You discovered that each soil type behaves differently but now it’s time to go deeper. Today, you will identify exactly what type of soil you’ve been testing and explore why that matters for growing different crops.
    
    By the end of this lesson, you will be able to:
                
    - Classify soil types using the Soil Texture Triangle
    - Explain how soil texture affects plant growth and crop choice
    - Connect your soil data to real-world farming decisions

    ##### 📚 Key Vocabulary
    
    You will use these terms in today’s activities:
    
    - **Absorption**: How much water something can take in
    - **Drainage**: How quickly water moves through it
    - **Texture**: How soil feels (gritty, sticky, smooth)
    - **Retention**: How well soil holds water
    - **Nutrients**: Elements in soil that plants need to grow
    - **Soil Texture Triangle**: A chart that classifies soil by the percentage of sand, silt, and clay
    - **Loam**: A balanced soil type with good drainage and nutrient retention
    - **Soil Type**: The category a soil falls into based on texture and properties
    - **Soil Profile**: The layers and characteristics of soil in a location

    ###### 🧩 Activity: Review Your Lesson 6 Results
    1. Look back at your Day 6 Soil Properties Observation Chart.
    2. Think about:
        - How did your soil feel?
        - How quickly did it drain?
        - Did it hold water for a long time or let it pass through quickly?
    3. These clues will help you when you place your sample on the Soil Texture Triangle.
    💡 Example: If your soil felt gritty and drained quickly, it might have a high sand content. If it felt sticky and held water, it might have more clay.

    ##### 🌱▲ Learn About Soil Texture Triangle
    """)

    st.video("https://youtu.be/Bn9ul9lxIdg")
    # Toggle for transcript

    if st.toggle("Show Video Transcript", key="v7-transcript"):
        st.markdown("""
        > -  Today, we're going to talk about soil. And you've probably noticed that there are many different kinds of soils. The soil near a beach looks and feels very different than the soil in a forest. And part of the reason for that difference is something called soil texture. Soil texture. So when soil is formed, different types of rock break down because of the wind and the rain and the weather. And they become differently sized particles. And the combination of these differently sized particles creates soil texture. So these differently sized particles can be broken down into three groups. We have sand. We have silt. And we have clay. Sand is made up of the larger and heavier particles of soil. Sand is around two millimeters. Two millimeters to 0.05 millimeters. Which is a 20th of a millimeter in diameter. And if it feels very gritty to touch. Clay on the other hand is the smallest particles of soil. It's around 0.002 millimeters and the smaller. That's a 500th of a millimeter. So really tiny. If you rubbed clay between your fingers, it would feel smooth, and you wouldn't be able to feel the individual particles of soil. And unlike sand, you can't even see clay's particles with a naked eye. Most people are familiar with sandy soils and clay soils, but silt is right in between. It's made of a particles between the size of clay and sand. So, it's between 0.05 millimeters and 0.002 millimeters. So when you think of silt imagine baking flour. It's powdery. Powdery. And it can be carried easily by wind and water. But soil is more complicated than just these three soil types. If you grabbed a handful of soil from outside your home, it would probably be a combination of all three soil types, along with some organic material. A soil's unique texture, that is it's combination of silt, sand, and clay, affects how plants will grow. And so gardeners often wanna know about their soil textures. They know what kinds of plants to grow in that area. This is where a helpful diagram called the soil texture triangle comes in. The soil texture triangle. The triangle allows us to place any soil sample into one of 12 different soil texture categories. The 12 different categories are broken up based on the percentage of silt, clay and sand in the soil. To see how this works, let's do an example. Let's say a gardener determined that a soil was 30% sand, 40% silt, and 30% clay. So, how can we figure out what kind of soil have? First, we need to pick a side of the triangle to start with. I'll start with sand. We know we have 30% sand. So, we go along the side of the triangle, until we find that 30% mark, right here. We want to draw a line from this point, to the side of the triangle, that this arrow is pointing to. The arrow is pointing towards the clay side. So we draw the line from the 30% sand mark, through the triangle, to the clay side. Like this. And by drawing this line, we already know that our soil sample will fall into a category along this line. So, it could be so silt loam, loam, clay loam, or clay. But to figure out exactly where it is, let's draw another line. Let's do silt. The soil has 40% silt. We'll draw our line through the triangle towards the sand side because of this arrow. So again, we do the same thing. We go along the percent silt's line. We find the 40% mark. And we're gonna draw a line from 40% to the other side of the triangle. And you can see when we draw that line, these two lines intersect at the clay loam point. But to double-check, let's draw a line from the 30% clay mark, to the other side of the triangle, like this. As you can see, these three lines, all intersected at the same point, right here in clay loam. So we know that we have clay loam. Notice that the percentage of clay, silt and sand, all add up to a total of 100%. We could have picked any two of these lines, just two, to find our answer. We don't need to draw three lines every time. Let's do another example. Let's say our gardener has another plot, with soil that contains 58% sand, 27% silt, and 15% clay. So, I'm gonna go along the percent sand part and find 58%. So that's pretty close to 60. And I'm gonna draw a line from 58%, to the other side of the triangle. Sometimes the example question, doesn't give us round numbers to work with. So when that's the case, I like to use a ruler or a straight edge, just to make sure that my lines are in the correct spot. Next I'm gonna use the 15% clay. So I find the 15% clay mark, and we draw a line for 15% to the other side of the triangle following the direction of the lines within the triangle. And we can see that our two lines intersect at this point. So, we have sandy loam. The gardener has these two plots clay loam and sandy loam. So when the gardener looks at her two plots, she might wanna take into account the different kinds of soil. Certain kinds of plants do better in clay loam soil while others would do better in the sandy loam soil. This is partly because clay soils, hold onto moisture for longer than sandy soils do. So the plants in the gardeners sandy loam plot, would do better if they had longer root systems to access water deeper in the ground. Or if they stored water inside themselves to access later. The gardener could use a gardening book or the internet to see what kinds of plants would do best in each of her two plots. Thanks for watching and happy soil identification.
        """)

    st.markdown("""
    📊 Activity: Use the Soil Texture Triangle
    1. Your teacher will give you the estimated sand, silt, and clay percentages for your sample.
    2. Find each percentage on the matching side of the Soil Texture Triangle.
    3. Follow the lines for each number until they intersect — that spot is your soil type.
    4. Write down your soil type on your chart.
    💡 Tip: Loam is often considered the “ideal” soil because it balances drainage, retention, and nutrient content — but different crops thrive in different soils.
    """)

    with open("documents/lesson-7.1.pdf", "rb") as file:
        st.download_button(
            label="Download Soil Texture Triangle(PDF)",
            data=file,
            file_name="lesson-7.1.pdf",
            mime="application/pdf",
            key="download-pdf-7.1"
        )

    
    st.image("images/lesson-7.1.png", caption="Soil Texture Triangle [1]", width=600)

    
    st.markdown("""
                
    ###### 💭 Activity: Think Like a Crop Planner
    
    Answer these questions in your notebook or discuss in a group:
    - Which crops would grow best in your soil type? Why?
    - If your soil type drains too fast, how could you help plants get enough water?
    - If your soil holds too much water, what could you do to prevent root problems?
    - How might the soil profile (layers beneath the surface) also affect plant growth?

    ###### 📜 Wrap-Up
    Today you learned how to use the Soil Texture Triangle to classify soil types and connect that information to real farm data. You also explored how soil type influences crop choices and farming strategies In the next lesson, we will shift from soil back to your plants, learning how to interpret plant growth data over time so you can catch problems early and adjust your care plan.
    
    Yay, you worked hard! It's game time now!

    #### 🎮 Activity: Crossword Puzzle

    Enjoy the puzzle solo or team up with a friend by creating an invite code inside the puzzle.
    Toggle the button to start the timer and reveal the board.
    You can restart or save your progress anytime using the options button in the top-left corner of the game.
 
    """) 

    if st.toggle("🧩 Show Puzzle", value=False, key="toggle-puzzle7"):
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
            src="https://puzzleme.amuselabs.com/pmm/crossword?id=7a55fb16&set=6fd209c1b707d2ea7d9a73fff6d267b361bf1cc2d39099da8f73fd4fd346d1c1"
            aria-label="Puzzle Me Game">
        </iframe>
        """, unsafe_allow_html=True)

    st.markdown("""
    Here are the answers if you need them!
    """)

    if st.toggle("Show Answers", key="answers7"):
        st.markdown("""
        1. SOILTYPE
        2. NUTRIENTS
        3. DRAINAGE
        4. LOAM
        5. RETENTION
        6. SOILPROFILE
        7. TEXTURE
        8. ABSORPTION
        """)

    
    st.markdown("---")
    st.success("Next up: Lesson 8 - What We Learned?")

    render_back_forth_nav(session_state, current_module_key="soillayers", all_modules=all_modules, position="bottom")