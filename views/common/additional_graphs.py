import streamlit as st

def createPage():

    st.subheader("📊 More Graphs")
    #st.info("Placeholder for Grafana visualizations. Coming soon!")

    st.markdown(
        """
        <p>See where the sensors are located!</p>
        <iframe 
            src="https://dashboard.oats.ecn.purdue.edu/d/cdpb3xnuohwqo2/soil-sensors?orgId=1&from=now-7d&to=now&timezone=browser&var-Project=$__all&var-Plot=$__all&var-MoistureDepth=$__all&var-TempDepth=$__all&viewPanel=panel-1-clone-0"
            width="800" height="800"
        ></iframe>
        """,
        unsafe_allow_html=True
    )

    # Old Graphs

    # https://dashboard.oats.ecn.purdue.edu/d/e69f4933-d92a-4cfc-956a-020c850bf4b9/soil-sensors-agbridge?orgId=1&from=now-14d&to=now&timezone=browser&var-Project=8&var-Plot=1001&var-MoistureDepth=$__all&var-TempDepth=$__all&viewPanel=panel-1-clone-0

    st.markdown(
        """
        Moisture Plot 1001 Average Live EDT Time
        <iframe src="https://dashboard.oats.ecn.purdue.edu/d-solo/e69f4933-d92a-4cfc-956a-020c850bf4b9/soil-sensors-agbridge?orgId=1&from=now-14d&to=now&timezone=browser&var-Project=8&var-Plot=1001&panelId=1&var-MoistureDepth=$__all&var-TempDepth=$__all&viewPanel=panel-1-clone-0&__feature.dashboardSceneSolo" width="900" height="400" frameborder="0"></iframe>
        """,
        unsafe_allow_html=True
    )

    # https://dashboard.oats.ecn.purdue.edu/d/e69f4933-d92a-4cfc-956a-020c850bf4b9/soil-sensors-agbridge?orgId=1&from=2025-07-09T20:56:23.574Z&to=2025-07-23T20:56:23.574Z&timezone=browser&var-Project=8&var-Plot=1001&var-MoistureDepth=$__all&var-TempDepth=$__all&viewPanel=panel-1-clone-0

    st.markdown(
        """
        Moisture Plot 1001 Average Fixed (FROM 2025-07-09T00:00 TO 2025-07-22T00:00 EDT)
        <iframe src="https://dashboard.oats.ecn.purdue.edu/d-solo/e69f4933-d92a-4cfc-956a-020c850bf4b9/soil-sensors-agbridge?orgId=1&from=2025-07-09T04:00:00.000Z&to=2025-07-23T04:00:00.000Z&timezone=browser&var-Project=8&var-Plot=1001&panelId=1&var-MoistureDepth=$__all&var-TempDepth=$__all&viewPanel=panel-1-clone-0&__feature.dashboardSceneSolo" width="900" height="400" frameborder="0"></iframe>
        """,
        unsafe_allow_html=True
    )

