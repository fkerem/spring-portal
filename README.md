# SPRING Portal

The SPRING Portal is an interactive learning environment for students, teachers, and public visitors to explore agriculture through plant science, classroom experiments, and sensor data. Developed through the IoT4Ag initiative, it connects hands-on growing activities with observations from classroom corn pots, research farms, and a weather station.

## Find your way

Open the portal using the address provided by your instructor or host. Start at **Home** for an overview video, then use **Select User Role** in the sidebar to choose the tools you need. The portal opens in the Student view by default.

| Role | Tools for this audience |
| --- | --- |
| **Student** | **Lessons** for guided learning and **Playground** for interactive activities. |
| **Teacher** | **Module** for the printable teaching guide and **Notes** for lesson preparation. |
| **Public Audience** | Shared dashboards, tutorials, photos, and farm visit information. |

All three roles can access **Home**, **Pot Data**, **Farm Data**, **Weather Data**, **Photos**, **Location**, and **Tutorials**. You can switch roles to explore the other views; selecting a role does not create an account.

## Lessons

Select **Student → Lessons**, then choose a lesson card. The current curriculum contains ten lessons, listed under Level 2 (Intermediate):

1. Plant Needs
2. Germination
3. Modern Tech Apps
4. Dashboard
5. Data Comparison
6. Soil Properties
7. Soil Layers
8. What We Learned?
9. Field Trip
10. Assessment

The lessons combine plant growth and soil investigations with agricultural technology, graph interpretation, and farm observations. Depending on the lesson, students can watch videos, download worksheets or slides, follow hands-on activities, and complete puzzles. Use the previous and next lesson buttons to move through the sequence.

The final lesson includes a 15-question quiz. Submitting answers displays a score and feedback for each question. Assessment results are temporary session data; the portal does not provide a persistent gradebook.

## Explore sensor data

| Page | What you can explore |
| --- | --- |
| **Pot Data** | An embedded classroom corn pot dashboard for observing soil sensor readings. |
| **Farm Data** | Live and historical soil measurements, with chart controls and historical CSV downloads. |
| **Weather Data** | An embedded weather station dashboard from Purdue Research Farm. |

### Try a farm data comparison

1. Open **Farm Data** and select **Purdue Research Farm (West Lafayette, IN)** under **Location**.
2. Choose **Soil Moisture** or **Soil Temperature** under **Modality**.
3. Choose **Live** or the historical period **July 9–22, 2025** under **Date**.
4. Set **Duration** to **Last 1 Day**, **Last 1 Week**, or **Last 2 Weeks**. For historical data, these are fixed windows ending on July 22, 2025.
5. Choose **Sensor 1** or **25 Sensors** under **Sensor Scope**, then choose a **Line Graph**, **Bar Chart**, **Histogram**, or **Box Plot**.
6. Expand the chart panels as needed. For historical selections, open **Raw Data & Downloads** to preview the first ten rows and choose **Download CSV** or **Download CSV for Excel**. Both downloads are CSV files.

The **All** options let you display multiple measurements, dates, or sensor scopes together. For a classroom discussion, compare the same measurement across one sensor and the group of 25 sensors, or compare moisture and temperature over the same historical window.

The second farm location, **KC Bailey Orchards, Inc. (New York)**, currently provides a live soil moisture line graph for Sensor 1, with the same three duration choices.

## Teaching and classroom resources

- **Module:** Choose the Teacher role to preview or download the [Teacher Module Guide](documents/spring-module.pdf), which includes lesson plans, classroom materials, and linked tutorials.
- **Notes:** Write preparation or class notes in the Teacher view, then select **Download Notes** to save a text file. Notes are temporary; download them before leaving the page or ending the session.
- **Tutorials:** Watch eight videos covering pot and soil selection, seeds, gateway connection, sensor setup, the pod, planting, and sensor placement, plus a closing question.
- **Photos:** Browse a 32-photo gallery from Purdue Research Farm, select an image for a larger preview, and adjust the number of thumbnails per row.
- **Location:** View the Purdue Research Farm map and directions. The page includes contact information for arranging a visit.

Printable materials are also available directly in this repository, including the [Plant Needs activity](documents/lesson1-activity.pdf), [Germination data collection worksheet](documents/lesson-2.1.pdf), and [Dashboard detective sheet](documents/lesson-4.1.pdf).

## Playground

Select **Student → Playground** and choose an activity:

- **Laughing Plant Monitor:** Adjust simulated air temperature and soil moisture to see the plant's illustrated response.
- **Graph Generator:** Change seven days of sample temperature and moisture values, then explore the resulting line graph.
- **SPRING Jigsaw:** Complete an embedded jigsaw puzzle.

The plant monitor and graph generator use sample data for experimentation. Changing their sliders affects the activity only.

## Using the portal in class

Farm, pot, and weather charts load from external dashboards. Videos, puzzles, and map tiles also require internet access and availability of their hosting services. If an embedded resource does not load, check the classroom connection and whether the school network permits that service.

Historical CSV files and printable learning materials are included in the repository. Historical chart displays still load from the external dashboard. Download worksheets and any historical data you need before a lesson.

For help using the portal, contact your instructor or host.

## Run the portal locally

For instructors or hosts running their own copy, this is a Python application built with Streamlit. The repository specifies Python **3.13.7** in [.python-version](.python-version).

From the repository root, create and activate a virtual environment, install the [dependencies](requirements.txt), and start the [portal](streamlit_app.py):

```sh
python3 -m venv env
source env/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run streamlit_app.py
```

On Windows, activate the environment with `env\Scripts\activate` instead. Open the local URL printed by Streamlit, normally `http://localhost:8501`. Run the command from the repository root so the portal can find its images, documents, and data.

## License

Copyright 2025 Faik Kerem Ors. All rights reserved. Use, copying, modification, and distribution require the author's prior written permission; see [LICENSE](LICENSE).
