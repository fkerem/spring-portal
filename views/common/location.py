import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium
from geopy.geocoders import Nominatim

# Cache geocoding so we don’t hit the free OSM service repeatedly
@st.cache_data(show_spinner=False)
def geocode(address: str):
    geolocator = Nominatim(user_agent="spring-portal/1.0 (contact@example.com)")
    return geolocator.geocode(address, timeout=10)

def createPage():
    st.set_page_config(layout="wide")
    st.subheader("📍 You are invited to Purdue Research Farm!")

    st.markdown("""
	    Thank you for your interest in our portal! To schedule a visit to the Purdue Research Farm, please contact us at [info@oatscenter.org](mailto:info@oatscenter.org).
	""")

    # Default (your coordinates)
    default_name = "Purdue Research Farm - High Bay"
    default_lat, default_lon = 40.470342, -86.994823

    # Optional address search (free via OpenStreetMap Nominatim)
    #address = st.text_input("Find by address (optional):", "Purdue University, West Lafayette, IN")
    #if address.strip():
    #    try:
    #        g = geocode(address.strip())
    #        if g:
    #            default_lat, default_lon = g.latitude, g.longitude
    #            default_name = g.address
    #    except Exception as e:
    #        st.info(f"Couldn’t geocode that address ({e}). Using default location.")

    # Build the map (OpenStreetMap tiles are free)
    m = folium.Map(location=[default_lat, default_lon], zoom_start=14, tiles="OpenStreetMap")

    # Pretty marker with popup + directions link (OSM)
    popup_html = f"""
        <b>{default_name}</b><br>
        4530 US-52, West Lafayette, IN 47906 <br>
        Lat: {default_lat:.5f}, Lon: {default_lon:.5f}<br>
        <a href="https://maps.app.goo.gl/CDMuAz1JUpKnsggi8" target="_blank">
            Google Maps Directions
        </a>
    """
    folium.CircleMarker(
        location=[default_lat, default_lon],
        radius=10,
        color="#2E86DE",
        fill=True,
        fill_opacity=0.7,
        popup=folium.Popup(popup_html, max_width=300),
        tooltip=default_name,
    ).add_to(m)

    # Optional: allow users to switch to a terrain-style base (also free)
    # folium.TileLayer('Stamen Terrain').add_to(m)  # comment in if you want an alt layer
    folium.LayerControl().add_to(m)

    st_folium(m, use_container_width=True, height=520)
