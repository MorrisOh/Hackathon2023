import src.utils as utils

from src.vision import Vision


def main(payload: dict = None) -> None:
    """ Pipeline of the heatmap generation function.
    Takes parameter either from argparse via Command Line Interface (CLI), or if it is
    called from a different function, from the payload: dict parameter.

    :param payload: dict -- Input Parameter
    :return: None
    """
    # Either get CLI arguments, or params defined in payload dict
    args = get_args(payload)

    # Get logger
    logger = utils.get_logger()

    # Create Vision object with YOLO model located in root
    vision = Vision(model=utils.get_model(),
                    path_to_video=args["path"],
                    confidence_threshold=args["conf"],
                    logger=logger)

    # Get frames to process and create heatmap
    centers, image, frame_count = vision.get_frames(take_every_k_frame=args["k"])
    heatmap_overlayed, heatmap = vision.get_heatmap()

    # Plot and/or save results
    vision.plot_densities(savefig=True, showfig=False)


def get_args(payload) -> dict:
    """ Returns the parameters either from CLI or from payload input param

    :param payload: dict -- Input parameter, if main is called from function instead of CLI
    :return: args: dict -- Parsed arguments / parameters
    """
    # Differentiate between CLI arguments and payload (if main is called from a function)
    if payload is None:
        # Parse args from CL
        args = utils.parse_args()
    else:
        args = payload
        # Assert that input parameter are defined in payload dict
        assert all(k in args for k in ['path', 'k', 'conf']), "Error: Entries for 'path', 'conf' and 'k' are missing!"

    return args


if __name__ == "__main__":
    main()

    # If called from function (and not CL) provide params as dict in payload param, e.g.
    #main(payload={"path": "data/raw/test_video.mov", "conf": 0.3, "k": 200})