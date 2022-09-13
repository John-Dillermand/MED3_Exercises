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


#The first [] controls the depth, so [0] would be the first depth or the Red value 
#The second [] controls the row
#The third [] controls the column 
#
## R = 0
## G = 1
## B = 2
#
#
i = 0
j = 0
for x in range (len(bayerInput)):
    bayerOutput[2][0+j][0+i] = bayerInput [0+j][0+i]
    bayerOutput[1][0+j][0+i] = bayerInput [0+j][1+i]
    bayerOutput[0][0+j][0+i] = bayerInput [1+j][1+i]
    i = i + 2
    if i == 4:
        i = 0
        j = j + 2
i1 = 0
j1 = 0

for x in range (len(bayerInput)):
    bayerOutput[2][0+j1][1+i1] = bayerInput [0+j1][0+i1]
    bayerOutput[1][0+j1][1+i1] = bayerInput [0+j1][1+i1]
    bayerOutput[0][0+j1][1+i1] = bayerInput [1+j1][1+i1]
    i1 = i1 + 2
    if i1 == 4:
        i1 = 0
        j1= j1 + 2

i2 = 0
j2 = 0

for x in range (4):
    bayerOutput[2][1+j2][0+i2] = bayerInput [0+j2][0+i2]
    bayerOutput[1][1+j2][0+i2] = bayerInput [1+j2][0+i2]
    bayerOutput[0][1+j2][0+i2] = bayerInput [1+j2][1+i2]
    i2 = i2 + 2
    if i2 == 4:
        i2 = 0
        j2= j2 + 2



# Red = 0
# Green = 1
# Blue = 2

#The first [] controls the row
#The second [] controls the column 


i3 = 0
j3 = 0

for x in range (4):
    bayerOutput[2][1+j3][1+i3] = bayerInput [0+j3][0+i3]
    bayerOutput[1][1+j3][1+i3] = bayerInput [0+j3][1+i3]
    bayerOutput[0][1+j3][1+i3] = bayerInput [1+j3][1+i3]
    i3 = i3 + 2
    if i3 == 4:
        i3 = 0
        j3= j3 + 2


print(bayerOutput)
#
#for x in range (len(bayer)):
#    print (bayer[x])

#[0][1]->1 
#[1][0]