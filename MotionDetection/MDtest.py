
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
  
# define a video capture object
vid = cv.VideoCapture(0)

frameCount = 0
previousFrame = None

while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()


    grayFrame =cv.cvtColor (frame,cv.COLOR_BGR2GRAY)
    blurredFrame= cv.GaussianBlur(grayFrame,(5,5),0)
    preparedFrame = blurredFrame
    if (previousFrame is None):
      previousFrame = preparedFrame

    diffFrame = cv.absdiff(src1=previousFrame,src2=preparedFrame)
    previousFrame = preparedFrame

    #Dilute the image to make differences more seeable
    kernel = np.ones((5,5))
    diffFrame = cv.dilate(diffFrame,kernel,1)
    threshFrame= cv.threshold(src=diffFrame, thresh=20, maxval=255,type=cv.THRESH_BINARY)[1]



      # Display the resulting frame
    cv.imshow('frame', threshFrame)
      
    if cv.waitKey(1) & 0xFF == ord('0'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv.destroyAllWindows()