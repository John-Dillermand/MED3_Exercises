import cv2 as cv
import numpy as np

imgBGR = cv.imread('dots.gif')
imgRGB = cv.cvtColor(imgBGR,cv.COLOR_BGR2RGB)


templateGray = cv.cvtColor(imgBGR, cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(imgBGR,(5,5),0)



cv.imshow(blur)
cv.waitKey(0)
