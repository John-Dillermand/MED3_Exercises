from pickletools import uint8
from turtle import width
import cv2 as cv
import numpy as np

img = cv.imread('Circles.png')
width, height = img.shape[0], img.shape[1]


structuringElement = np.ones((3,3))



kernel = np.ones((3,3))


offset = len(structuringElement) //2

hitTest = np.zeros((3,3))
hitTest[0,0] = 1

blurredImage = np.zeros((width,height),np.uint8)



for x in range(offset,width-offset):
    for y in range(offset,height-offset):
        acc = [0,0,0]
        for a in range (len(kernel)):
            for b in range(len(kernel)):
                xn = x + a - offset
                yn = y + b  - offset
                pixel = img[xn, yn]
                acc[0] += pixel[0] * kernel[a,b]
                acc[1] += pixel[1] * kernel[a,b]
                acc[2] += pixel[2] * kernel[a,b]





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
print(offset)

#cv.imshow("Image",img)
cv.waitKey(0)
#Ide til hvordan jeg skal lave Dilation and erosion

#Jeg skal bare kunne trække en matrix af 3x3 størrelse ud af en bestemt center pixel.