from pickletools import uint8
import cv2 as cv
import numpy as np
import math

img = cv.imread("2dark.png")
height, width = img.shape[0], img.shape[1]



Red   =  img[:, :, 2]
Green =  img[:, :, 1]
Blue  =  img[:, :, 0]


hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
img2 = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)

standardValue = 118
hue          = hsv[:, :, 0]
saturation   = hsv[:, :, 1]
values       = hsv[:, :, 2]



currentValue = (np.sum(values)/(height*width))

 
scalar = math.ceil(118/currentValue)
newValue = img + (2,2,2)
print(scalar)




brightnessCorrugated = cv.merge([hue,saturation,newValue])
brightnessCorrugated = cv.cvtColor(brightnessCorrugated, cv.COLOR_HSV2BGR)

cv.imshow("Original", img)
cv.imshow("The new Values", newValue)
cv.imshow("Brightend",brightnessCorrugated)
cv.waitKey(0)

