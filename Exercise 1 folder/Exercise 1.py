import cv2 as cv
import numpy as np

#This part here declares the variable "dickbutt", as the picture Dbutt.jpg at the same time it graysacels the image
tp = cv.imread("tinypic.png", 0)

for i in range (tp.shape[0]):
    for j in range (tp.shape[1]):
        print(tp[i][j])



