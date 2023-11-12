import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards
import pandas as pd
import numpy as np
import datetime
from datetime import time
import src.settings as settings

csv_file_path = settings.PEDESTRIAN_DISTRIBUTION

df = pd.read_csv(csv_file_path, sep=';')
# Find unique Values
unique_cities = df['city'].unique()

# Find the lowest and highest dates
#lowest_date = datetime.strptime(df['date_time'].min(), '%d.%m.%y %H:%M')
#highest_date = datetime.strptime(df['date_time'].max(), '%d.%m.%y %H:%M')

# Convert 'datetime_column' to a datetime object
df['date_time'] = pd.to_datetime(df['date_time'], format='%d.%m.%y %H:%M')

# Split datetime column into date and time columns
df['date_column'] = df['date_time'].dt.date
df['time_column'] = df['date_time'].dt.time

lowest_date = df['date_column'].min()
highest_date = df['date_column'].max()



# Sidebar
st.sidebar.header("Detail Location View")
option = st.sidebar.multiselect(
   "Which City do you want to select?",
   options = unique_cities,
)
map_df = df
# Check if option is not NULL or empty:
if not option:
    map_df = df
else:
    map_df = df[df['city'].isin(option)]
    unique_location = map_df['location'].unique()
    model_type = st.sidebar.multiselect(
        "Select Location", unique_location)
    if not model_type:
        map_df = df
    else:
        map_df = df[df['location'].isin(model_type)]
    
clock_range = st.sidebar.slider(
    "Choose a time range",
    value=(time(00, 00), time(23, 59)))

MIN_MAX_RANGE = (lowest_date, highest_date)
PRE_SELECTED_DATES = (lowest_date, highest_date)

selected_min_date, selected_max_date = st.slider(
    "Select your preferred Date Range",
    value=PRE_SELECTED_DATES,
    min_value=MIN_MAX_RANGE[0],
    max_value=MIN_MAX_RANGE[1],
)

filtered_df = map_df[
    (map_df['date_column'] >= selected_min_date) & (map_df['date_column'] <= selected_max_date)
]

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
chart_data = filtered_df
st.bar_chart(data=chart_data, x='date_time',y='total_count')




