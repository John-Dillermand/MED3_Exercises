import cv2 as cv
import numpy as np
import math
from numpy import array
import math

img = cv.imread("753.jpg",1)


height = img.shape[0]
width = img.shape[1]

Red = img[:, :, 2]
Green = img[:, :, 1]
Blue = img[:, :, 0]
np.set_printoptions(suppress=True)

cv.inRange

HSIOutput = np.zeros ((height,width,3),np.uint8)


hue = 0
saturation = 1
intensity = 2




for i in range(0, height):
    for j in range(0, width):
        r = int (img[i,j,2])
        g = int (img[i,j, 1])
        b = int (img[i,j, 0])
        #Calculations for Saturation
        MinNum = min(r,g,b)
        s = 1 - 3*(MinNum/(r + g + b))

        #Calculation for Intensity 
        i = (r + g + b)/3

        #Calculation for hue
        h = np.arccos(0.5 * ((r-g)+(r-b))/np.sqrt((r-g)*(r-g)+(r-b)*(g-b)+0.001))

        if g >= b:
            h  = h
        else:
            h  = ((360*np.pi)/180) - h

        HSIOutput[i][j][0] = (h * 180)/np.pi
        HSIOutput[i,j][1] = s
        HSIOutput[i,j][2] = i


cv.imshow("Image",HSIOutput)
cv.waitKey(0)

#print(bayerOutput)