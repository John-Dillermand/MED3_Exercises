import cv2 as cv
import numpy as np
import math
from numpy import array
import math

FileName = "YellowBlank3.png"


img = cv.imread(FileName)


height = img.shape[0]
width = img.shape[1]




Red = img[:, :, 2]
Green = img[:, :, 1]
Blue = img[:, :, 0]
np.set_printoptions(suppress=True)

print((np.sum(Red))/(height*width))
print((np.sum(Green))/(height*width))
print((np.sum(Blue))/(height*width))


FileObject = open(r"Datasheet","r+")

FileObject.write("Penis")

FileObject.close()

#cv.imshow("Image",img)
#cv.waitKey(0)

#print(bayerOutput)