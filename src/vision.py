import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

from tqdm import tqdm


class Vision:

    def __init__(self, model, path_to_video: str, confidence_threshold: float, logger):
        self.model = model
        self.path_to_video = path_to_video
        self.confidence_threshold = confidence_threshold
        self.logger = logger

        self.centers = None
        self.image = None
        self.frame_count = None
        self.heatmap = None

    def get_frames(self, take_every_k_frame: int = 24) -> tuple[list, np.array, int]:
        """ Applies the YOLO model on every k-th frame and returns, among others, the BB centers

        :param take_every_k_frame: int -- Every k frame to take
        :return:
            centers: list -- List of centers (Shoe position BB)
            image: np.array -- First frame of the input video
            frame_count: int -- Number of frames collected
        """
        centers: list = []  # Bounding Boxes Centers (Shoe centric)
        image = None
        counter: int = 0  # Help variable to get every k frame
        frame_count: int = 0  # Counter variable to check how many frames were taken
        start_time = time.time()

        # Capture Video
        cap = cv2.VideoCapture(self.path_to_video)
        while cap.isOpened():
            ret, frame = cap.read()
            # If no frame is available, break while loop
            if not ret:
                break
            if image is None:
                image = frame

            # Take every k-th frame
            counter += 1
            if counter % take_every_k_frame != 0:
                continue

            # Transform BGR image to RGB image and predict on given frame
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.model.predict(frame, classes=[0], conf=self.confidence_threshold, verbose=False)
            for r in results:
                boxes = r.boxes
                for box in boxes:
                    b = box.xyxy[0]  # Get box coordinates in (top, left, bottom, right) format
                    x0, y0, x1, y1 = b
                    x, y, w, h = x0, y0, x1 - x0, y1 - y0      # Get origin of BB and width and height
                    center: tuple = (int(x + w / 2), int(y1))  # Get shoe position (center)
                    centers.append(center)

            # Track how many frames were taken
            frame_count += 1

        cap.release()
        cv2.destroyAllWindows()
        end_time = time.time()

        self.set_frames_attributes(centers, image, frame_count)
        self.logger.info(f"Collected {frame_count} frames in {(end_time - start_time):.2f} seconds ...")
        return centers, image, frame_count

    def set_frames_attributes(self, centers, image, frame_count) -> None:
        """ Sets collected data as instance attributes

        :param centers: list -- Collected centers
        :param image: np.array -- First frame / image of the given video
        :param frame_count: int -- Number of frames collected
        :return: None
        """
        self.centers = centers
        self.image = image
        self.frame_count = frame_count
        # Log information
        self.logger.debug("Set attributes ...")

    def get_heatmap(self) -> np.array:
        """ Adds multiple collected frames together by adding ellipse at the center positions and post-processes it
        :return: heatmap: np.array -- Postprocessed Heatmap
        """
        densities = np.zeros((self.image.shape[0], self.image.shape[1]), dtype=np.float32)
        for center in tqdm(self.centers):
            size = (30, 30)
            angle = 0
            startAngle = 0
            endAngle = 360
            density = np.zeros((self.image.shape[0], self.image.shape[1]), dtype=np.float32)
            cv2.ellipse(density, center, size, angle, startAngle, endAngle, (1, 1), -1)
            densities = densities + density

        # Postprocess densities / heatmap
        heatmap = self.postprocess_heatmap(densities)
        self.heatmap = heatmap

        return heatmap

    def postprocess_heatmap(self, densities: np.array) -> np.array:
        """ Performs multiple post-processing on the given densities / heatmap

        :param densities: np.array -- Input densities / heatmap
        :return: heatmap: np.array -- Processed heatmap
        """
        # Postprocess densities / heatmap
        densities = cv2.GaussianBlur(densities, (21, 21), 0)
        densities = cv2.normalize(densities, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
        heatmap = cv2.applyColorMap(densities, cv2.COLORMAP_TURBO)
        heatmap = cv2.cvtColor(heatmap, cv2.COLOR_BGR2RGB)
        heatmap = cv2.addWeighted(self.image, 0.5, heatmap, 1, 0)

        return heatmap

    def plot_densities(self) -> None:
        """ Plots the densities / heatmap as a two axis plot
        First axis shows the heatmap overlayed on the first input image;
        Second axis show the heatmap only.

        :return: None
        """
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 10))
        axes[0].imshow(self.image)
        axes[0].set_title(f"Heatmap Overlay (N_Frames = {self.frame_count})", size=16, fontweight="bold")
        axes[1].imshow(self.heatmap)
        axes[1].set_title(f"Heatmap (N_Frames = {self.frame_count})", size=16, fontweight="bold")
        fig.tight_layout()
        # plt.savefig("../assets/heatmap.png", dpi=126, bbox_inches='tight')
        plt.show()
