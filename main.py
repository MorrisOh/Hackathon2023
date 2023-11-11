import numpy as np

import src.utils as utils

from src.vision import Vision


def main():
    logger = utils.get_logger()

    vision = Vision(model=utils.get_model('yolov8s.pt'),
                    path_to_video="data/raw/test_video.mov",
                    confidence_threshold=0.3,
                    logger=logger)

    centers, image, frame_count = vision.get_frames(take_every_k_frame=100)
    heatmap: np.array = vision.get_heatmap()
    vision.plot_densities()


if __name__ == "__main__":
    main()
