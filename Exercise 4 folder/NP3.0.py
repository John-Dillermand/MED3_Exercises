from locale import normalize
import cv2 as cv
import numpy as np
import math
from numpy import array
import math

img = cv.imread("lion.jpg")
np.set_printoptions(suppress=True)

height = img.shape[0]
width = img.shape[1]

imageSize = (4,4)
kernel = np.array([
            [1,1,1],
            [1,1,1],
            [1,1,1]],np.uint8)

Red = img[:, :, 2]
Green = img[:, :, 1]
Blue = img[:, :, 0]

RedNormalized   = np.zeros([img.shape[0],img.shape[1]],np.uint8)
GreenNormalized = np.zeros([img.shape[0],img.shape[1]],np.uint8)
BlueNormalized  = np.zeros([img.shape[0],img.shape[1]],np.uint8)

kernelSize = np.sum(kernel)

for i in range(1,img.shape[0]-1):
    for j in range (1,img.shape[1]-1):
        RedTopRow = kernel[1-1,1-1]*Red[i-1,j-1]  /kernelSize  + kernel[1-1,1]*Red[i-1,j]/ kernelSize  + kernel[1-1,1+1]*Red[i-1,j+1]/kernelSize
        RedMidRow = kernel[1,1-1]  *Red[i,j-1]    /kernelSize + kernel[1,1]*  Red[i,j]  /  kernelSize + kernel[1,1+1]  *Red[i,j+1]/kernelSize
        RedBotRow = kernel[1+1,1-1]*Red[i+1,j-1]  /kernelSize + kernel[1+1,1]*Red[i+1,j]/  kernelSize + kernel[1+1,1+1]*Red[i+1,j+1]/kernelSize
        RedNormalized[i-1,j-1] = RedTopRow + RedMidRow + RedBotRow

        GreenTopRow = kernel[1-1,1-1]*Green[i-1,j-1]/kernelSize + kernel[1,1-1]*Green[i-1,j-1]/kernelSize + kernel[1-1,1+1]*Green[i-1,j+1]/kernelSize
        GreenMidRow = kernel[1,1-1]*Green[i,j-1]    /kernelSize + kernel[1,1]  *Green[i,j]  /kernelSize + kernel[1,1+1]*  Green[i,j+1]/kernelSize
        GreenBotRow = kernel[1+1,1-1]*Green[i+1,j-1]/kernelSize + kernel[1+1,1]*Green[i+1,j]/kernelSize + kernel[1+1,1+1]*Green[i+1,j+1]/kernelSize
        GreenNormalized[i-1,j-1] = GreenTopRow + GreenMidRow + GreenBotRow

        BlueTopRow = kernel[1-1,1-1]*Blue[i-1,j-1]/kernelSize + kernel[1,1-1]*Blue[i-1,j]/kernelSize + kernel[1-1,1+1]*Blue[i-1,j+1]/kernelSize
        BlueMidRow = kernel[1,1-1]*Blue[i,j-1]    /kernelSize + kernel[1,1]*Blue[i,j]    /kernelSize + kernel[1,1+1]  *Blue[i,j+1]  /kernelSize
        BlueBotRow = kernel[1+1,1-1]*Blue[i+1,j-1]/kernelSize + kernel[1+1,1]*Blue[i+1,j]/kernelSize + kernel[1+1,1+1]*Blue[i+1,j+1]/kernelSize
        BlueNormalized[i-1,j-1] = BlueTopRow + BlueMidRow + BlueBotRow





nomImg = cv.merge([BlueNormalized,GreenNormalized,RedNormalized])
#print(RedNormalized)

cv.imshow("red",RedNormalized)

cv.imshow("ImageBlurred",nomImg)
#cv.imshow("Image",img)
cv.waitKey(0)