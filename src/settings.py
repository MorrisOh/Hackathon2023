from pathlib import Path
import sys
from ultralytics import YOLO

# Get the absolute path of the current file
file_path = Path(__file__).resolve()

# Get the parent directory of the current file
root_path = file_path.parent

# Add the root path to the sys.path list if it is not already there
if root_path not in sys.path:
    sys.path.append(str(root_path))

# Get the relative path of the root directory with respect to the current working directory
ROOT = root_path.relative_to(Path.cwd())

# Sources
WEBCAM = 'Webcam'
YOUTUBE = 'YouTube'
VIDEO = 'Video'

SOURCES_LIST = [WEBCAM, YOUTUBE, VIDEO]

# Videos config
VIDEO_DIR = root_path / 'data/raw/'

# Define video paths dynamically based on the script's location
VIDEO_1_PATH = 'data/raw/test_video.mov'
VIDEO_2_PATH = 'data/raw/GX010650.MP4'
VIDEO_3_PATH = 'data/raw/video_3.mp4'

VIDEOS_DICT = {
    'test_video': VIDEO_1_PATH,
    'Fruehstuck': VIDEO_2_PATH,
    'video_3': VIDEO_3_PATH,
}


# ML Model config
DETECTION_MODEL = YOLO('yolov8s.pt')
SEGMENTATION_MODEL = YOLO('yolov8n-seg.pt')

# Webcam
WEBCAM_PATH = 0