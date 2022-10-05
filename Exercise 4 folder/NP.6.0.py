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

kernel = np.array([
            [1,1,1],
            [1,2,1],
            [1,1,1]],np.uint8)

testArray =     np.array([
[1,2,0,1,3],
[2,1,4,2,2],
[1,0,1,0,1],
[1,2,1,0,2],
[2,5,3,1,2],
])

blurTestArray = np.zeros((5,5))

arraySize = np.sqrt(np.prod(kernel.shape))
arraySize = int(arraySize)

kernelSize = np.sum(kernel)

Red = img[:, :, 2]
Green = img[:, :, 1]
Blue = img[:, :, 0]

RedNormalized   = np.zeros([img.shape[0],img.shape[1]],np.uint8)
GreenNormalized = np.zeros([img.shape[0],img.shape[1]],np.uint8)
BlueNormalized  = np.zeros([img.shape[0],img.shape[1]],np.uint8)



for x in range(1,4):
    for y in range (1,4):

        for i in range(0,arraySize):
            for j in range (0,arraySize):
                blurTestArray = 


print(kernelSize)
print(blurTestArray)
#print(RedNormalized)
#nomImg = cv.merge([BlueNormalized,GreenNormalized,RedNormalized])
##print(RedNormalized)
#
#cv.imshow("red",RedNormalized)
#cv.imshow("Image",img)
#cv.waitKey(0)