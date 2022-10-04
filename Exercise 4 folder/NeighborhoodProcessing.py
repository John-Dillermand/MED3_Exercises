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
            [1,2,1],
            [1,1,1]],np.uint8)

#image = np.array([[100,200,0,110],
#                 [200,200,40,200],
#                 [150,0,10,50],
#                 [100,200,0,42]],np.uint8)


image = np.array([[1,2,0,1,3],
                  [2,1,4,2,2],
                  [1,0,1,0,1],
                  [1,2,1,0,2],
                  [2,5,3,1,2]],np.uint8)

imageNormalized = np.zeros([3,3],np.uint8)

kernelSize = np.sum(kernel)

for i in range(1,4):
    for j in range (1,4):
        temp = 0
        topRow = kernel[1-1,1-1]*image[i-1,j-1]/kernelSize + kernel[1,1-1]*image[i,j-1]/ + kernel[1-1,1+1]*image[i-1,j+1]/kernelSize
        midRow = kernel[1,1-1]  *image[i,j-1]    /kernelSize + kernel[1,1]  *image[i,j]  / + kernel[1,1+1]  *image[i,j+1]  /kernelSize
        botRow = kernel[1+1,1-1]*image[i+1,j-1]/kernelSize + kernel[1+1,1]*image[i+1,j]/ + kernel[1+1,1+1]*image[i+1,j+1]/kernelSize
        imageNormalized[i-1,j-1] = topRow + midRow + botRow

 
print(imageNormalized)