import cv2 as cv
import numpy as np
import math
from numpy import array
import math

img = cv.imread("Rb.jpg")


height = img.shape[0]
width = img.shape[1]




Red = img[:, :, 2]
Green = img[:, :, 1]
Blue = img[:, :, 0]
np.set_printoptions(suppress=True)

cv.inRange

HSIOutput = np.zeros ((height,width,3),np.uint8)


# 0 = hue
# 1 = saturation
# 2 = intensity 
hue = 0
saturation = 1
intensity = 2


# R = 0
# G = 1
# B = 2


for i in range(0, height):
    for j in range(0, width):
        totalBayerOut = Red[i][j]/3+Green[i][j]/3+Blue[i][j]/3
    #Calculations for Saturation
        MinNum = (min(Red[i][j],Green[i][j],Blue[i][j]))
        
         
        HSIOutput[i][j] = 1 - (3 / (totalBayerOut + 0.001) * MinNum)


        #Calculation for Intensity 
        HSIOutput[i][j][intensity] = (totalBayerOut)/3
    #---------------------------------------------------------------------------------------


#print(totalBayerOut/3)
#---------------------------------------------------
#   Calculations for Hues
for i in range(0, height):
    for j in range(0, width):
        HSIOutput[i][j][hue] = 0.5 * ((Red[i][j] - Green[i][j]) + (Red[i][j] - Blue[i][j])) / \
                    math.sqrt((Red[i][j] - Green[i][j])**2 +
                            ((Red[i][j] - Blue[i][j]) * (Green[i][j] - Blue[i][j])))
        HSIOutput[i][j][hue] = math.acos(HSIOutput[i][j][hue])

        if Blue[i][j] <= Green[i][j]:
            HSIOutput[i][j][hue] = HSIOutput[i][j][hue]
        else:
            HSIOutput[i][j][hue] = ((360 * math.pi) / 180.0) - HSIOutput[i][j][hue]

img = HSIOutput
cv.imshow("Image",img)
cv.waitKey(0)

#print(bayerOutput)