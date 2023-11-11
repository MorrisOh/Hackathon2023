import torch.backends.mps
from ultralytics import YOLO

import logging


def get_model():
    """ Returns model from root dir
    :return: YOLO Model
    """
    if torch.backends.mps.is_available():
        logging.info("MPS is available. Taking X Model ...")
        return YOLO('yolov8x.pt')
    else:
        logging.info("MPS is not available. Taking S Model ...")
        return YOLO('yolov8s.pt')


def get_logger(log_level=logging.INFO):
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=log_level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    return logger
