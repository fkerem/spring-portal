import io
import streamlit as st
import pandas as pd
from pytz import timezone

def filter_df(base, from_time, to_time):
    with open(f"{base}.csv", "rb") as file:
        df = pd.read_csv(file)

    if "Time (EDT)" in df.columns:
        df["Time (EDT)"] = pd.to_datetime(df["Time (EDT)"])
        eastern = timezone("America/New_York")
        from_dt = pd.to_datetime(from_time, utc=True).tz_convert(eastern).tz_localize(None)
        to_dt = pd.to_datetime(to_time, utc=True).tz_convert(eastern).tz_localize(None)
        df = df[(df["Time (EDT)"] >= from_dt) & (df["Time (EDT)"] < to_dt)]

    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    return df, csv_buffer

def _iso_utc(dt: pd.Timestamp) -> str:
    return dt.tz_convert("UTC").strftime("%Y-%m-%dT%H:%M:%S.000Z")

def adjust_from_for_boxplot(from_time: str, graph_type: str, date: str, duration: str) -> str:
    if graph_type != "Box Plot" or date != "July 9–22, 2025":
        return from_time
    base = pd.to_datetime(from_time, utc=True)
    if duration == "Last 1 Day":
        base = base - pd.Timedelta(minutes=30)
    else:
        base = base - pd.Timedelta(hours=12)
    return _iso_utc(base)

def get_bucket_type(duration: str, graph_type: str) -> str:
    if graph_type in ["Bar Chart", "Box Plot"]:
        if duration == "Last 1 Day":
            return "bucket_hourly"
        else:
            return "bucket_daily"
    return "data"

def get_data_filename(sensor_scope, modality, graph_type, bucket_type, excel=False):
    prefix = "lse01"
    sensor_scope = sensor_scope.lower().replace(" ", "_")
    modality = modality.lower().replace(" ", "_")
    graph_type = graph_type.lower().replace(" ", "_")
    option_excel_header = "-excel" if excel else ""
    return f"data/{prefix}-{sensor_scope}-{modality}-{graph_type}-{bucket_type}{option_excel_header}.csv"

