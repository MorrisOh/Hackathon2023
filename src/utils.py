import argparse

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
    """ Configures the logger and returns a logger object

    :param log_level: constant -- Level of Log
    :return: logger object
    """
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=log_level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    return logger


def parse_args() -> dict:
    """ Sets the CLI arguments and parses it

    :return: vars(args): dict -- Parsed args as dict
    """
    # Parse arguments
    parser = argparse.ArgumentParser()
    # Argument 1: Input video path
    parser.add_argument("--path",
                        default="data/raw/test_video.mov",
                        type=str,
                        help="str -- Path to the test video (relative to root dir)")
    # Argument 2: Every k frame to consider
    parser.add_argument("--k",
                        default=20,
                        type=int,
                        help="int -- Every k-th you want to consider during inference")
    # Argument 3: Confidence Threshold
    parser.add_argument("--conf",
                        default=0.3,
                        type=float,
                        help="float -- Confidence threshold to consider for classification")
    # places the extracted data in an argparse.Namespace object:
    args = parser.parse_args()
    return vars(args)
