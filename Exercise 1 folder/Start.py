import cv2 as cv
import numpy as np

#This part here declares the variable "dickbutt", as the picture Dbutt.jpg at the same time it graysacels the image
dickbutt = cv.imread("Dbutt.jpg", cv.IMREAD_GRAYSCALE)



#Here is the commando to show the window
cv.imshow("Our window", dickbutt)


#
print(f"Calculation:{type(dickbutt)}")
cv.waitKey(0)