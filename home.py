from pathlib import Path
import PIL
import streamlit as st
import src.settings as settings
import src.helper as helper
from ultralytics import YOLO

# Setting page layout
st.set_page_config(
    page_title="Object Detection using YOLOv8",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main page heading
st.title("Pedestrian Detection")

# Sidebar
st.sidebar.header("ML Model Config")

# Model Options
model_type = st.sidebar.radio(
    "Select Task", ['Detection', 'Segmentation'])

confidence = float(st.sidebar.slider(
    "Select Model Confidence", 25, 100, 40)) / 100

# Selecting Detection Or Segmentation
if model_type == 'Detection':
    model = YOLO('yolov8s.pt')
elif model_type == 'Segmentation':
    model = YOLO('yolov8x-seg.pt')


st.sidebar.header("Config")
source_radio = st.sidebar.radio(
    "Select Source", settings.SOURCES_LIST)

if source_radio == settings.WEBCAM:
    helper.play_webcam(confidence, model)

elif source_radio == settings.RTSP:
    helper.play_rtsp_stream(confidence, model)

elif source_radio == settings.YOUTUBE:
    helper.play_youtube_video(confidence, model)

else:
    st.error("Please select a valid source type!")