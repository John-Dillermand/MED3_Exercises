import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img_rgb = cv.imread('neon-text.png')
imgGray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('Heart.png')
templateGray = cv.cvtColor(template, cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(imgGray,(5,5),0)

#Template matching
matchedTemplate = cv.matchTemplate(imgGray,templateGray,cv.TM_CCOEFF_NORMED)

#A matrix to store the result the normalized image
resultImage = np.zeros((matchedTemplate.shape[0],matchedTemplate.shape[1]))

#Normalization of the image
print((matchedTemplate.shape[0],matchedTemplate.shape[1]))

image_norm = cv.normalize(matchedTemplate,resultImage,1,255, norm_type=cv.NORM_MINMAX)

#Threshold of the image
#ret, imageThresh = cv.threshold(matchedTemplate,1,255,cv.THRESH_BINARY)

#cv.imshow("grayImg",img_gray)
#cv.imshow("Template",grayTemplate)
#cv.imshow("BlurredImage",blur)
cv.imshow("matchedTemplate",matchedTemplate)
cv.imshow("normImage", resultImage)
#cv.imshow("ImageThresh",imageThresh)




cv.waitKey(0)
