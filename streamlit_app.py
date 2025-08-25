import streamlit as st
import pandas as pd
import base64
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html

import importlib
import inspect

from utils.navigation import navigate_to
from utils.img_formatting import image_to_base64_str

from streamlit_scroll_to_top import scroll_to_here

# Inject scroll-to-top once if flagged
if st.session_state.pop("_scroll_to_top", False):
    #st.markdown("<a name='top'></a>", unsafe_allow_html=True)
    #st.markdown("<meta http-equiv='refresh' content='0; URL=#top'>", unsafe_allow_html=True)
    scroll_to_here(0, key='header')


# Get current route from URL
current_user = st.query_params.get("user", "student")
current_page = st.query_params.get("page", "home")
current_module = st.query_params.get("lesson")  # optional

logo_b64 = image_to_base64_str("logos/logo.png")
logo_iot4ag_b64 = image_to_base64_str("logos/iot4ag.png")
#logo_purdue_dark_b64 = image_to_base64_str("logos/purdue-darkmode.png")
#logo_purdue_light_b64 = image_to_base64_str("logos/purdue-lightmode.png")
#logo_nsf_dark_b64 = image_to_base64_str("logos/nsf-darkmode.png")
#logo_nsf_light_b64 = image_to_base64_str("logos/nsf-lightmode.png")

theme_base = st.context.theme.type
#print("Selected theme:", theme_base)

if theme_base == "light":
    logo_purdue_b64 = image_to_base64_str("logos/purdue-lightmode.png")
    logo_nsf_b64 = image_to_base64_str("logos/nsf-lightmode.png")
    #print("Light mode logos:", logo_purdue_b64[:30], logo_nsf_b64[:30])  # Print first 30 characters for brevity
else:
    logo_purdue_b64 = image_to_base64_str("logos/purdue-darkmode.png")
    logo_nsf_b64 = image_to_base64_str("logos/nsf-darkmode.png")
    #print("Dark mode logos:", logo_purdue_b64[:30], logo_nsf_b64[:30])

logo_asu_b64 = image_to_base64_str("logos/asu.png")
logo_ucmerced_b64 = image_to_base64_str("logos/ucmerced.png")
logo_uflorida_b64 = image_to_base64_str("logos/uflorida.png")
logo_upenn_b64 = image_to_base64_str("logos/upenn.png")

# 1) Read & Base64‐encode your logo
#with open("logos/logo.png", "rb") as f:
#    logo_b64 = base64.b64encode(f.read()).decode()

# Read from Streamlit config
base_path = st.get_option("server.baseUrlPath") or ""
base_path = base_path.strip("/")  # remove leading/trailing slashes

# Construct the link
href = f"/{base_path}" if base_path else "/"

st.set_page_config(page_title="SPRING Portal", layout="wide", initial_sidebar_state="expanded")

header_bg_color = "#ffffff" if theme_base == "light" else "#0e1117"
header_text_color = "#000000" if theme_base == "light" else "#f1f1f1"

