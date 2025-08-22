import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="SPRING Dashboard", layout="wide")

# Logos


st.markdown(
    """
    <div style="display: flex; align-items: center; gap: 20px; padding-bottom: 10px;">
        <img src="https://erc-assoc.org/sites/default/files/styles/large/public/2024-02/IoT4Ag_Logo_AS_Upd.png?itok=GzTOSWZC.png" alt="Logo 2" style="height: 60px;">
        <img src="https://oatscenter.org/OATSCenter/Images/OATS.png" alt="Logo 2" style="height: 60px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Purdue_Boilermakers_logo.svg/2560px-Purdue_Boilermakers_logo.svg.png" alt="Logo 2" style="height: 60px;">
    </div>
    """,
    unsafe_allow_html=True
)

# Simulated sensor data
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
soil_moisture = [45, 50, 47, 49, 55, 60, 58]         # %
optical_intensity = [200, 180, 190, 220, 240, 250, 245]  # lux

df = pd.DataFrame({
    "Day": days,
    "Soil Moisture (%)": soil_moisture,
    "Optical Sensor (lux)": optical_intensity
})

# Global variable for teacher's quiz questions
if "quiz_bank" not in st.session_state:
    st.session_state.quiz_bank = []

# Tabs for each user tier
tabs = st.tabs(["👶 Young Student", "🧑‍🎓 High School", "👩‍🏫 Teacher", "👁‍🗨️ Public Display"])

# ---------- Young Student ----------
with tabs[0]:
    st.header("🌱 Young Student View")
    st.success("😊 The plant is doing great!")

    subtab1, subtab2, subtab7, subtab3, subtab4, subtab5, subtab6 = st.tabs(["📊 Visual", "📄 Raw Data", "📉 Additional Graphs", "🎮 Playground", "🖼️ Photos", "📚 Learn", "❓ Quiz"])

    with subtab1:
        st.write("Let’s see how the plant is feeling today:")

        soil_level = int(np.clip(np.interp(soil_moisture[-1], [0, 100], [0, 10]), 0, 10))
        light_level = int(np.clip(np.interp(optical_intensity[-1], [0, 500], [0, 10]), 0, 10))

        def get_gradient_color(level):
            hue = int(np.interp(level, [0, 10], [0, 120]))
            return f"hsl({hue}, 85%, 45%)"

        def draw_bar(level):
            color = get_gradient_color(level)
            bar = "".join(["█" if i < level else "░" for i in range(10)])
            return f"<span style='color:{color}; font-size: 24px; letter-spacing: 2px;'>{bar}</span>"

        col1, col2 = st.columns(2)
        with col1:
            st.metric("💧 Soil Moisture", f"{soil_moisture[-1]}%")
            st.markdown(draw_bar(soil_level), unsafe_allow_html=True)

        with col2:
            st.metric("☀️ Sunlight Level", f"{optical_intensity[-1]} lux")
            st.markdown(draw_bar(light_level), unsafe_allow_html=True)

        #st.image("./happy-plant.png", width=200, caption="Happy Plant ☀️")
        
        with st.container():
            st.markdown("<br>", unsafe_allow_html=True)  # Optional spacing
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image("images/happy-plant.png", width=200, caption="Happy Plant ☀️")

        #st.image("https://cdn-icons-png.flaticon.com/512/616/616408.png", width=100, caption="Happy Plant ☀️")

    with subtab2:
        st.subheader("📄 Raw Sensor Data (Week)")
        st.dataframe(df)

    with subtab3:
        st.subheader("🎮 Adjust the Conditions!")

        st.write("Change the sunlight and moisture to see how your plant feels!")

        sm_input = st.slider("Soil Moisture (%)", 0, 100, soil_moisture[-1])
        light_input = st.slider("Light Level (lux)", 0, 500, optical_intensity[-1])

        sm_level = int(np.interp(sm_input, [0, 100], [0, 10]))
        light_level = int(np.interp(light_input, [0, 500], [0, 10]))

        def predict_health(sm, light):
            if sm >= 5 and light >= 5:
                return "🌱😊 The plant is happy!"
            elif sm < 3 or light < 3:
                return "🥀😟 The plant is sad!"
            else:
                return "🌾😐 The plant is okay."

        st.markdown(f"**Your Prediction:** {predict_health(sm_level, light_level)}")

    with subtab4:
        st.subheader("🖼️ Photos from the Farm")
        st.image(
            "https://prairiefarmland.com/wp-content/uploads/2015/02/Benton-County-Indiana-farms-for-sale.jpg",
            caption="Purdue University Farm",
            use_container_width=True
        )

    with subtab5:
        st.subheader("📚 Learn")
        st.markdown("""
        **What does sensor mean?**
        >

        **Why do we use sensors on farms?**
        > So plants can “talk” to us! Sensors tell us when plants are thirsty or need more sun 🌞 or water 💧.

        **What is internet?**
        >

        **What is the Internet of Things (IoT)?**
        > It’s like a magic network that helps things like plants, animals, and tractors share what they feel.

        **Why is it helpful?**
        > Farmers don’t need to guess! They know exactly what the plants need to grow big and strong 🌽🌻.
        """)

    with subtab6:
        st.subheader("❓ Quiz Time!")
        st.markdown("What does a soil moisture sensor measure?")
        answer = st.radio("Choose one:", ["Light", "Water level", "Wind speed"], index=None, key="quiz1")
        if answer:
            if answer == "Water level":
                st.success("Correct! 🌱")
            else:
                st.error("Try again!")

    with subtab7:
        st.subheader("📉 ChirpStack Graphs")
        st.info("Placeholder for ChirpStack visualizations. Coming soon!")