def createPage():
    st.subheader("🌾 Farm Data")

    locations = ["Purdue Research Farm (West Lafayette, IN)", "KC Bailey Orchards, Inc. (New York)"]
    location = st.selectbox("Location", locations, index=0, key="location")

    # --- NYC Farm (only one graph for now) ---
    if location == "KC Bailey Orchards, Inc. (New York)":
        modalities = ["Soil Moisture"]
        sensors = ["Sensor 1"]
        graph_types = ["Line Graph"]
        dates = ["Live"]
        durations = ["Last 1 Day", "Last 1 Week", "Last 2 Weeks"]

        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            modality = st.selectbox("Modality", modalities, index=0, key="modality")
        with col2:
            date = st.selectbox("Date", dates, index=0, key="date")
        with col3:
            duration = st.selectbox("Duration", durations, index=0, key="duration")
        with col4:
            sensor = st.selectbox("Sensor Scope", sensors, index=0, key="sensor")
        with col5:
            graph_type = st.selectbox("Graph Type", graph_types, index=0, key="graph_type")

        if duration == "Last 1 Day":
            from_time = "now-1d"
            to_time = "now"
        elif duration == "Last 1 Week":
            from_time = "now-7d"
            to_time = "now"
        else:
            from_time = "now-14d"
            to_time = "now"

        st.markdown("### Sensor-1 Soil Moisture (KC Bailey Orchards, Inc. (New York))")
        st.markdown(
            f"""
            <iframe src="https://oats.ecn.purdue.edu/d-solo/e24986f4-9af2-4d1b-9277-f2d68663c54b/dashboard-agbridge?orgId=2&from={from_time}&to={to_time}&timezone=edt&panelId=13&viewPanel=panel-13&__feature.dashboardSceneSolo"
                style="width: 100%; height: 400px;"
                frameborder="0"></iframe>
            """,
            unsafe_allow_html=True
        )
        return

    # --- Purdue Research Farm ---
    modalities = ["Soil Moisture", "Soil Temperature", "All"]
    sensors = ["Sensor 1", "25 Sensors", "All"]
    graph_types = ["Line Graph", "Bar Chart", "Histogram", "Box Plot"]
    dates = ["Live", "July 9–22, 2025", "All"]
    durations = ["Last 1 Day", "Last 1 Week", "Last 2 Weeks"]

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        modality = st.selectbox("Modality", modalities, index=0, key="modality-purdue")
    with col2:
        date = st.selectbox("Date", dates, index=0, key="date-purdue")
    with col3:
        duration = st.selectbox("Duration", durations, index=2, key="duration-purdue")
    with col4:
        sensor = st.selectbox("Sensor Scope", sensors, index=0, key="sensor-purdue")
    with col5:
        graph_type = st.selectbox("Graph Type", graph_types, index=0, key="graph_type-purdue")

    special_bucket_key = "1D"
    panel_ids = {
        "Line Graph": {
            ("Soil Moisture", "Live", "Sensor 1"): 60,
            ("Soil Moisture", "Live", "25 Sensors"): 58,
            ("Soil Moisture", "July 9–22, 2025", "Sensor 1"): 60,
            ("Soil Moisture", "July 9–22, 2025", "25 Sensors"): 58,
            ("Soil Temperature", "Live", "Sensor 1"): 61,
            ("Soil Temperature", "Live", "25 Sensors"): 59,
            ("Soil Temperature", "July 9–22, 2025", "Sensor 1"): 61,
            ("Soil Temperature", "July 9–22, 2025", "25 Sensors"): 59,
        },
        "Bar Chart": {
            ("Soil Moisture", "Live", "Sensor 1"): 62,
            ("Soil Moisture", "Live", "25 Sensors"): 64,
            ("Soil Moisture", "July 9–22, 2025", "Sensor 1"): 62,
            ("Soil Moisture", "July 9–22, 2025", "25 Sensors"): 64,
            ("Soil Moisture", special_bucket_key, "Sensor 1"): 66,
            ("Soil Moisture", special_bucket_key, "25 Sensors"): 68,
            ("Soil Temperature", "Live", "Sensor 1"): 63,
            ("Soil Temperature", "Live", "25 Sensors"): 65,
            ("Soil Temperature", "July 9–22, 2025", "Sensor 1"): 63,
            ("Soil Temperature", "July 9–22, 2025", "25 Sensors"): 65,
            ("Soil Temperature", special_bucket_key, "Sensor 1"): 67,
            ("Soil Temperature", special_bucket_key, "25 Sensors"): 69,
        },
        "Histogram": {
            ("Soil Moisture", "Live", "Sensor 1"): 72,
            ("Soil Moisture", "Live", "25 Sensors"): 70,
            ("Soil Moisture", "July 9–22, 2025", "Sensor 1"): 72,
            ("Soil Moisture", "July 9–22, 2025", "25 Sensors"): 70,
            ("Soil Temperature", "Live", "Sensor 1"): 73,
            ("Soil Temperature", "Live", "25 Sensors"): 71,
            ("Soil Temperature", "July 9–22, 2025", "Sensor 1"): 73,
            ("Soil Temperature", "July 9–22, 2025", "25 Sensors"): 71,
        },
        "Box Plot": {
            ("Soil Moisture", "Live", "Sensor 1"): 76,
            ("Soil Moisture", "Live", "25 Sensors"): 74,
            ("Soil Moisture", "July 9–22, 2025", "Sensor 1"): 76,
            ("Soil Moisture", "July 9–22, 2025", "25 Sensors"): 74,
            ("Soil Moisture", special_bucket_key, "Sensor 1"): 77,
            ("Soil Moisture", special_bucket_key, "25 Sensors"): 75,
            ("Soil Temperature", "Live", "Sensor 1"): 80,
            ("Soil Temperature", "Live", "25 Sensors"): 78,
            ("Soil Temperature", "July 9–22, 2025", "Sensor 1"): 80,
            ("Soil Temperature", "July 9–22, 2025", "25 Sensors"): 78,
            ("Soil Temperature", special_bucket_key, "Sensor 1"): 81,
            ("Soil Temperature", special_bucket_key, "25 Sensors"): 79,
        },
    }

    m_list = [m for m in modalities if m != "All"] if modality == "All" else [modality]
    d_list = [d for d in dates if d != "All"] if date == "All" else [date]
    s_list = [s for s in sensors if s != "All"] if sensor == "All" else [sensor]

    graph_keys = []
    for m in m_list:
        for d in d_list:
            for s in s_list:
                lookup_key = (m, d, s)
                if duration == "Last 1 Day" and d in ["Live", "July 9–22, 2025"] and graph_type in ["Bar Chart", "Box Plot"]:
                    lookup_key = (m, special_bucket_key, s)
                if lookup_key in panel_ids[graph_type]:
                    graph_keys.append((m, d, s))

    single_graph = len(graph_keys) == 1

    for m, d, s in graph_keys:
        lookup_key = (m, d, s)
        if duration == "Last 1 Day" and d in ["Live", "July 9–22, 2025"] and graph_type in ["Bar Chart", "Box Plot"]:
            lookup_key = (m, special_bucket_key, s)

        panel_id = panel_ids[graph_type][lookup_key]

        # Base window
        if d == "Live":
            if duration == "Last 1 Day":
                from_time = "now-1d"
                to_time = "now"
            elif duration == "Last 1 Week":
                from_time = "now-7d"
                to_time = "now"
            else:
                from_time = "now-14d"
                to_time = "now"
        else:
            if duration == "Last 1 Day":
                from_time = "2025-07-22T04:00:00.000Z"
                to_time = "2025-07-23T04:00:00.000Z"
            elif duration == "Last 1 Week":
                from_time = "2025-07-16T04:00:00.000Z"
                to_time = "2025-07-23T04:00:00.000Z"
            else:
                from_time = "2025-07-09T04:00:00.000Z"
                to_time = "2025-07-23T04:00:00.000Z"

        # Adjust fixed-date Box Plot start so the first box is full
        effective_from_time = adjust_from_for_boxplot(from_time, graph_type, d, duration)

        with st.expander(f"{graph_type}: {m} - {s} - {d} ({duration})", expanded=single_graph):
            st.markdown(
                f"""
                <iframe src="https://dashboard.oats.ecn.purdue.edu/d-solo/e69f4933-d92a-4cfc-956a-020c850bf4b9/soil-sensors-agbridge?orgId=1&from={effective_from_time}&to={to_time}&timezone=edt&var-Project=8&panelId={panel_id}&viewPanel=panel-{panel_id}&__feature.dashboardSceneSolo"
                    style="width: 100%; height: 400px;"
                    frameborder="0"></iframe>
                """,
                unsafe_allow_html=True
            )

            if d == "July 9–22, 2025":
                with st.expander("📄 Raw Data & Downloads", expanded=single_graph):

                    bucket_type = get_bucket_type(duration, graph_type)
                    file_base = get_data_filename(s, m, graph_type, bucket_type, excel=False).replace(".csv", "")
                    file_excel = get_data_filename(s, m, graph_type, bucket_type, excel=True)

                    try:
                        # Use the same adjusted window for CSV filtering
                        df, csv_buffer = filter_df(file_base, effective_from_time, to_time)
                        st.download_button(
                            label="📥 Download CSV",
                            data=csv_buffer.getvalue(),
                            file_name=file_base.split("/")[-1] + ".csv",
                            mime="text/csv",
                            key=f"{file_base}-std"
                        )

                        _, excel_buffer = filter_df(file_base + "-excel", effective_from_time, to_time)
                        st.download_button(
                            label="📥 Download CSV for Excel",
                            data=excel_buffer.getvalue(),
                            file_name=file_excel.split("/")[-1],
                            mime="text/csv",
                            key=f"{file_base}-excel"
                        )

                        st.markdown("#### 👀 Data Preview (first 10 rows)")
                        st.dataframe(df.head(10), use_container_width=True)
                    except FileNotFoundError:
                        st.warning(f"⚠️ Data file not found for {m}, {s}, {d}.")