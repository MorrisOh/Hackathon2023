import cv2 as cv
import numpy as np 
import torch
from ultralytics import YOLO
from create_heatmap import crt_htmp

model = YOLO("yolov8x-seg.pt")
if torch.backends.mps.is_available():
    model.to("mps")
vid = cv.VideoCapture(1)

while(True):
    
    ret, frame = vid.read() 
    frame  = cv.resize(frame, (640,480))
    
    results = model(frame, conf=0.1, classes=[0], retina_masks=True)
    boxes = results[0].boxes.xyxy
    
    for box in boxes:
        allBB.append(box.numpy())
        
    # Display the resulting frame 
    #cv.imshow('frame', frame) 
    
    crt_htmp(frame, allBB)
    
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv.destroyAllWindows() 
