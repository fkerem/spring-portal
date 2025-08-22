import streamlit as st
from utils.navigation import render_back_forth_nav
from utils.img_formatting import image_to_base64_str

# Define module structure
from shared_modules import all_modules  # or define inline if not importing

def createPage(session_state):
    st.set_page_config(page_title="Modern Tech Apps in Agriculture", layout="wide")

    render_back_forth_nav(session_state, current_module_key="moderntechapps", all_modules=all_modules, position="top")

    #st.title("📡 Lesson 1: Modern Tech Apps in Agriculture")
    st.subheader("📡 Lesson 3: Modern Tech Apps in Agriculture")

    st.markdown("""
    Hi students! 👋 

    Welcome to our lesson **Modern Technology Applications in Agriculture**.

    Modern technology is rapidly transforming the way we grow food, manage farms, and promote sustainability. From satellites that monitor crop health to robots that help with harvesting, modern agriculture is more high-tech than ever before! In this lesson, we will focus on one of the most exciting and transformative technologies being used in agriculture today, **the Internet of Things (IoT)**.

    By the end of this lesson, you will be able to:

    - Identify IoT components: sensors and gateways
    - Describe LoRaWAN and its key characteristics, specifically range and power
    - Explain real-world use cases and benefits of IoT in agriculture
    - Recognize related cloud services such as network server, database and dashboard

    Before we begin, let's do some activities.

    ##### 🌾 Activity: Unhealthy Soil

    Imagine you are a farmer and notice that your plants do not look healthy. You suspect the problem might be the soil, but you are not sure whether it is too dry or wet.
    Here comes the question:

    👉 How can we tell if the soil is wet or dry without digging it up or getting our hands dirty?

    > Take a moment to think. You can shout out your ideas or write them down. There is no wrong answer, be creative!

    ##### 🗣️ Activity: Soil Talking to Farmer

    👉 The image below illustrates one way the soil can “talk” to the farmer. Can you tell what’s happening?

    """)

    st.image("images/level2-lesson1-1.png", caption="Image: Soil Talking to the Farmer", use_container_width=True)

    st.markdown("""
    > Good job! How exciting, isn't it?

    We will now start learning about each component in this interconnected system called the Internet of Things (IoT), and how it’s helping farmers grow food more efficiently without always needing to be in the field. Fasten your seatbelts adventurers! 🛫


    #### 🤔 What is Internet of Things (IoT)?

    **Internet of Things (IoT)** is a system of interconnected devices that collect and exchange data.
    These devices are called “things” because they can come in all shapes and sizes (often tiny) and are designed for specific tasks.

    Imagine your smartwatch sending your heart rate to your phone, or your voice assistant playing your favorite music when you ask. These are all examples of IoT devices.

    IoT devices come in many types, but we will focus on just two:

    - **Sensors**: Sensors measure specific physical properties in the environment. For example, a soil moisture sensor measures how wet the soil is, while a temperature sensor tracks how hot or cold the air or ground is. They often use probes (small attachments or extensions) to collect this data directly from the source, like the soil or the air.
    - **Gateways**: A gateway acts like a translator or messenger. It collects data from sensors, and forwards them to the internet.

    Sensors cannot connect to the internet on their own because they have limited capabilities such as low power and basic communication.
    That’s why they send their data to a more powerful device called gateway, which relays the message to the internet.
    This will make even more sense in the next section, so let’s switch gears and keep going!..

    #### 📶 Why Gateways Matter: A Look into LoRaWAN

    **LoRaWAN** stands for _Long Range Wide Area Network_, but what does that actually mean? Let’s watch the video to find out:

    """)

    st.video("https://youtu.be/UvI8_3Zw4qo")

    # Toggle for transcript
    if st.toggle("Show Video Transcript", key="v1-transcript"):
        st.markdown("""
        > Hi everyone. So let's now see why we need a gateway and explore LoRaWAN. The internet runs on a set of rules called protocols. Different devices should use the same protocol to be able to communicate with each other. This is just like speaking the same language. We have seen that IoT devices are often tiny and have limited power capabilities. Because of that, they cannot use the same protocols as regular devices. They need a different kind of system. The one that allows them to send small amounts of data over long distances using very little power. That's where LoRaWAN comes in. LoRaWAN stands for Long Range Wide Area Network. It is a special type of protocol designed just for this purpose. It allows many sensors to send data at low power over long ranges of distances. But it only works with the help of a gateway. So let's now see how it works over an image. You've seen this image before, right? Let me summarize what is happening in the image. So on the left we have a farm and we have the corns in the farm and underneath we have our soil moisture sensors attached to the soil through their probes and each of them have a radio on top. These soil moisture sensors measure the amount of water absorbed by the soil. They do not have a direct communication with the other systems and devices in the internet because they have low power capabilities and they need to use a specific set of rules among each other. So that is why they are only able to send the data to the gateway. Gateway is able to speak the same language as the sensors. So what happens is that gateway gets the data, collects the data from the sensors and the communication is maintained by LoRaWAN protocol and after that gateway can actually speak multiple languages. So that is why the collected data can be sent from gateway to the other systems such as cloud on the internet and then the farmers can access the data. So gateway is just like a translator, language translator or you can think of it as a post office sending the messages coming from the sensors to the internet. I hope you enjoyed the discussion. If you have any questions, feel free to ask over our email address.
        """)

    with open("slides/why-gateways-matter-a-look-into-lorawan.pdf", "rb") as file:
        st.download_button(
            label="📥 Download Slides (PDF)",
            data=file,
            file_name="why-gateways-matter-a-look-into-lorawan.pdf",
            mime="application/pdf",
            key="download-pdf-1"
        )

    st.markdown("""
    Remember, LoRaWAN is a wireless communication protocol designed for:

    - Connecting many sensors 🤝
    - Low power consumption 🔋
    - Long range transmission 📶

    ##### 🔍 Activity: Explore in Hand

    Let’s break into groups and explore the sensors and gateways that your teacher will hand out.

    ##### 🌡️ Sensor Types, Use Cases and Benefits

    There are many different types of sensors used in agriculture, and each one serves a specific purpose. 
    In this section, we will focus on three common types of agricultural sensors:

    - **Soil moisture sensor:** Measures how much water is present in the soil.
    - **Temperature sensor:** Measures the temperature of the air or the soil.
    - **Rain gauge:** Measures how much rainfall has occurred in a specific area.
    """)

    # Convert images to base64 strings
    se01_b64 = image_to_base64_str("images/se01-lb.jpg")
    rain_b64 = image_to_base64_str("images/rain-gauge.jpg")

    # Layout with columns
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="data:image/png;base64,{se01_b64}" width="300"><br>
                <div><strong>
                <a href="https://www.dragino.com/products/agriculture-weather-station/item/277-se01-lb.html" target="_blank" style="text-decoration: none; color: inherit;">
                SE01-LB: Soil Moisture & Temperature Sensor
                </a>
                </strong></div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="data:image/png;base64,{rain_b64}" width="205"><br>
                <div><strong>
                <a href="https://extension.purdue.edu/news/county/white/2021/03/Report-Whats-in-Your-Rain-Gauge-Contribute-to-Science.html" target="_blank" style="text-decoration: none; color: inherit;">
                Rain Gauge Sensor
                </a>
                </strong></div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("""
    These sensors play an important role in deciding when and how much to water crops, tracking dry conditions, and monitoring soil and plant health.


    ##### 🧠 Activity: Brainstorming

    Let’s break into groups and brainstorm about these:

    👉 What problems on a farm could sensors solve?

    > Take a moment to think. Discuss with your group and take notes of your ideas. Pick a representative to share your ideas with the class.

    👉 Imagine you are designing an IoT solution for a farm, what sensors would you use?

    > Take a moment to think. Feel free to invent your own imaginary sensors just for fun! Again; discuss, take notes and pick a representative to share your ideas with the class.


    #### ☁️ What is Cloud?

    We have talked about sensors and gateways but what happens after the sensor data is sent to the Internet?
    That's where the cloud comes in. The cloud is made up of powerful computers that store, process, and visualize data online.
    When the gateway sends data to the cloud, cloud systems organize that information and can even turn it into charts or dashboards for farmers to see and use.

    Go ahead and watch the video below to get familiar with these cloud components:

    """)

    st.video("https://youtu.be/vskhPf3naSc")
    # Toggle for transcript
    if st.toggle("Show Video Transcript", key="v2-transcript"):
        st.markdown("""
        > Hi everyone, we have seen the sensors and the gateway. But what about cloud? So the cloud contains the components that processes and analyzes the data. So let me summarize over this diagram. So we have the gateway that collected the data from the sensors and it needs to transmit the data to the internet to the cloud. And cloud has three main components. The first component is the network server. What happens is the gateway transmits all the messages that it gets from the sensors to the network server in the cloud. Network server then accepts and organizes this data and then transmits them to the second component called database. The duty of the database is just to store the data in an organized manner in different tables. And after that database transmits those data to the dashboard when needed by the dashboard because dashboard visualizes the data and presents them to the farmer. These were the components in the cloud that allows to organize the data and then presents them in a visualized manner to the farmer so that farmer can make smart decisions. I hope you enjoyed the discussion.
        """)

    with open("slides/cloud-components.pdf", "rb") as file:
        st.download_button(
            label="📥 Download Slides (PDF)",
            data=file,
            file_name="cloud-components.pdf",
            mime="application/pdf",
            key="download-pdf-2"
        )

    st.markdown("""
    Remember, we have the cloud components:

    - Network server, accepting and organizing the data
    - Database, storing the organized data
    - Dashboard, turning the stored data into visualizations that help farmers make smart decisions.

    Farmers can directly access the data and the visualizations on the cloud through internet.

    Yay, you worked hard! It's game time now!

    #### 🎮 Activity: Crossword Puzzle

    Enjoy the puzzle solo or team up with a friend by creating an invite code inside the puzzle.
    Toggle the button to start the timer and reveal the board.
    You can restart or save your progress anytime using the options button in the top-left corner of the game.

    """)

    if st.toggle("🧩 Show Puzzle", value=False, key="toggle-puzzle3"):
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
            src="https://puzzleme.amuselabs.com/pmm/crossword?id=modern-tech-apps-ag&set=abbafa240bf74287a3998277c2f60529b4bef12bea89892f469bce494dbd9e88"
            aria-label="Puzzle Me Game">
        </iframe>
        """, unsafe_allow_html=True)

    st.markdown("""
        Here are the answers if you need them!
        """)
    
    if st.toggle("Show Answers", key="answers3"):
        st.markdown("""
        1. NETWORKSERVER
        2. TRANSLATOR
        3. DASHBOARD
        4. DATABASE
        5. SENSOR
        6. FARMER
        7. MOISTURE
        8. GATEWAY
        9. PROBE
        10. PROTOCOL
        11. CLOUD
        12. LORAWAN
        13. THREE
        14. RAINGAUGE
        """)

    st.markdown("---")
    st.success("Next up: Lesson 4 - Dashboard")

    render_back_forth_nav(session_state, current_module_key="moderntechapps", all_modules=all_modules, position="bottom")