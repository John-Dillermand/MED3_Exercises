import cv2 
import numpy as np  
def nothing(x):     pass  # Create a black image, a window img = np.zeros((300,512,3), np.uint8) cv2.namedWindow('image')


#Create a black image, a window
img = cv2.imread('1.jpg',0)
cv2.namedWindow('image')


# create trackbars for color change
cv2.createTrackbar('LowThresh','image',0,126,nothing)
cv2.createTrackbar('HighThresh','image',127,255,nothing)

# create switch for ON/OFF functionality


while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('LowThresh','image')
    g = cv2.getTrackbarPos('HighThresh','image')

    
img[:] = [r,g]
cv2.destroyAllWindows()