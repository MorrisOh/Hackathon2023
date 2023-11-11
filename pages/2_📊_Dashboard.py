import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards
import pandas as pd
import numpy as np
import datetime

# Sidebar
st.sidebar.header("Detail Location View")
option = st.sidebar.selectbox(
   "Which City do you want to select?",
   ("Heilbronn", "Hoelle", "Wakanda"),
   index=None,
   placeholder="Please select City....",
)
# Check if option is not NULL or empty:
if option is not None:
    # cams = // get all Cams from City
    model_type = st.sidebar.radio(
        "Select Location", ['FFK Club', 'Heilbronn Shower'])

# KPI-Header
# Define Column Count
col1, col2, col3 = st.columns(3)

# Define Column Content


# Define Column Content Display
col1.metric(label="Durchschnitt - 1 Tag", value=5000, delta=1000)
col2.metric(label="Durchschnitt - 12 h", value=5000, delta=-1000)
col3.metric(label="Durchschnitt - ALL", value=5000, delta=0)

# Render Metric Cards
style_metric_cards()

# Bar Chart
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.bar_chart(chart_data)

MIN_MAX_RANGE = (datetime.datetime(2022,1,1), datetime.datetime(2023,7,1))
PRE_SELECTED_DATES = (datetime.datetime(2023,1,1), datetime.datetime(2023,7,1))

selected_min, selected_ax = st.slider(
    "Datetime slider",
    value=PRE_SELECTED_DATES,
    min_value=MIN_MAX_RANGE[0],
    max_value=MIN_MAX_RANGE[1],
)

