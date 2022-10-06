from pickletools import uint8
from turtle import width
import cv2 as cv
import numpy as np

img = cv.imread('Circles.png',0)
height, width = img.shape[0], img.shape[1]

ret, thresh = cv.threshold(img,127,255,cv.THRESH_BINARY)
kernel = np.ones((5,5))
offset = len(kernel) //2

erodeImage = np.zeros((height,width),np.uint8)
dilationImage = np.zeros((height,width),np.uint8)

for x in range(offset,width-offset):
    for y in range(offset,height-offset):
        if thresh[y,x] == 0:
            for a in range (len(kernel)):
                for b in range(len(kernel)):
                    xn = x + a - offset
                    yn = y + b  - offset
                    erodeImage [yn,xn] = 255




for x in range(offset,width-offset):
    for y in range(offset,height-offset):
        if thresh[y,x] == 255:
            for a in range (len(kernel)):
                for b in range(len(kernel)):
                    xn = x + a - offset
                    yn = y + b  - offset
                    dilationImage [yn,xn] = 255


cv.imshow("ImageErode", erodeImage)
cv.imshow("ImageDilation", dilationImage)
cv.waitKey(0)