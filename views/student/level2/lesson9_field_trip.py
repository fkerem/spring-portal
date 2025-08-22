import streamlit as st
from utils.navigation import render_back_forth_nav
from utils.img_formatting import image_to_base64_str

#Module Structure
from shared_modules import all_modules

def createPage(session_state):
    st.set_page_config(page_title="Field Trip", layout="wide")

    render_back_forth_nav(session_state, current_module_key="fieldtrip", all_modules=all_modules, position="top")

    st.subheader("🗺️ Lesson 9: Field Trip")
 
    st.markdown("""
    Hi students! 👋
    
    You’ve spent the last eight lessons planting seeds, testing soils, tracking data, and using the SPRING dashboard to make farming decisions. Today, you will step out of the classroom to see how real farmers and agricultural experts use these same ideas and tools in their daily work.
    
    By the end of this lesson, you will be able to:
                
    - Describe at least one career in agriculture and the skills it requires 👩‍🌾👨‍🔬
    - Explain how technology (like sensors and dashboards) is used on real farms 📡
    - Make clear connections between your SPRING project work and real-world farming practices 🌱
 
    ##### 📚 Key Vocabulary
    You will hear these terms during your visit.
    
    - **Career Pathway**: A planned route to gain skills and qualifications for a specific job
    - **Agronomist**: A scientist who studies crops and soils
    - **Agricultural Engineer**: Designs systems and technology to improve farming
    - **Extension Agent**:An educator who helps farmers apply research in the field
    - **Precision Agriculture**: Using technology and data to improve farming decisions
    """) 
    
    st.image("images/lesson-9.2.png", caption="Field Trip", use_container_width=True)

    st.markdown("""
    ##### 🌟 Activity: Getting Ready for the Visit
    1. **Class Recap**: Think back to what we’ve done in the SPRING project: planting, soil testing, monitoring moisture, and making decisions using data.
    2. **Big Question**: How do farmers use these same ideas and tools in the real world?
    3. **Review the Interview Questions Worksheet**: Choose at least 3 questions you want to ask.

    💡 Tip: Pick questions that interest you most or connect directly to what we’ve studied.

    """)
   


    with open("documents/lesson-9.1.pdf", "rb") as file:
        st.download_button(
            label="Download the Field Trip Interview Questions Worksheet(PDF)",
            data=file,
            file_name="lesson-9.1.pdf",
            mime="application/pdf",
            key="download-pdf-9"
        )
    

    st.markdown("""
                             
    ##### 🚜 Activity: On-Site Observation

    Explore the [Photos](agbridge/?user=student&page=photos) and [Location](agbridge/?user=student&page=location) tabs to get to know Purdue’s Research Farm. You’re invited to visit! To schedule a visit, email us at [info@oatscenter.org](mailto:info@oatscenter.org).

    During the field trip:
    - Look around, what crops are growing?
    - Notice any technology being used: sensors, irrigation systems, dashboards, weather stations, drones, etc.
    - Think about how these tools compare to the SPRING system in class.

    ##### 🗣️ Activity: Learning from the Expert
    The farmer or agricultural expert will:
    - Describe the farm’s conditions and crops
    - Explain how technology is used in daily decision-making
    - Connect their work to data and tools like the ones in the SPRING project

    ##### 💬 Activity: Q&A with the Expert
    """)  

    st.image("images/lesson-9.3.png", caption="", use_container_width=True)

    st.markdown("""
    Use your Interview Questions Worksheet to guide your conversation.
    - Ask your selected questions
    - Write short notes or key phrases in the “Interview Notes” section
    - Listen for examples of precision agriculture and connections to our classroom work

    ##### 📝 Activity 5: Reflection
    Before leaving or once you return to class, complete the reflection section on your worksheet:
    
    1. One new thing you learned about agricultural careers
    2. One example of how technology improves farming
    3. A connection between today’s visit and the SPRING project

   
    ##### 📜 Wrap-Up
    Today you connected your classroom learning to real-world farming. You saw how careers in agriculture use both traditional knowledge and modern technology to keep crops healthy and productive. Next lesson, we will reflect on everything you’ve learned in the SEED to SPRING project and create a final presentation to share your discoveries.
    
    Yay, you worked hard! It's game time now!

    #### 🎮 Activity: Crossword Puzzle

    Enjoy the puzzle solo or team up with a friend by creating an invite code inside the puzzle.
    Toggle the button to start the timer and reveal the board.
    You can restart or save your progress anytime using the options button in the top-left corner of the game.

    """)

    if st.toggle("🧩 Show Puzzle", value=False, key="toggle-puzzle9"):
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
            src="https://puzzleme.amuselabs.com/pmm/crossword?id=78f2a7d1&set=6fd209c1b707d2ea7d9a73fff6d267b361bf1cc2d39099da8f73fd4fd346d1c1"
            aria-label="Puzzle Me Game">
        </iframe>
        """, unsafe_allow_html=True)

    st.markdown("""
    Here are the answers if you need them!
    """)

    if st.toggle("Show Answers", key="answers9"):
        st.markdown("""
        1. PATHWAY
        2. AGRONOMIST
        3. CAREER
        4. WEATHER
        5. DRONE
        6. ENGINEER
        7. IRRIGATION
        """)

    
    st.markdown("---")
    st.success("Next up: Lesson 10 - Assessment & Reflection")

    render_back_forth_nav(session_state, current_module_key="fieldtrip", all_modules=all_modules, position="bottom")