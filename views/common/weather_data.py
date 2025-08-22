import streamlit as st

def createPage():

    st.subheader("☀️ Purdue Research Farm Weather Station Dashboard")

    st.markdown(
        """
        <style>
        .full-page-iframe {
            width: 100%;
            height: 4400px; /* You can adjust this value as needed */
            border: none;
            margin-top: 1rem;
        }
        </style>

        <iframe 
            class="full-page-iframe"
            src="https://dashboard.oats.ecn.purdue.edu/public-dashboards/04afe848746d4220a3352202d014859d"
            allowfullscreen
        ></iframe>
        """,
        unsafe_allow_html=True
    )