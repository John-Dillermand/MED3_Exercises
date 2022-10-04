import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


vid = cv.VideoCapture(0)





frameCount = 0
previousFrame = None
while True:
    frameCount += 1
    imgBRG = np.array(vid.grab())
    imgRGB = cv.cvtColor(src=imgBRG, code=cv.COLOR_BGR2RGB)
    if ((frameCount%2)==0):
        #2. Preparing the image
        preparedFrame = cv.cvtColor(imgRGB,cv.COLOR_BGR2GRAY)
        preparedFrame = cv.GaussianBlur(src=preparedFrame, ksize=(5,5),sigmax=0)
    if (previousFrame is None):
        #First frame; there is no previous yet
        previousFrame = preparedFrame
    diffFrame = cv.absdiff(src1=previousFrame,src2=preparedFrame)
    previousFrame = preparedFrame
    #Dilute the image, to make differences more seeable
    kernel = np.ones((5,5))
    diffFrame = cv.dilate(diffFrame,kernel,1)
    threshFrame = cv.threshold(src=diffFrame, thresh=20, maxval=255, type=cv.THRESH_BINARY)[1]
    contours, _ = cv.findContours(image=threshFrame,mode=cv.RETR_EXTERNAL,method=cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(image=imgRGB, contours=contours, contourIdx=-1, color=(0,255,0),thickness=2,lineType=cv.LINE_AA)
    countours,_=cv.findContours(image=threshFrame, mode=cv.RETR_EXTERNAL,metod=cv.CHAIN_APPROX_SIMPLE)
    for contour in countours:
        if cv.countourArea(contour) <50:
            continue
        (x,y,w,h) = cv.boundingRect(contour)
        cv.rectangle(img=imgRGB,pt1=(x,y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=2)
        cv.imshow('Motion detector', imgRGB)
        if (cv.waitKey(30) == 27):
            break