html(f"""
<script>
(function() {{
  const parent = window.parent.document;

  const style = parent.createElement('style');
  style.textContent = `
    :root {{
      --sidebar-w: 250px;
      --hdr-h: 4rem;
      --bg-color: {header_bg_color};
    }}

    iframe[data-testid="stIFrame"] {{
      display: none !important;
      height: 0 !important;
      width: 0 !important;
      opacity: 0 !important;
      pointer-events: none !important;
    }}


    /* ─── TOOLBAR FIX ────────────────────────────────────────────── */
    /* Disable toolbar interference with sidebar */
    [data-testid="stToolbar"] {{
      pointer-events: none !important;
    }}
    
    /* Re-enable pointer events for toolbar buttons */
    [data-testid="stToolbar"] button {{
      pointer-events: auto !important;
    }}
    
    [data-testid="stToolbar"] [data-testid="stMainMenu"] {{
      pointer-events: auto !important;
    }}
    
    [data-testid="stToolbar"] [data-testid="stAppDeployButton"] {{
      pointer-events: auto !important;
    }}

    .fixed-header {{
      position: fixed;
      top: 0; left: 0;
      width: 100%;
      height: var(--hdr-h);
      background: var(--bg-color);
      box-shadow: 0 2px 5px rgba(0,0,0,0.3);
      z-index: 2147483645;
      display: flex;
      align-items: center;
      padding: 0 1rem;
      pointer-events: none;
    }}

    .fixed-header * {{
      pointer-events: auto;
    }}



    .fixed-header .sidebar-logo-container {{
      width: var(--sidebar-w);
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .fixed-header .sidebar-logo-container img {{
      height: 60px;
      max-height: 100%;
    }}

    .fixed-header h2 {{
      position: absolute;
      top: 50%; left: 50%;
      transform: translate(-50%, -50%);
      margin: 0;
      color: {header_text_color};
      font-size: 2rem;
      pointer-events: none;
    }}

    .fixed-header .footer-logos-container {{
      margin-left: auto;
      display: flex;
      align-items: center;
      gap: 1rem;
    }}

    .fixed-header .footer-logos-container img {{
      height: 26px;
    }}

    .fixed-header .footer-logos-container img[alt="NSF Logo"] {{
        height: 40px;
    }}

    [data-testid="stAppViewContainer"] {{
      margin-top: var(--hdr-h) !important;
    }}



    /* Target the specific sidebar content area */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {{
      margin-top: -2rem !important;
    }}

    .stMainBlockContainer {{
      padding-top: 1rem;
    }}

    .stAppHeader {{
      background-color: rgba(255, 255, 255, 0.0);
      visibility: visible;
    }}

    /* ─── Responsive Mobile Fixes ───────────────────────────── */
    /* ─── Mobile: stack title, keep logos in ONE ROW ───────────────── */
    @media (max-width: 767.98px) {{
      .fixed-header {{
        flex-direction: column;
        align-items: flex-start;
        height: auto;
        padding: 0.5rem 1rem;
      }}

      .fixed-header h2 {{
        position: static;
        transform: none;
        font-size: 1.2rem;
        margin: 0.5rem 0;
        text-align: center;
        width: 100%;
      }}

      .fixed-header .sidebar-logo-container {{
        justify-content: flex-start;
        width: 100%;
        margin-bottom: 0.5rem;
      }}

      .fixed-header .footer-logos-container {{
        width: 100%;
        display: flex;
        align-items: center;
        /* keep them on ONE line */
        flex-wrap: nowrap;
        gap: 0.4rem;
        justify-content: center;
        /* if they still don't fit, allow gentle horizontal scroll */
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
        white-space: nowrap;
        padding-bottom: 0.25rem;
      }}

      /* unify ALL logo heights on mobile, including NSF */
      .fixed-header .footer-logos-container img {{
        height: 26px !important;  /* beats the NSF attribute rule */
        width: auto;
        flex: 0 0 auto;
      }}

      /* bump page content down under fixed header */
      [data-testid="stAppViewContainer"] {{
        margin-top: 11rem !important;
      }}

      /* float the expand button */
      [data-testid="stSidebarExpandButton"] {{
        position: fixed !important;
        top: 1rem !important;
        left: 1rem !important;
        z-index: 2147483648 !important;
        background-color: var(--bg-color) !important;
        border-radius: 4px;
        padding: 0.2rem;
      }}
    }}

    /* ─── Tablet: progressive hide (no overlap with mobile) ─────────── */
    @media (min-width: 768px) and (max-width: 1050px) {{
      .fixed-header .footer-logos-container img:nth-child(3) {{
        display: none !important;
      }}
    }}

    @media (min-width: 768px) and (max-width: 850px) {{
      .fixed-header .footer-logos-container img:nth-child(2) {{
        display: none !important;
      }}
    }}
  `;
  parent.head.appendChild(style);

  // ─── Header Build ─────────────────────────────────────────────
  // Remove any existing header first
  const existingHeader = parent.querySelector('.fixed-header');
  if (existingHeader) {{
    existingHeader.remove();
  }}
  
  const header = parent.createElement('header');
  header.className = 'fixed-header';
  header.innerHTML = `
    <div class="sidebar-logo-container">
      <a href="{href}" title="Home" aria-label="SPRING Home">
        <img src="data:image/png;base64,{logo_b64}" alt="Logo">
      </a>
    </div>
    <h2>SPRING Portal</h2>
    <div class="footer-logos-container">
      <img src="data:image/png;base64,{logo_purdue_b64}" alt="Purdue Logo">
      <img src="data:image/png;base64,{logo_iot4ag_b64}" alt="IoT4Ag Logo">
      <img src="data:image/png;base64,{logo_nsf_b64}" alt="NSF Logo">
    </div>
  `;
  parent.body.prepend(header);
}})();
</script>
""", height=0)

# Simulated sensor data
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
soil_moisture = [45, 50, 47, 49, 55, 60, 58]         # %
optical_intensity = [200, 180, 190, 220, 240, 250, 245]  # lux

