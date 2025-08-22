import streamlit as st
from utils.navigation import render_back_forth_nav
from utils.img_formatting import image_to_base64_str

# Define module structure
from shared_modules import all_modules  # or define inline if not importing

def createPage(session_state):
    st.set_page_config(page_title="What Do Plants Need to Grow?", layout="wide")

    render_back_forth_nav(session_state, current_module_key="plantneeds", all_modules=all_modules, position="top")
 
    st.subheader("🌱 Lesson 1: What Do Plants Need to Grow?")

    st.markdown("""
    Hi students! 👋

    Welcome to our lesson **What Do Plants Need to Grow?**.

    🌻 Plants may look simple, but they have specific needs to stay alive, healthy, and strong. In this lesson, we will explore the six basic needs of plants, and why each one is important.
    
    By the end of this lesson, you will be able to:

    - Name the six things plants need to grow 
    - Explain why each one is important 
    - Predict what happens when a plant doesn’t get one of its needs 
               
    ##### 📚 Key Vocabulary

    Before we start, read through these words. You will see them throughout today’s activities.
    - **Light☀️**: The energy from the sun that helps plants make their own food.
    - **Water💧**: Keeps plants alive and helps move nutrients to where they are needed.
    - **Air💨**: Plants “breathe in” carbon dioxide from the air to grow.
    - **Temperature🌡️**: How warm or cool it is, which affects how fast plants grow.
    - **Space🌱**: Room for roots and leaves to stretch and spread out.
    - **Nutrient🪴**: Natural substances in the soil that feed plants and help them grow.
    - **Plant health🩺**: How strong, green, and healthy a plant looks.
    - **Growth📈** The process of a plant getting bigger over time.

    ##### 🎥 Watch & Think
    """)
    
    st.video("https://youtu.be/u46A0WKp2nk")
    # Toggle for transcript

    if st.toggle("Show Video Transcript", key="v1-transcript"):
        st.markdown("""
        > [Music] how do plants grow for kids plants are everywhere there are many different kinds of plants that grow all around the world on every single continent today we are going to talk about the things that plants need in order to grow are you the same height as you were when you were one year old how about when you were five every year you probably grow a little taller and get a little bigger which is awesome because that means you are growing whether it is human life animal life or plant life all living things need certain things to survive be healthy and grow so what helps plants grow plants need four main things in order to grow just for fun let's call them the core four the core four are soil sunlight air and water let's talk about each of these things individually and then see how they all work together to help plants thrive first up is soil many of the nutrients plants need are found in soil these nutrients include nitrogen phosphorus and potassium and what do these do well nitrogen helps make a plant's leaves green phosphorus helps create large flowers and a strong healthy root system and potassium helps a plant fight off diseases all of these nutrients help keep the soil healthy and create the perfect place for a plant to grow soil also gives support to plants and prevents them from falling over next up is sunlight the sun is a super important part of plant growth plants use the energy from the sun to make their own food here is an interesting fact this food making process is called photosynthesis talk about a big word let's say it again just for fun photo synthesis even though sunlight is important it has to be the right amount too much sun and a plant may wither and die too little and it may stop growing plants receive carbon dioxide or co2 from the air which helps with photosynthesis that means that the co2 molecules in the air work with the sun to help plants make their own food which in turn helps the plant to grow here is another interesting fact during photosynthesis plants release oxygen or o2 into the air this oxygen is breathed in by animals including humans like you which is why plants are a vital part of keeping our planet healthy and alive last is our good old friend water which is also necessary to keep plants alive and help them to grow the water a plant receives helps bring the nutrients found in the soil to the plant through their roots stems and into their leaves and like sunlight it is important for a plant to get just the right amount of water it is pretty cool to see how soil sunlight air and water all work together to help plants grow were you surprised that plants need some of the same things that you need it is pretty cool to compare and contrast right beyond the core 4 there are two other things that help plants stay healthy and strong the first is temperature most plants grow well in warm daytime temperatures and cooler nighttime temperatures if it is too hot plants will dry up and die if it is too cold they will freeze second is space plants need enough room to grow into their full size without this room plants will not be able to develop deep enough roots to allow them to grow the way they are meant to and if they are overcrowded they might suffer from disease or not receive enough air we have learned a lot about plants today are you ready to review let's do it fill in the blank the process that plants use to make food is called blank photosynthesis true or false a plant can never have too much or too little water false plants need just the right amount of water in order to stay healthy this amount depends on the type of plant can you list the core four that plants need to survive possible answers include soil sunlight air and water true or false plants release oxygen into the air that humans and other animals breathe true fantastic job friends no matter where you live plants are a necessary part of life on earth and just like people plants need air and water to survive whether it is the tallest redwood tree or the smallest wildflower plants are constantly growing and helping keep the environment healthy and safe it is pretty cool to know that all life on this planet is connected the next time you take a breath of air or drink a cup of water think about what you have in common with our green plant friends and maybe you can take a nature walk and see how many different types of plants you can identify hope you had fun learning with us visit us at learnbright.org for thousands of free resources and turnkey solutions for teachers and homeschoolers.
        """)
    
    st.markdown("""
    > Which plant needs are mentioned?
    > What happens if one of those needs is missing?

    ##### 🎨 Activity: Design Your Own Plant

    Page 1:   
    - Draw your very own healthy plant in the activity pot.
    - Add big green leaves, colorful flowers!
    - Label each part with the needs from the vocabulary list you learned.
    
    Page 2:
    - Match each word to its meaning.
    > Tip: If you are stuck, check the video or vocabulary list again.
    
    """)

    # Convert images to base64 strings
    img1 = image_to_base64_str("images/lesson1_1.png")
    img2 = image_to_base64_str("images/lesson1_2.png")

    # Layout with columns
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="data:image/png;base64,{img1}" width="300"><br>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="data:image/png;base64,{img2}" width="300"><br>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    with open("documents/lesson1-activity.pdf", "rb") as file:
        st.download_button(
            label="📥 Download the Activity (PDF)",
            data=file,
            file_name="lesson1-activity.pdf",
            mime="application/pdf",
            key="download-pdf-1"
        )
    
    st.markdown("""

    ##### 🤔 Activity: What If?
    Let’s imagine what happens when plants don’t get what they need.
    Pick one scenario:
    - No sunlight for a week
    - Too much water every day
    - No space to grow
    >Draw or write what would happen to the plant in your notebook.
    >Explain why it would happen, using the vocabulary words to support your reasoning.
                
    ##### 🎯 Activity: Do You Know the Answer? (Group Game)
   
    This is a quick review game to test what you’ve learned.
    
    How to Play:
    1. Stand in a circle (or around a table). ⋆⭒˚𖠋𖠋𖠋*.⋆
    2. One person is the “Caller” and reads a clue.
    3. Everyone else shouts the answer as fast as they can.
    4. The Caller picks someone who got it right to read the next clue.
    5. Keep going until all clues are used or time runs out.
    """)

    st.image("images/lesson-1.4.png", caption="Let's Play", use_container_width=600)
          
    st.markdown("""
    🗣️ Clues:
    1.	This comes from the sun and helps plants make food!
    2.	Plants breathe in this gas to grow.
    3.	This comes from soil and is like vitamins for plants.
    4.	This gives roots and leaves room to spread out.
    5.	If this is too hot or too cold, it can slow down plant growth.
    6.	Plants need this liquid to stay alive and move nutrients.
    
   
    (If working alone: Read the clues to yourself and shout the answers out loud. Try to answer all in under 30 seconds!)
    """)

    if st.toggle("Show Answers", key="answers1-1"):
        st.markdown("""
        1. Light
        2. Air
        3. Nutrient
        4. Space
        5. Temperature
        6. Water
        """)
    
    st.markdown("""
   ##### 📜 Wrap-Up
    - Today you discovered the six essential needs plants must have to survive and grow. You also practiced identifying and describing them in different activities. In our next lesson, we will zoom in on the very first stage of a plant’s life, germination, and you will plant your own seed to start tracking its growth.
    
    Yay, you worked hard! It's game time now!

    #### 🎮 Activity: Crossword Puzzle

    Enjoy the puzzle solo or team up with a friend by creating an invite code inside the puzzle.
    Toggle the button to start the timer and reveal the board.
    You can restart or save your progress anytime using the options button in the top-left corner of the game.

    """)

    if st.toggle("🧩 Show Puzzle", value=False, key="toggle-puzzle1"):
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
            src="https://puzzleme.amuselabs.com/pmm/crossword?id=9ec0b783&set=6fd209c1b707d2ea7d9a73fff6d267b361bf1cc2d39099da8f73fd4fd346d1c1"
            aria-label="Puzzle Me Game">
        </iframe>
        """, unsafe_allow_html=True)

    st.markdown("""
    Here are the answers if you need them!
    """)

    if st.toggle("Show Answers", key="answers1-2"):
        st.markdown("""
        1. GROWTH
        2. WATER
        3. SEED
        4. LIGHT
        5. PLANT
        6. AIR
        7. PREDICT
        """)


    st.markdown("---")
    st.success("Next up: Lesson 2 - Germination")

    render_back_forth_nav(session_state, current_module_key="plantneeds", all_modules=all_modules, position="bottom")