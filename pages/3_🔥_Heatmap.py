import streamlit as st
import leafmap.foliumap as leafmap
import numpy as np
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

st.sidebar.info(
   "Let's go Wakanda!"
)

# Content
st.title("Heatmap")
tab1, tab2 = st.tabs(["📈 Global", "🗃 Local"])
with tab1:
    st.subheader("Global")
    filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
    m = leafmap.Map(center=[40, -100], zoom=4)
    m.add_heatmap(
        filepath,
        latitude="latitude",
        longitude="longitude",
        value="pop_max",
        name="Heat map",
        radius=20,
    )
    m.to_streamlit(height=700)

with tab2:
    st.subheader("Camera Heatmaps")
    st.image(
        "assets/heatmap.png",
    )






