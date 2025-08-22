import streamlit as st
from utils.navigation import render_back_forth_nav
from utils.img_formatting import image_to_base64_str

# Define module structure
from shared_modules import all_modules  # or define inline if not importing

def createPage(session_state):
    st.set_page_config(page_title="Data Analysis 2", layout="wide")

    render_back_forth_nav(session_state, current_module_key="dataanalysis2", all_modules=all_modules, position="top")

    st.title("📡 Lesson 3: Data Analysis and Interpretation 2")

    st.markdown("""

    3. Explain

    Purpose: Deepen understanding by analyzing seasonal data through graph interpretation, reinforcing formal vocabulary, and making connections to corn’s ideal growth conditions.
    Activity:
    Each team presents their graph-based findings from the Explore phase and discusses:
     
    What does each graph reveal about the environmental conditions in their assigned  season? 
    Are there any noticeable patterns, trends, or outliers? 
    What does the median temperature or soil moisture level suggest about that season’s growing environment? 
    Based on your data, would this season be a good fit for growing corn? 
     
    The teacher leads a short mini-lesson that includes:
    Visual comparison of well-constructed vs. inaccurate graphs 
    Clarification of how key vocabulary connects to the data 
    A review of measurement units and how to interpret values across metric and standard systems
    
    Vocabulary focus:

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
    
    Teacher role:
    Facilitate discussion and ask students to support their claims with data 
    Clarify any misconceptions and highlight effective graphing practices 
    Provide charts, visual examples, and clear definitions 
    Reinforce vocabulary through applied examples from student work  
    Student role:
    Present and explain their seasonal graphs using academic vocabulary 
    Reflect on whether the season’s data aligns with corn’s ideal conditions 
    Listen to other teams’ comparisons and ask questions 
    Adjust their interpretations as needed based on peer feedback and teacher clarification
    
    4. Elaborate
    Purpose: Apply understanding in a new context by interpreting sensor graphs on the SPRING dashboard to comparing them to corn’s ideal growth conditions.
    Activity:
    Students explore the SPRING dashboard playground, where they examine alive data. Working in teams, they:
    Identify trends or patterns in soil moisture and temperature across different seasons 
    Compare the dashboard graphs 
    Use academic vocabulary to describe whether the conditions support healthy plant growthor not 
    Teacher role:
    Facilitate exploration of the dashboard
    Guide student comparisons between real data and crop-specific needs
    Ask reasoning-based questions to promote critical thinking
    Sample prompts:
    Which season seems most favorable for corn growth? Why? 
    How does soil moisture in the winter compare to what corn needs? 
    Which graph helped you see the trend more clearly? 
    
    Student role:
    Examine seasonal dashboard graphs as a team 
     Compare data to corn’s optimal growing conditions 
     Discuss their reasoning using graph vocabulary and evidence 
    
    5. Evaluate
    Purpose: Assess students’ ability to read, interpret, and create graphs using seasonal plant sensor data – through a game-based challenge that concludes with a collaborative classroom poster.
    Activity:
    Students complete a challenge called “The Secret Code of the Garden” – a mystery game where they use graphing and data interpretation skills to uncover a hidden message.
    Working in teams, students solve puzzles by:
    Reading and analyzing graphs (line plots, histograms, box plots)
    Answering data-based questions involving median, range, and unit interpretation
    Identifying visual clues embedded in the graphs  (e.g., tallest histogram bar)
    Each correct interpretation reveals a letter or symbol. Once all clues are solved, teams piece the letters together to  reveal a mystery phrase.
    This phrase become the final element of their Save the Plant Poster, the culminating product of the lesson.
    Poster Contents:
    Completed graphs from the Explore phase
    Key vocabulary and definitions from the Explain phase
    The decoded mystery phrase and supporting visual clues from the game 
    A student-drawn cartoon that illustrates their plant’s story or team’s detective journey 
    A brief written reflection: “What did we learn about data, graphs, and plant health? 
     
    Teacher role: Facilitate the game, provide clue materials, support poster creation, and assess student work using a rubric that includes graph accuracy, vocabulary use, reasoning, and collaboration.
    Student Role: Collaborate to solve the puzzle, apply graphing and analysis skills, and create a poster that showcases their learning.  
    (Optional: present their poster or participate in a classroom gallery walk.)
    
    The seasonal weather data used in this lesson was retrieved from the National Weather Service’s official climate records for Indianapolis, IN (National Weather Service, n.d.). 

    """)

    st.markdown("---")
    st.success("Next up: Module 1 - Data Analysis")

    render_back_forth_nav(session_state, current_module_key="dataanalysis2", all_modules=all_modules, position="bottom")

