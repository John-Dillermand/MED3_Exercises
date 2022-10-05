import cv2 as cv
import numpy as np

imgBGR = cv.imread('BP.png')
imgRGB = cv.cvtColor(imgBGR,cv.COLOR_BGR2RGB)


imgGray = cv.cvtColor(imgBGR, cv.COLOR_BGR2GRAY)

ret,threshold = cv.threshold(imgGray,85,255,cv.THRESH_BINARY_INV)


blur = cv.GaussianBlur(imgBGR,(5,5),0)
kernel = np.ones((5,5),np.uint8)
ersion = cv.erode(threshold,kernel,iterations=3)
dilation = cv.dilate(threshold,kernel,iterations = 3)

opening = cv.dilate(ersion,kernel,iterations=1)

closing = cv.erode(dilation,kernel,iterations=1)


cv.imshow("imageErsion",ersion)
cv.imshow("imageDilation",dilation)
cv.imshow("imageThreshold",threshold)
cv.imshow("imageOpening",opening)
cv.imshow("imageClosing",closing)


cv.waitKey(0)
