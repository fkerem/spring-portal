import streamlit as st
import numpy as np
import pandas as pd
import re
from sklearn.linear_model import LinearRegression
from utils.img_formatting import image_to_base64_str

def createPage(session_state):
    st.markdown("## 🎮 SPRING Playground")

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    soil_moisture = [45, 50, 47, 49, 55, 60, 58]
    air_temperature = [29, 17, 20, 24, 25, 15, 30]  # lux

    df = pd.DataFrame({
        "Day": days,
        "Soil Moisture (%)": soil_moisture,
        "Air Temperature (°C)": air_temperature
    })

    game = st.selectbox("Choose a game to play:", [
        "🌞 Laughing Plant Monitor",
        "📊 Graph Generator",
        "🧩 SPRING Jigsaw"
    ])

    if game == "📊 Graph Generator":
        run_forecast_game(df)
    elif game == "🌞 Laughing Plant Monitor":
        run_happy_plant_game(df)
    elif game == "🧩 SPRING Jigsaw":
        run_spring_jigsaw()

# Tab version loads all games at once -- not good
#def createPage(session_state):
#    st.title("🌱 Plant Dashboard Games")
#
#    tab1, tab2 = st.tabs(["📊 Forecast Game", "🌞 Happy Plant Monitor"])
#
#    with tab1:
#        run_forecast_game(session_state)
#
#    with tab2:
#        run_happy_plant_game(session_state)

