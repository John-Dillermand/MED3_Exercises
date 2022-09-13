import cv2 as cv
import numpy as np
from numpy import array

# R = 0
# G = 1
# B = 2
bayerInput = array ([[ 100, 10, 100, 11],
                     [ 9  , 50, 8  , 49 ],
                     [ 105, 12, 112, 9  ],
                     [ 14 , 52, 15 , 54 ]])

bayerOutput = np.zeros ((3,4,4))

i = 0
j = 0
for x in range (len(bayerInput)):
    bayerOutput[2][0+j][0+i] = bayerInput [0+j][0+i]
    bayerOutput[1][0+j][0+i] = bayerInput [0+j][1+i]
    bayerOutput[0][0+j][0+i] = bayerInput [1+j][1+i]

    bayerOutput[2][0+j][1+i] = bayerInput [0+j][0+i]
    bayerOutput[1][0+j][1+i] = bayerInput [0+j][1+i]
    bayerOutput[0][0+j][1+i] = bayerInput [1+j][1+i]

    bayerOutput[2][1+j][0+i] = bayerInput [0+j][0+i]
    bayerOutput[1][1+j][0+i] = bayerInput [1+j][0+i]
    bayerOutput[0][1+j][0+i] = bayerInput [1+j][1+i]

    bayerOutput[2][1+j][1+i] = bayerInput [0+j][0+i]
    bayerOutput[1][1+j][1+i] = bayerInput [0+j][1+i]
    bayerOutput[0][1+j][1+i] = bayerInput [1+j][1+i]

    i = i + 2
    if i == 4:
        i = 0
        j = j + 2

print(bayerOutput)