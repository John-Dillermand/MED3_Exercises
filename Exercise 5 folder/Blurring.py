from pickletools import uint8
from turtle import width
import cv2 as cv
import numpy as np

img = cv.imread('Circles.png',0)
height, width = img.shape[0], img.shape[1]




kernel = np.ones((11,11))


offset = len(kernel) //2

hitTest = np.zeros((3,3))
hitTest[0,0] = 1

blurredImage = np.zeros((height,width),np.uint8)

for x in range(offset,width-offset):
    for y in range(offset,height-offset):
        pixelValue=0
        for a in range (len(kernel)):
            for b in range(len(kernel)):
                xn = x + a - offset
                yn = y + b  - offset
                pixelValue += img[yn,xn] * kernel[a,b] 


        blurredImage[yn,xn]=pixelValue /9


cv.imshow("Image", blurredImage)
cv.waitKey(0)


#print(acc)
#
##Kan det her bruges?
##print(np.convolve(structuringElement,imgOnes))
#print(height)
#print(width)













#Fit 
#print(structuringElement==fitTest)
#print(np.all(structuringElement==fitTest))
#print(np.all(structuringElement==hitTest))



#Ide til hvordan jeg skal lave Dilation and erosion

#Jeg skal bare kunne trække en matrix af 3x3 størrelse ud af en bestemt center pixel.