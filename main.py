import src.utils as utils

from src.vision import Vision


def main():
    # Parse args
    args = utils.parse_args()

    # Get logger
    logger = utils.get_logger()

    # Create Vision object with YOLO model located in root
    vision = Vision(model=utils.get_model(),
                    path_to_video="data/raw/test_video.mov",
                    confidence_threshold=args["conf"],
                    logger=logger)

    # Get frames to process and create heatmap
    centers, image, frame_count = vision.get_frames(take_every_k_frame=args["k"])
    heatmap_overlayed, heatmap = vision.get_heatmap()

    # Plot and/or save results
    vision.plot_densities(savefig=True, showfig=False)


if __name__ == "__main__":
    main()