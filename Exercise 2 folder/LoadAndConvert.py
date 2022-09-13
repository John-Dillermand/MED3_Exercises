import cv2 as cv
import numpy as np
import math
from numpy import array
import math


# R = 0
# G = 1
# B = 2
bayerInput = array ([[ 100, 10, 100, 11],
                     [ 9  , 50, 8  , 49 ],
                     [ 105, 12, 112, 9  ],
                     [ 14 , 52, 15 , 54 ]])

bayerOutput = np.zeros ((3,4,4))

HSIOutput = np.zeros ((3,4,4))

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

# 0 = hue
# 1 = saturation
# 2 = intensity 


hue = 0
saturation = 1
intensity = 2


Red = 0
Green = 1
Blue = 2


for i in range(0, 4):
    for j in range(0, 4):
        totalBayerOut = bayerOutput[0][i][j]+bayerOutput[1][i][j]+bayerOutput[Blue][i][j]
    #Calculations for Saturation
        HSIIndex = 0
        if HSIOutput[Red][i][j]>HSIOutput[saturation][i][j]:
            HSIIndex = 1
            if HSIOutput[saturation][i][j]>HSIOutput[intensity][i][j]:
                HSIIndex = 2


        HSIOutput[saturation][i][j]=1-(3*bayerOutput[HSIIndex][i][j])/totalBayerOut


        #Calculation for Intensity 
        HSIOutput[intensity][i][j] = (totalBayerOut)/3
    #----------------------------------------------------------------------------------------







#---------------------------------------------------
#   Calculations for Hues
for i in range(0, 4):
    for j in range(0, 4):
        HSIOutput[hue][i][j] = 0.5 * ((bayerOutput[Red][i][j] - bayerOutput[Green][i][j]) + (bayerOutput[Red][i][j] - bayerOutput[Blue][i][j])) / \
                    math.sqrt((bayerOutput[Red][i][j] - bayerOutput[Green][i][j])**2 +
                            ((bayerOutput[Red][i][j] - bayerOutput[Blue][i][j]) * (bayerOutput[Green][i][j] - bayerOutput[Blue][i][j])))
        HSIOutput[hue][i][j] = math.acos(HSIOutput[hue][i][j])

        if bayerOutput[Blue][i][j] <= bayerOutput[Green][i][j]:
            HSIOutput[hue][i][j] = HSIOutput[hue][i][j]
        else:
            HSIOutput[hue][i][j] = ((360 * math.pi) / 180.0) - HSIOutput[hue][i][j]

print(HSIOutput)




       

#print(bayerOutput)