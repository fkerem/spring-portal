import streamlit as st
from utils.navigation import render_back_forth_nav
from utils.img_formatting import image_to_base64_str

#Module Structure
from shared_modules import all_modules

def createPage(session_state):
    st.set_page_config(page_title="Assessment & Reflection", layout="wide")

    render_back_forth_nav(session_state, current_module_key="assessment", all_modules=all_modules, position="top")

    st.subheader("📝 Lesson 10: Assessment & Reflection")

    st.markdown("""
    
    Hi students! 👋
                
    You’ve learned a lot during the SEED to SPRING project; from planting seeds and testing soils, to reading dashboard data and making farming decisions using technology.
    
    Today is your final check-in. You will take a short quiz to show what you know.
   
    By the end of this lesson, you will be able to:
     
    - Demonstrate your understanding of plant growth needs, soil properties, and agricultural technology 🌱
    - Review and reinforce your knowledge through discussion 📊

    ##### QUIZ
    - Answer each question, then click **Submit**.
    - You will see which ones are correct and the right answers for any you miss.
    """)
        
    st.image("images/lesson-10.1.png", caption="", use_container_width=True)

    questions_data = [
        {
            "q": "1) Which of the following is NOT a basic need for plant growth?",
            "options": ["Water", "Light", "Plastic", "Nutrients"],
            "answer_idx": 2
        },
        {
            "q": "2) Seeds need the right temperature to germinate because:",
            "options": [
                "Too hot or too cold can slow or stop germination",
                "Heat makes seeds grow twice as fast",
                "Cold always kills seeds instantly",
                "Temperature has no effect"
            ],
            "answer_idx": 0
        },
        {
            "q": "3) If your soil is 50% clay, 30% silt, and 20% sand, which problem is most likely?",
            "options": [
                "Soil dries out too fast",
                "Roots struggle to grow due to poor drainage",
                "Soil blows away in the wind",
                "Nutrients wash away quickly"
            ],
            "answer_idx": 1
        },
        {
            "q": "4) In the SPRING project, the soil moisture sensor helps farmers:",
            "options": [
                "Count how many seeds are in the soil",
                "Measure how much water is in the soil",
                "Predict the price of corn",
                "Test soil color"
            ],
            "answer_idx": 1
        },
        {
            "q": "5) Which soil type drains water the fastest?",
            "options": ["Clay", "Loam", "Sandy", "Silty"],
            "answer_idx": 2
        },
        {
            "q": "6) If plants in the SPRING project grew slowly even with enough water, what might be missing?",
            "options": ["Soil", "Nutrients", "Sand", "Shade"],
            "answer_idx": 1
        },
        {
            "q": "7) Why is good drainage important for healthy plant growth?",
            "options": [
                "It prevents roots from rotting in too much water",
                "It keeps the soil cold",
                "It stops insects from entering the soil",
                "It makes plants grow faster in all conditions"
            ],
            "answer_idx": 0
        },
        {
            "q": "8) If the SPRING dashboard shows soil moisture dropping quickly for two days, what could be a possible cause?",
            "options": ["Heavy rain", "Overwatering", "Hot, dry weather", "Adding more clay to the soil"],
            "answer_idx": 2
        },
        {
            "q": "9) Which crop would likely do BEST in sandy soil with limited water?",
            "options": ["Rice", "Cactus", "Lettuce", "Carrots"],
            "answer_idx": 1
        },
        {
            "q": "10) Which soil type has a balanced mix of sand, silt, and clay?",
            "options": ["Clay", "Loam", "Sandy", "Silty"],
            "answer_idx": 1
        },
        {
            "q": "11) Precision agriculture means:",
            "options": [
                "Guessing when to water crops",
                "Planting in perfect rows only",
                "Using technology and data to make farming decisions",
                "Growing crops without soil"
            ],
            "answer_idx": 2
        },
        {
            "q": "12) If soil temperature stays below the ideal range for two weeks, what might happen?",
            "options": [
                "Seeds may germinate more slowly",
                "Plants will grow twice as fast",
                "Roots will dry out immediately",
                "Soil will turn into clay"
            ],
            "answer_idx": 0
        },
        {
            "q": "13) Yellowing leaves on a plant can be caused by:",
            "options": [
                "Too much sunlight only",
                "Lack of nutrients or water stress",
                "Planting too close together only",
                "Using a loam soil type"
            ],
            "answer_idx": 1
        },
        {
            "q": "14) Which is an advantage of sandy soil?",
            "options": ["Holds water well", "Drains quickly", "Contains more nutrients than clay", "Always keeps plants warm"],
            "answer_idx": 1
        },
        {
            "q": "15) Which career works directly with farmers to apply research in the field?",
            "options": ["Agronomist", "Agricultural engineer", "Extension agent", "Soil tester"],
            "answer_idx": 2
        },
    ]

    if "lesson10_answers" not in st.session_state:
        st.session_state.lesson10_answers = {i: None for i in range(len(questions_data))}
    if "lesson10_submitted" not in st.session_state:
        st.session_state.lesson10_submitted = False
    if "lesson10_reveal" not in st.session_state:
        st.session_state.lesson10_reveal = False

    with st.form("final_quiz_form", clear_on_submit=False):
        for i, qd in enumerate(questions_data):
            st.markdown(f"**{qd['q']}**")
            choice = st.radio(
                label="",
                options=qd["options"],
                index=(qd["options"].index(st.session_state.lesson10_answers[i]) if st.session_state.lesson10_answers[i] in qd["options"] else 0),
                key=f"q_{i}",
            )
            st.session_state.lesson10_answers[i] = choice  
            st.divider()

        submitted = st.form_submit_button("✅ Submit")
        
     
    if submitted:
        st.session_state.lesson10_submitted = True
        correct_flags = []
        for i, qd in enumerate(questions_data):
            sel = st.session_state.lesson10_answers[i]
            correct = (qd["options"].index(sel) == qd["answer_idx"]) if sel is not None else False
            correct_flags.append(correct)

        score = sum(correct_flags)
        st.success(f"Your score: **{score} / {len(questions_data)}**")

        if score >= 12:
            st.balloons()

        for i, qd in enumerate(questions_data):
            sel = st.session_state.lesson10_answers[i]
            is_correct = (qd["options"].index(sel) == qd["answer_idx"]) if sel is not None else False
            correct_text = qd["options"][qd["answer_idx"]]

            if is_correct:
                st.markdown(f"**Q{i+1}: Correct!** ✅  \n*Your answer:* {sel}")
            else:
                st.markdown(f"**Q{i+1}: Not quite.** ❌  \n*Your answer:* {sel if sel else 'No answer'}  \n*Correct answer:* **{correct_text}**")
            st.divider()

        colA, colB, colC = st.columns([1,1,1])
        with colA:
            if st.button("🔁 Try Again"):
                # reset
                st.session_state.lesson10_answers = {i: None for i in range(len(questions_data))}
                st.session_state.lesson10_submitted = False
                st.session_state.lesson10_reveal = False
                st.experimental_rerun()
       
    
    st.markdown("---")

    render_back_forth_nav(session_state, current_module_key="assessment", all_modules=all_modules, position="bottom")