df = pd.DataFrame({
    "Day": days,
    "Soil Moisture (%)": soil_moisture,
    "Optical Sensor (lux)": optical_intensity
})

# Initialization
if 'sensor_df' not in st.session_state:
    st.session_state.sensor_df = df

# ─── Sidebar: Role & Section Selection ────────────────────────────────
user_roles = {
    #"👶 Young Student": "young-student",
    #"🧑‍🎓 High School": "high-school",
    "🧑‍🎓 Student": "student",
    "👩‍🏫 Teacher": "teacher",
    "🕵️‍♂️ Public Audience": "public"
}

options_by_role = {
    #"👶 Young Student": ["Visual", "Raw Data", "Additional Graphs", "Playground", "Photos", "Learn"],
    #"🧑‍🎓 High School": ["Visual", "Raw Data", "Additional Graphs", "Playground", "Photos", "Location", "Learn", "Exercises"],
    "🧑‍🎓 Student": ["Home", "Lessons", "Pot Data", "Farm Data", "Weather Data", "Photos", "Location", "Tutorials", "Playground"],
    "👩‍🏫 Teacher": ["Home", "Module", "Pot Data", "Farm Data", "Weather Data", "Photos", "Location", "Tutorials", "Notes"],
    "🕵️‍♂️ Public Audience": ["Home", "Pot Data", "Farm Data", "Weather Data", "Photos", "Location", "Tutorials"]
}

icon_map = {
    "Home": "house",
    "Lessons": "book",
    "Module": "book",
    "Pot Data": "box",
    "Farm Data":"tree",
    "Weather Data":"sun",
    "Playground": "controller",
    "Photos": "image",
    "Location": "geo-alt",
    "Notes": "pencil-square",
    "Tutorials": "play-circle"
}

if theme_base == "light":
    menu_styles = {
        "container": {"padding": "0!important", "background-color": "#ffffff"},
        "icon": {"color": "#333", "font-size": "16px"},
        "nav-link": {
            "color": "#333",
            "font-size": "14px",
            "text-align": "left",
            "margin": "5px 0",
            "--hover-color": "#f0f0f0"
        },
        "nav-link-selected": {
            "background-color": "#e6e6e6",
            "color": "#000",
            "font-weight": "600"
        }
    }
else:
    menu_styles = {
        "container": {"padding": "0!important", "background-color": "#0e1117"},
        "icon": {"color": "white", "font-size": "16px"},
        "nav-link": {
            "color": "white",
            "font-size": "14px",
            "text-align": "left",
            "margin": "5px 0",
            "--hover-color": "#44475a"
        },
        "nav-link-selected": {
            "background-color": "#373a40"
        }
    }

# ─── Map Section Names to Page Filenames ──────────────────────────────
filename_map = {
    "Home": "home",
    "Lessons": "lessons",
    "Module": "module",
    "Pot Data": "pot_data",
    "Farm Data": "farm_data",
    "Weather Data": "weather_data",
    "Playground": "playground",
    "Photos": "photos",
    "Location": "location",
    "Notes": "notes",
    "Tutorials": "tutorials"
}

emoji_map = {
    "Home": "🏠",
    "Lessons": "📚",
    "Module": "📚",
    "Pot Data": "🪴",
    "Farm Data": "🌾",
    "Weather Data": "☀️",
    "Playground": "🎮",
    "Photos": "🖼️",
    "Location": "📍",
    "Notes": "🗒️",
    "Tutorials": "🎯"
}

# ─── Common Sections ────────────────────────────────────────────────
common_sections = {
    "Home", "Pot Data", "Farm Data", "Weather Data", "Photos", "Location", "Tutorials"
}

with st.sidebar:
    st.markdown("## 👥 Select User Role")
    #selected_label = st.selectbox("Choose your role:", list(user_roles.keys()))
    selected_label = st.selectbox(
        "Choose your role:",
        list(user_roles.keys()),
        index=list(user_roles.values()).index(current_user)  # ensures it matches the URL
    )
    options = options_by_role[selected_label]
    icons = [icon_map[opt] for opt in options]

    default_section = next((k for k, v in filename_map.items() if v == current_page and k in options), options[0])

    section = option_menu(
        menu_title=None,
        options=options,
        icons=icons,
        #default_index=options.index([k for k, v in filename_map.items() if v == current_page][0]),
        default_index=options.index(default_section),
        orientation="vertical",
        styles=menu_styles
    )

    svg_base64 = image_to_base64_str("images/logo-youtube.svg")

    if theme_base == "light":
        yt_text_color = "black"
        yt_underline_color = "green"
    else:
        yt_text_color = "white"
        yt_underline_color = "green"

    st.markdown(f"""
        <div style="text-align: center; margin-top: 2rem;">
            <a href="https://youtube.com/@iot4agspring?si=a48TrReVapcr4FGN" target="_blank" style="text-decoration: none;">
                <img src="data:image/svg+xml;base64,{svg_base64}" alt="YouTube" style="height:40px;"><br>
                <span style="
                    display: inline-block;
                    margin-top: 0.4rem;
                    font-size: 15px;
                    font-weight: 600;
                    letter-spacing: 0.3px;
                    color: {yt_text_color};
                    text-decoration: underline;
                    text-decoration-color: {yt_underline_color};
                    line-height: 1.4;
                ">
                    Watch Tutorials<br>on YouTube
                </span>
            </a>
        </div>
    """, unsafe_allow_html=True)



