import cv2 as cv
import numpy as np
import math
from numpy import array
import math

FileName = "YellowBlank3.png"
crown    = 0
crown = str(crown)
enumerate
sand = 0
regions = ["sand", "water", "grass"]

img = cv.imread(FileName)


height = img.shape[0]
width = img.shape[1]

str1 = "Test1"
str2 = "Test2"
str3 = "Test3"


Red = img[:, :, 2]
Green = img[:, :, 1]
Blue = img[:, :, 0]
np.set_printoptions(suppress=True)

averageRed    = str(((np.sum(Red))  /(height*width)))
averageGreen  = str(((np.sum(Green))/(height*width)))
averageBlue   = str(((np.sum(Blue)) /(height*width)))

averageRGB = ["RED=",averageRed,"GREEN=",averageGreen,"BLUE=",averageBlue]

printToData = ["FileName=",FileName,",""RED=",averageRed,",","GREEN=",averageGreen,",","BLUE=",averageBlue,",",",crown=",crown]





#printToData = ["FileName=",FileName,",""RED=",averageRed,",","GREEN=",averageGreen,",","BLUE=",averageBlue,",","region=",",","Crown=",crown]
dataSheet = open("dataSheet", "r+")

dataSheet.writelines(printToData)





dataSheet.close()

print(averageRGB)




#cv.imshow("Image",img)
#cv.waitKey(0)

#print(bayerOutput)