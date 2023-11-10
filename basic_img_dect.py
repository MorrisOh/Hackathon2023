import cv2 as cv
import numpy as np 
from ultralytics import YOLO

model = YOLO("yolov8s-seg.pt")
vid = cv.VideoCapture(0)

while(True):
    
    ret, frame = vid.read() 
    frame  = cv.resize(frame, (640,480))
    
    results = model(frame, conf=0.1, classes=[0], retina_masks=True)
    try:
        masks = results[0].masks.data
        blurFrame = cv.GaussianBlur(frame,[101,101],0)
        
        for mask in masks:
            bitMask = mask.numpy()
            bitMask = np.around(bitMask)
            
            
            frame[bitMask == 1] = blurFrame[bitMask == 1]
      
    except Exception as e:
          print(e)
        
    # Display the resulting frame 
    cv.imshow('frame', frame) 
      
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv.destroyAllWindows() 