# ─── Define Selected Page Path Based on Role or Common ──────────────
selected_user = user_roles[selected_label]
selected_filename = filename_map[section]

# Determine which view module to actually load
if section in common_sections:
    actual_view_user = "common"
else:
    actual_view_user = selected_user

#print(selected_page_path)

# Check if navigation is needed
#if current_user != selected_user or current_page != selected_filename:
#    navigate_to(user=selected_user, page=selected_filename)
#    st.stop()  # stop execution after rerun trigger

if selected_user != "student" and selected_filename != "lessons":
    st.session_state.pop("selected_module_key", None)
    st.session_state.pop("selected_module_path", None)

module_key = st.session_state.get("selected_module_key")
if (
    current_user != selected_user or
    current_page != selected_filename or
    (selected_filename == "lessons" and current_module != module_key and module_key is not None)
):
    navigate_to(st.session_state, user=selected_user, page=selected_filename, module=module_key)
    #st.stop()

# Call the createPage() function for the selected view
view_map = {
    "student": "views.student",
    "teacher": "views.teacher",
    "common": "views.common",
    "public": "views.public"
}


if actual_view_user not in view_map:
    st.error("Unknown user role")
else:
    module_path = f"{view_map[actual_view_user]}.{selected_filename}"
    page_module = importlib.import_module(module_path)
    create_func = getattr(page_module, "createPage")
    if len(inspect.signature(create_func).parameters) == 1:
        create_func(st.session_state)
    else:
        create_func()

#selected_page = st.Page(selected_page_path, title=section, icon=emoji_map[section])

# ─── Register and Run Navigation ────────────────────────────────────
#pg = st.navigation([selected_page])
#pg.run()

# ─── Static footer in normal flow ─────────────────────────────────────
footer_bg = "#ffffff" if theme_base == "light" else "#0e1117"
footer_text = "#000000" if theme_base == "light" else "#f1f1f1"

st.markdown(
    f"""
    <style>
      .page-footer {{
        width: 100%;
        background: {footer_bg};
        color: {footer_text};
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 1rem 1rem 0.8rem 1rem;
        box-shadow: 0 -2px 5px rgba(0,0,0,0.1);
        margin-top: 2rem;
        gap: 0.5rem;
      }}
      .page-footer .footer-text {{
        font-size: 0.9rem;
        text-align: center;
      }}
      .page-footer .footer-logos {{
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
        gap: 1rem;
        width: 100%;
        max-width: 900px;
      }}
      .page-footer .footer-logos img {{
        height: 35px;
        max-height: 100%;
        max-width: 100px;
        width: auto;
        flex: 1 1 70px;
        object-fit: contain;
      }}

      @media (max-width: 700px) {{
        .page-footer .footer-logos img {{
          height: 28px;
          flex: 1 1 50px;
        }}
      }}
    </style>

    <div class="page-footer">
      <span class="footer-text">© 2025 SPRING Portal</span>
      <div class="footer-logos">
        <img src="data:image/png;base64,{logo_purdue_b64}" alt="Purdue Logo">
        <img src="data:image/png;base64,{logo_upenn_b64}" alt="UPenn Logo">
        <img src="data:image/png;base64,{logo_ucmerced_b64}" alt="UCMERCED Logo">
        <img src="data:image/png;base64,{logo_uflorida_b64}" alt="UFlorida Logo">
        <img src="data:image/png;base64,{logo_asu_b64}" alt="ASU Logo">
        <img src="data:image/png;base64,{logo_iot4ag_b64}" alt="IoT4Ag Logo">
        <img src="data:image/png;base64,{logo_nsf_b64}" alt="NSF Logo">
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)