# ---------- High School ----------
with tabs[1]:
    st.header("📈 High School Student View")
    subtab1, subtab2, subtab8, subtab3, subtab4, subtab5, subtab6, subtab7, subtab9 = st.tabs(["📊 Visual", "📄 Raw Data", "📉 Additional Graphs", "🎮 Playground", "🖼️ Photos", "📍 Location", "📚 Learn", "❓ Quiz", "📝 Exercises"])

    with subtab1:
        st.subheader("Sensor Data Over the Week")
        st.line_chart(df.set_index("Day"))
        st.write("Try analyzing relationships between soil moisture and sunlight!")

    with subtab2:
        st.subheader("📄 Raw Sensor Data")
        st.dataframe(df)

    with subtab3:
        st.subheader("🎮 Experiment with the Data")

        st.markdown("🔧 Modify last 7 days of data:")

        modified_sm = []
        modified_light = []

        for i, day in enumerate(days):
            col1, col2 = st.columns(2)
            with col1:
                sm = st.slider(f"{day} - Soil Moisture (%)", 0, 100, soil_moisture[i], key=f"sm_{i}")
                modified_sm.append(sm)
            with col2:
                light = st.slider(f"{day} - Light (lux)", 0, 500, optical_intensity[i], key=f"light_{i}")
                modified_light.append(light)

        modified_df = pd.DataFrame({
            "Day": days,
            "Soil Moisture (%)": modified_sm,
            "Optical Sensor (lux)": modified_light
        }).set_index("Day")

        st.line_chart(modified_df)

        st.markdown("📈 **Forecast Soil Moisture for Next 10 Days** (Linear Regression)")

        X = np.arange(7).reshape(-1, 1)
        y = np.array(modified_sm)
        model = LinearRegression().fit(X, y)

        X_future = np.arange(7, 17).reshape(-1, 1)
        y_future = model.predict(X_future)

        forecast_df = pd.DataFrame({
            "Day": [f"Day {i+1}" for i in range(7, 17)],
            "Predicted Soil Moisture (%)": y_future
        }).set_index("Day")

        st.line_chart(forecast_df)

    with subtab4:
        st.subheader("🖼️ Photos from the Farm")
        st.image(
            "https://prairiefarmland.com/wp-content/uploads/2015/02/Benton-County-Indiana-farms-for-sale.jpg",
            caption="Purdue University Farm",
            use_container_width=True
        )

    with subtab5:
        st.subheader("📍 Location of the Farm")
        st.map(pd.DataFrame({"lat": [40.4237], "lon": [-86.9212]}))

    with subtab6:
        st.subheader("📚 Learn")
        st.markdown("""
        **Why Technology in Agriculture?**
        > Using data helps reduce waste, increase yield, and protect the environment. Precision farming uses sensor data to water only when needed.

        **What is Internet?**
        > The Internet is a global network that connects millions of computers and devices.

        **What is Internet-of-Things (IoT)?**
        > A system where devices like soil sensors, weather stations, and drones collect and send data via the internet.

        📺 **Video: What is IoT?**
        """) # close previous markdown
        st.markdown(
            """
            <div style="position: relative; padding-bottom: 28.125%; height: 0; overflow: hidden; max-width: 50%;">
                <iframe 
                    src="https://www.youtube.com/embed/6mBO2vqLv38" 
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                    allowfullscreen 
                    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;">
                </iframe>
            </div>
            """,
            unsafe_allow_html=True
        )

        # enter markdown again
        st.markdown(
            """

            <br>

            **Introduction to IoT**
            >

            **Why LoRaWAN?**
            > LoRaWAN is a low-power, long-range wireless network. It's perfect for farms where WiFi or cell signals are weak.

            **Basics of LoRaWAN Communication**

            **Data Science Concepts (mean, variance, trends)**

            **Forecasting with Linear Regression**

            📘 Challenge: Can you write a mini-report using this data applying the linear regression techniques you learned?
            """,
            unsafe_allow_html=True
        )

    with subtab7:
        st.subheader("❓ Quiz Time!")
        st.markdown("Which algorithm did we use to forecast soil moisture?")
        q2 = st.radio("Choose one:", ["Decision Trees", "Linear Regression", "Neural Networks"], index=None, key="hs_q2")
        if q2:
            if q2 == "Linear Regression":
                st.success("Correct! Well done 🌾")
            else:
                st.error("Nope, check the Learn tab and try again!")

    with subtab8:
        st.subheader("📉 ChirpStack Graphs")
        st.info("Placeholder for ChirpStack visualizations. Coming soon!")

    with subtab9:
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

