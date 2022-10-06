from turtle import width
import cv2 as cv
import numpy as np

img = cv.imread('Rb.jpg')
height, width = img.shape[0], img.shape[1]

print(np.ndim(img))

Red = img[:, :, 2]
Green = img[:, :, 1]
Blue = img[:, :, 0]

redArray  = np.zeros((height,width),np.uint8)
greenArray= np.zeros((height,width),np.uint8)
blueArray = np.zeros((height,width),np.uint8)

kernel = np.ones((5,5))

kernelSum = np.sum(kernel)

offset = len(kernel) //2

blurredImage = np.zeros((height,width),np.uint8)



if np.ndim(img) == 1:
    for x in range(offset,width-offset):
        for y in range(offset,height-offset):
            pixelValue = 0
            for a in range (len(kernel)):
                for b in range(len(kernel)):
                    xn = x + a - offset
                    yn = y + b  - offset
                    pixelValue += img[yn,xn] * kernel[a,b] 
            blurredImage[yn,xn]=pixelValue / kernelSum


if np.ndim(img) == 3:
    for x in range(offset,width-offset):
        for y in range(offset,height-offset):
            pixelValueRed = 0
            pixelValueBlue = 0
            pixelValueGreen= 0
            for a in range (len(kernel)):
                for b in range(len(kernel)):
                    xn = x + a - offset
                    yn = y + b  - offset
                    pixelValueRed += img[yn,xn,0] * kernel[a,b] 
                    pixelValueBlue += img[yn,xn,1] * kernel[a,b] 
                    pixelValueGreen += img[yn,xn,2] * kernel[a,b] 
            redArray[yn,xn] = pixelValueRed / kernelSum
            blueArray[yn,xn] = pixelValueBlue/ kernelSum
            greenArray[yn,xn] = pixelValueGreen/ kernelSum




if np.ndim(img) == 0:

    cv.imshow("Image",blurredImage)
    cv.waitKey(0)




if np.ndim(img) == 3:
    merged = cv.merge([redArray,blueArray,greenArray])
    cv.imshow("Image",merged)
    cv.waitKey(0)
