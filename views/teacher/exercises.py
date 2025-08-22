import streamlit as st

def createPage():
    st.subheader("📝 Exercises")
    st.markdown("""
    These open-ended exercises will help you reflect on sensor concepts:
    - Understand measurement units
    - Apply critical thinking
    """)
    st.download_button(
        label="📥 Download Exercise Form",
        data=
        """- What is the measurement unit of the temperature sensor?

    [Your answer comes here]

    - What is the measurement unit of the soil moisture sensor?

    [Your answer comes here]""",
        file_name="example_exercise_file.txt",
        mime="text/plain"
    )
