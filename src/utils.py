from ultralytics import YOLO

import logging


def get_model(path: str = 'yolov8s.pt'):
    return YOLO(path)


def get_logger(log_level=logging.INFO):
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=log_level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    return logger