# ---------- Teacher ----------
with tabs[2]:
    st.header("📚 Teacher Tools")
    subtab1, subtab2, subtab7, subtab3, subtab4, subtab5, subtab6, subtab8, subtab10, subtab9 = st.tabs([
        "📊 Visual", "📄 Raw Data", "📉 Additional Graphs", "🖼️ Photos", "📍 Location", "📚 Learn",
        "✍️ Quiz Manager", "📏 Standards", "✅ Assessments", "📝 Notes"])

    with subtab1:
        st.write("Use this data to guide lesson planning and student experiments.")
        st.subheader("Combined Sensor Trends")
        st.line_chart(df.set_index("Day"))

    with subtab2:
        st.subheader("📄 Raw Data Table")
        st.dataframe(df)
        st.download_button("📥 Download CSV", df.to_csv(index=False).encode(), "sensor_data.csv")

    with subtab3:
        st.subheader("🖼️ Photos from the Farm")
        st.image(
            "https://prairiefarmland.com/wp-content/uploads/2015/02/Benton-County-Indiana-farms-for-sale.jpg",
            caption="Purdue University Farm",
            use_container_width=True
        )

    with subtab4:
        st.subheader("📍 Location of the Farm")
        st.map(pd.DataFrame({"lat": [40.4237], "lon": [-86.9212]}))

    with subtab5:
        st.subheader("📚 Learn")
        st.markdown("""
        **Why teach tech in ag?**
        > Agriculture is evolving. Understanding IoT empowers students to approach farming as a science.

        **Lesson Objectives:**
        - Understand the role of IoT and LoRaWAN in sustainable agriculture.
        - Interpret sensor data for decision-making.

        **Teaching Tools:**
        - Classroom discussion prompts (e.g., “What happens if you overwater a plant?”)
        - Mini-lab kits using Arduino or Micro:bit to simulate soil sensors.
        - Quizzes (can be embedded or downloadable)
        - Guided reading: How smart farming supports climate resilience.

        **Full lesson plans on:**
        - IoT and LoRaWAN
        - Data visualization and analysis
        **Assessment tools and student worksheets**
        - Quiz Generator (coming soon!)
        """)

    with subtab6:
        st.subheader("✍️ Create a Quiz")

        with st.form("quiz_form"):
            question = st.text_input("Enter your quiz question")
            option1 = st.text_input("Option 1")
            option2 = st.text_input("Option 2")
            option3 = st.text_input("Option 3")
            correct = st.radio("Select correct option", ["Option 1", "Option 2", "Option 3"])
            submitted = st.form_submit_button("Add Question")

            if submitted:
                st.session_state.quiz_bank.append({
                    "question": question,
                    "options": [option1, option2, option3],
                    "correct": correct
                })
                st.success("Question added!")

        if st.session_state.quiz_bank:
            st.subheader("🧾 Current Questions")
            for idx, q in enumerate(st.session_state.quiz_bank):
                st.markdown(f"**Q{idx+1}: {q['question']}**")
                for opt in q["options"]:
                    st.markdown(f"- {opt}")
                st.markdown(f"✔ Correct Answer: **{q['correct']}**")

    with subtab7:
        st.subheader("📉 ChirpStack Graphs")
        st.info("Placeholder for ChirpStack visualizations. Coming soon!")

    with subtab8:
        st.subheader("📏 Standards")
        st.info("This section will include mapped educational standards aligned with the lessons.")

    with subtab9:
        st.subheader("📝 Teacher Notes")
        notes = st.text_area("Use this space for class notes or preparation:", height=300)

        # Download button always shown, but disabled if empty
        st.download_button(
            label="📥 Download Notes",
            data=notes,
            file_name="teacher_notes.txt",
            mime="text/plain",
            disabled=(notes.strip() == "")
        )
        
        st.info("Note: Your input will remain only for this session unless connected to a persistent user system.")

    with subtab10:
        st.subheader("✅ Assessments")
        st.info("This section will include assessment templates, rubrics, and sample worksheets soon.")

# ---------- Public Display ----------
with tabs[3]:
    st.header("🌍 Public Display")
    subtab1, subtab2, subtab5, subtab3, subtab4 = st.tabs(["📊 Visual", "📄 Raw Data", "📉 Additional Graphs", "🖼️ Photos", "📍 Location"])

    with subtab1:
        st.write("Live demo of the field sensor data:")
        st.bar_chart(df.set_index("Day")[["Soil Moisture (%)"]])
        st.bar_chart(df.set_index("Day")[["Optical Sensor (lux)"]])

    with subtab2:
        st.subheader("📄 Raw Sensor Data")
        st.dataframe(df)

    with subtab3:
        st.subheader("🖼️ Photos from the Farm")
        st.image(
            "https://prairiefarmland.com/wp-content/uploads/2015/02/Benton-County-Indiana-farms-for-sale.jpg",
            caption="Purdue University Farm",
            use_container_width=True
        )

    with subtab4:
        st.subheader("📍 Location of the Farm")
        st.map(pd.DataFrame({"lat": [40.4237], "lon": [-86.9212]}))

    with subtab5:
        st.subheader("📉 ChirpStack Graphs")
        st.info("Placeholder for ChirpStack visualizations. Coming soon!")