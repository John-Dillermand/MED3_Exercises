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

RedNormalized   = np.zeros([img.shape[0]-1,img.shape[1]-1],np.uint8)
GreenNormalized = np.zeros([img.shape[0]-1,img.shape[1]-1],np.uint8)
BlueNormalized  = np.zeros([img.shape[0]-1,img.shape[1]-1],np.uint8)

kernelSize = np.sum(kernel)

kernelWidth = math.floor(kernelSize/2)

outputSignal = np.zeros(img.shape[0]-2*kernelWidth)


for i in range(img.shape[0]):
    outputSignal[i] = sum(Red[i:i+kernelSize]*kernel)/sum(kernel)






nomImg = cv.merge([BlueNormalized,GreenNormalized,RedNormalized])
print(RedNormalized)

cv.imshow("Output",outputSignal)
cv.imshow("red",RedNormalized)

cv.imshow("Image",nomImg)
cv.waitKey(0)