def run_happy_plant_game(df):
    st.markdown("##### Monitor the Plant")
    st.markdown("- Watch how your plant feels based on the sensor values, then adjust them to make it laugh!")
    
    soil_moisture = df["Soil Moisture (%)"].tolist()
    air_temp = df["Air Temperature (°C)"].tolist()

    # Normalize levels
    soil_level = int(np.clip(np.interp(soil_moisture[-1], [0, 100], [0, 10]), 0, 10))
    temp_level = int(np.clip(np.interp(air_temp[-1], [-50, 50], [0, 10]), 0, 10))

    # Custom bar drawer with color map
    def draw_bar(level, type):
        if type == "temp":
            # Cold (blue, hue 240) to hot (red, hue 0)
            hue = int(np.interp(level, [0, 10], [240, 0]))
        elif type == "moisture":
            # Dry (red, hue 0) to wet (blue, hue 240) — reversed
            hue = int(np.interp(level, [0, 10], [0, 240]))
        else:
            hue = 120  # fallback: green

        color = f"hsl({hue}, 85%, 45%)"
        return f"<span style='color:{color}; font-size: 24px; letter-spacing: 2px;'>" + ''.join(['█' if i < level else '░' for i in range(10)]) + "</span>"

    # Display actual sensor values
    col1, col2 = st.columns(2)
    with col1:
        st.metric("☀️ Air Temperature", f"{air_temp[-1]} °C")
        st.markdown(draw_bar(temp_level, "temp"), unsafe_allow_html=True)

    with col2:
        st.metric("💧 Soil Moisture", f"{soil_moisture[-1]}%")
        st.markdown(draw_bar(soil_level, "moisture"), unsafe_allow_html=True)

    st.markdown("##### Adjust the Conditions!")
    st.write("- Change the air temperature and soil moisture to see how your plant feels!")

    # User controls
    temp_input = st.slider("Air Temperature (°C)", -50, 50, air_temp[-1])
    sm_input = st.slider("Soil Moisture (%)", 0, 100, soil_moisture[-1])

    # Normalize input values to 0–10 scale
    sm_level = int(np.interp(sm_input, [0, 100], [0, 10]))
    temp_level = int(np.interp(temp_input, [-50, 50], [0, 10]))

    def predict_health(sm, temp):
        if (sm <= 2 or sm >= 9) and (temp <= 4 or temp >= 9):
            return "😭 Oh no, the plant is crying!", "images/crying-plant.png"
        elif (sm <= 3 or sm >= 9) or (temp <= 5 or temp >= 8):
            return "😟 The plant is sad!", "images/sad-plant.png"
        elif (sm <= 4 or sm >= 8) or (temp <= 6):
            return "😊 The plant is happy, make it laugh!", "images/happy-plant.png"
        elif (sm <= 6 or sm >= 7) or (temp == 7):
            return "😂 The plant is laughing! You made it!", "images/laughing-plant.png"

    # Final prediction
    message, img_path = predict_health(sm_level, temp_level)
    st.markdown("**🌿 Plant Status:**")
    #st.image(img_path, width=200, caption=message)
    # Center the image using a one-column layout
    b64_img = image_to_base64_str(img_path)
    st.markdown(
        f"""
        <div style='text-align: center;'>
            <img src='data:image/png;base64,{b64_img}' style='max-width: 25%; height: auto;' />
            <div style='font-weight: bold; margin-top: 0.5em;'>{message}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

def run_forecast_game(df):
    st.markdown("##### Experiment with the Data")
    st.markdown("- Adjust 7 days of air temperature and soil moisture data, then explore the generated graph. Share your insights on the trends!")

    #df = session_state.sensor_df
    days = df["Day"].tolist()  # e.g. ["Friday","Saturday",…] or ["Day 1","Day 2",…]
    soil_moisture = df["Soil Moisture (%)"].tolist()
    air_temperature = df["Air Temperature (°C)"].tolist()

    # — let user tweak the last N days
    modified_sm = []
    modified_at = []

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("##### Air Temperature")

    with c2:
        st.markdown("##### Soil Moisture")

    for i, day in enumerate(days):
        c1, c2 = st.columns(2)

        with c1:

            modified_at.append(
                st.slider(f"{day}", 0, 40, air_temperature[i], key=f"at_{i}")
            )

        with c2:

            modified_sm.append(
                st.slider(f"{day}", 0, 100, soil_moisture[i], key=f"sm_{i}")
            )


    # — build the “actual” DataFrame in the SAME order as days[]
    actual_df = pd.DataFrame({
        "Day": days,
        "Soil Moisture (%)": modified_sm,
        "Air Temperature (°C)": modified_at
    }).set_index("Day")

    # — helper to pull numbers out of "Day 8", "Day10", etc.
    def day_num(label):
        m = re.search(r"(\d+)", label)
        return int(m.group(1)) if m else float("inf")

    # — forecast prep
    n = len(modified_sm)                    # normally 7
    X_train = np.arange(n).reshape(-1, 1)   # 0…6
    X_future = np.arange(n, n+10).reshape(-1, 1)  # 7…16
    future_days = [f"Day {i+1}" for i in range(n, n+10)]

    # — soil moisture forecast
    sm_model = LinearRegression().fit(X_train, np.array(modified_sm))
    sm_pred  = sm_model.predict(X_future)

    # — st forecast
    at_model = LinearRegression().fit(X_train, np.array(modified_at))
    at_pred  = at_model.predict(X_future)

    # — build & sort the forecast DataFrame by day number
    forecast_df = pd.DataFrame({
        "Day": future_days,
        "Soil Moisture Forecast (%)": sm_pred,
        "Air Temperature Forecast (lux)": at_pred
    }).set_index("Day")
    forecast_df = forecast_df.loc[sorted(forecast_df.index, key=day_num)]

    # — now concatenate **without** re-sorting the actual days…
    combined = pd.concat([actual_df])

    # — but force pandas to keep THAT exact order on the x-axis
    full_order = list(actual_df.index)
    combined.index = pd.CategoricalIndex(full_order, categories=full_order, ordered=True)
    combined = combined.loc[full_order]  # reindex so the underlying DataFrame matches the categorical exactly

    st.markdown("📈 **Generated Line Graph**")
    st.line_chart(combined)


def run_spring_jigsaw():
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
        src="https://puzzleme.amuselabs.com/pmm/jigsaw?id=5dee3eee&set=6fd209c1b707d2ea7d9a73fff6d267b361bf1cc2d39099da8f73fd4fd346d1c1"
        aria-label="SPRING Jigsaw">
    </iframe>
    """, unsafe_allow_html=True)