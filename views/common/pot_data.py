import streamlit as st

def createPage():
    st.subheader("🪴 Classroom Corn Pot Dashboard")

    st.markdown(
        """
        <style>
        .full-page-iframe {
            width: 100%;
            height: 2000px; /* Adjust as needed */
            border: none;
            margin-top: 1rem;
        }
        </style>

        <iframe 
            class="full-page-iframe"
            src="https://dashboard.oats.ecn.purdue.edu/d/35e51d63-fe4f-4a6e-8072-bf46fa66310b/soil-sensors-agbridge-pot?orgId=1&from=now-12h&to=now&timezone=browser&var-Project=$__all&var-Plot=$__all&var-MoistureDepth=$__all&var-TempDepth=$__all"
            allowfullscreen
        ></iframe>
        """,
        unsafe_allow_html=True
    )