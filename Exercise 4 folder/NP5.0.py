from locale import normalize
import cv2 as cv
import numpy as np
import math
from numpy import array
import math

#img = cv.imread("lion.jpg")
#np.set_printoptions(suppress=True)

#height = img.shape[0]
#width = img.shape[1]

imageSize = (4,4)
kernel = np.array([
            [1,2,3],
            [4,5,6],
            [7,8,9]])

image = np.array([[100,200,0,110],
                 [200,200,40,200],
                 [150,0,10,50],
                 [100,200,0,42]],np.uint8)


print(kernel[1-1,1-1])
print(kernel[1-1,1])
print(kernel[1-1,1+1])

print(kernel[1,1-1])
print(kernel[1,1])
print(kernel[1,1+1]  )



print(kernel[1+1,1-1])
print(kernel[1+1,1])
print(kernel[1+1,1+1])
