import cv2 as cv
import numpy as np 
from ultralytics import YOLO

model = YOLO("yolov8s-seg.pt")
vid = cv.VideoCapture(1)

while(True):
    
    ret, frame = vid.read() 
    frame  = cv.resize(frame, [640,480])
    
    results = model(frame, conf=0.1, classes=[0], retina_masks=True)
    masks = results[0].masks
    
    #for mask in masks:
        
    
    # Display the resulting frame 
    cv.imshow('frame', results[0].plot()) 
      
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv.destroyAllWindows() 