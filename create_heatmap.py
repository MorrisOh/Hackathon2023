import cv2
import numpy as np

def crt_htmp(img, all_bounding_boxes):

    density = np.zeros((img.shape[0], img.shape[1]), dtype=np.float32)
    for x0, y0, x1, y1 in all_bounding_boxes:
        x, y, w, h = x0, y0, x1-x0, y1-y0
        center = (int(x + w/2), int(y + h/2))
        size = (int(w/2 * 0.04), int(h/2 * 0.04))
        angle = 0
        startAngle = 0
        endAngle = 360
        cv2.ellipse(density, center, size, angle, startAngle, endAngle, (1, 1), -1)

    density = cv2.GaussianBlur(density, (21, 21), 0)
    density = cv2.normalize(density, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    heatmap = cv2.applyColorMap(density, cv2.COLORMAP_TURBO)
    img = cv2.addWeighted(img, 0.5, heatmap, 0.5, 0)

    cv2.imshow('img',img)
    
if __name__ == '__main__':
    print('bla')