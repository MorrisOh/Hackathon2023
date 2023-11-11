import streamlit as st
import leafmap.foliumap as leafmap
import numpy as np
import pandas as pd
from datetime import datetime
from datetime import time
# Data
# Read .csv with pandas
csv_file_path = 'data/raw/results_distribution.csv'
# Read the CSV file into a DataFrame
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
print(option)
map_df = df
# Check if option is not NULL or empty:
if not option:
    map_df = df
else:
    map_df = df[df['city'].isin(option)]
    # cams = // get all Cams from City
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

# Content
st.title("Heatmap")
MIN_MAX_RANGE = (lowest_date, highest_date)
PRE_SELECTED_DATES = (lowest_date, highest_date)

selected_min_date, selected_max_date = st.slider(
    "Select your preferred Date Range",
    value=PRE_SELECTED_DATES,
    min_value=MIN_MAX_RANGE[0],
    max_value=MIN_MAX_RANGE[1],
)

# Create Final DataFrame
# Convert 'datetime_column' to datetime objects

filtered_df = map_df[
    (map_df['date_column'] >= selected_min_date) & (map_df['date_column'] <= selected_max_date)
]


tab1, tab2 = st.tabs(["📈 Global", "🗃 Local"])
with tab1:
    st.subheader("Global")
    m = leafmap.Map(center=[49.123100,  9.210643], zoom=12)
    m.add_heatmap(
        data=filtered_df,
        latitude="latitude",
        longitude="longitude",
        value="total_count",
        name="Heat map",
        radius=20,
    )
    m.to_streamlit(height=700)

with tab2:
    st.subheader("Camera Heatmaps")
    st.image(
        "assets/heatmap.png",
    )






