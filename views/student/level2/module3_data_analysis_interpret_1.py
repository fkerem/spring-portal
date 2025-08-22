import streamlit as st
from utils.navigation import render_back_forth_nav
from utils.img_formatting import image_to_base64_str

# Define module structure
from shared_modules import all_modules  # or define inline if not importing

def createPage(session_state):
    st.set_page_config(page_title="Data Analysis 1", layout="wide")

    render_back_forth_nav(session_state, current_module_key="dataanalysis1", all_modules=all_modules, position="top")

    st.title("📡 Lesson 3: Data Analysis and Interpretation 1")

    st.markdown("""

    By the end of this lesson, you will be able to:

    - Create and interpret line plots, histograms, and box plots using plant sensor data.
    - Describe patterns using median, quartile, range.
    - Convert and analyze data using standard and metric units.
    - Use data analysis to develop a recovery plan for a failing plant.
    - Test and refine their plan using a simulated dashboard and reflect on outcomes.
    - Solve a game-based mystery by reading and interpreting graphs.
    - Present their findings in a collaborative poster.


    These are the terms you’ll become familiar with after completing the class:

    - **Line Plot:** A graph that shows changes over time by connecting data points with lines.
    - **Histogram:** A bar graph that shows how often each range of values appears in a dataset.
    - **Box Plot:** A graph that shows how data is spread out, including the median, quartiles, and any outliers.
    - **Median:** The middle number in a list of numbers arranged in order.
    - **Range:** The difference between the highest and lowest values in a set.
    - **Interquartile Range (IQR):** The range between the first quartile (25%) and the third quartile (75%) of the data – it shows where the middle half of the data lies.
    - **Outlier:** A number in a dataset that is much higher or lower than most of the other values.
    - **Metric System:** A measurement system based on units like Celsius (°C), liters (L), and centimeters (cm). Used in science and most countries around the world.
    - **Standard System (U.S. Customary):** A measurement system based on units like Fahrenheit (°F), gallons, and inches. Common in the United States.


    ##### 👀 Activity: What You See?
    """)

    st.image("images/the-four-seasons-of-corn.png", caption="Image: The Four Seasons of Corn", use_container_width=False, width=600)

    st.markdown("""
    👉 What differences do you notice in how the corn looks across the seasons?

    👉 How might temperature, sunlight, or water availability affect plant health during these times?


    ##### 🔎 Activity: Data Detectives

    You will work as a team for this activity. Your role is 

    2. Explore
    Purpose: Engage students in collaborative data analysis by interpreting real sensor data, identifying patterns, and making seasonal comparisons using graphical tools.
    Activity:
    Students work in teams as “Data Detective” groups. Each team receives a “Mission File” that includes:
    The farmer’s weekly sensor data (same across all teams), including soil moisture, temperature, and watering schedule.
    A reference chart of ideal corn-growing conditions (temperature and moisture ranges) using both metric and standard units. 
    A seasonal assignment, specific for each team. 
    Each team collaborates to:
    Construct three graphs based on their assigned season’s sensor data:
    A line plot (temperature trend)
    A histogram (soil moisture frequency)
    A box plot (moisture distribution)
    Compare their seasonal data to the ideal conditions for corn. 
    Determine if corn would thrive under the given seasonal conditions.  
    Drawing a cartoon representing the plant’s condition in that season.  
     
    Teacher role: Distribute mission files, provide graphing resources, monitor collaboration, and guide teams with strategic questions (e.g., “How does your data differ from the ideal range? or “Would corn survive in this season?”)
    Student role: Collaborate within teams to build graphs, identify mismatches between seasonal conditions and corn’s needs, and express their findings visually and verbally.

    """)

    st.markdown("---")
    st.success("Next up: Lesson 4 - Data Analysis and Interpretation 2")

    render_back_forth_nav(session_state, current_module_key="dataanalysis1", all_modules=all_modules, position="bottom")