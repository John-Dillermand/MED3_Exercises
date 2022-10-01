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

image = np.array([[100,200,0,110],
                 [200,200,40,200],
                 [150,0,10,50],
                 [100,200,0,42]],np.uint8)

Red = img[:, :, 2]
Green = img[:, :, 1]
Blue = img[:, :, 0]

RedNormalized = np.zeros([img.shape[0]-1,img.shape[1]-1],np.uint8)
GreenNormalized = np.zeros([img.shape[0]-1,img.shape[1]-1],np.uint8)
BlueNormalized = np.zeros([img.shape[0]-1,img.shape[1]-1],np.uint8)

kernelSize = np.sum(kernel)

for i in range(1,img.shape[0]-1):
    for j in range (1,img.shape[0]-1):
        temp = 0
        topRow = kernel[1-1,1-1]*Red[i-1,j-1]/kernelSize + kernel[1,1-1]*Red[i,j-1]/ + kernel[1-1,1+1]*Red[i-1,j+1]/kernelSize
        midRow = kernel[1,1-1]*Red[i,j-1]    /kernelSize + kernel[1,1]*Red[i,j]    / + kernel[1,1+1]*Red[i,j+1]/kernelSize
        botRow = kernel[1+1,1-1]*Red[i+1,j-1]/kernelSize + kernel[1+1,1]*Red[i+1,j]/ + kernel[1+1,1+1]*Red[i+1,j+1]/kernelSize
        if topRow + midRow + botRow < 0:
            RedNormalized[i-1,j-1] = 0
        RedNormalized[i-1,j-1] = topRow + midRow + botRow



for i in range(1,img.shape[0]-1):
    for j in range (1,img.shape[0]-1):
        temp = 0
        topRow = kernel[1-1,1-1]*Blue[i-1,j-1]/kernelSize + kernel[1,1-1]*Blue[i,j-1]/ + kernel[1-1,1+1]*Blue[i-1,j+1]/kernelSize
        midRow = kernel[1,1-1]*Blue[i,j-1]    /kernelSize + kernel[1,1]*Blue[i,j]    / + kernel[1,1+1]*Blue[i,j+1]/kernelSize
        botRow = kernel[1+1,1-1]*Blue[i+1,j-1]/kernelSize + kernel[1+1,1]*Blue[i+1,j]/ + kernel[1+1,1+1]*Blue[i+1,j+1]/kernelSize
        if topRow + midRow + botRow < 0:
            BlueNormalized[i-1,j-1] = 0
        BlueNormalized[i-1,j-1] = topRow + midRow + botRow


for i in range(1,img.shape[0]-1):
    for j in range (1,img.shape[0]-1):
        temp = 0
        topRow = kernel[1-1,1-1]*Green[i-1,j-1]/kernelSize + kernel[1,1-1]*Green[i,j-1]/ + kernel[1-1,1+1]*Green[i-1,j+1]/kernelSize
        midRow = kernel[1,1-1]*Green[i,j-1]    /kernelSize + kernel[1,1]*Green[i,j]    / + kernel[1,1+1]*Green[i,j+1]/kernelSize
        botRow = kernel[1+1,1-1]*Green[i+1,j-1]/kernelSize + kernel[1+1,1]*Green[i+1,j]/ + kernel[1+1,1+1]*Green[i+1,j+1]/kernelSize
        if topRow + midRow + botRow < 0:
            GreenNormalized[i-1,j-1] = 0
        GreenNormalized[i-1,j-1] = topRow + midRow + botRow

nomImg = cv.merge([BlueNormalized,GreenNormalized,RedNormalized])
print(RedNormalized)

cv.imshow("red",RedNormalized)

cv.imshow("Image",nomImg)
cv.waitKey(0)