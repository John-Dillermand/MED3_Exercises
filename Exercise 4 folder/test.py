import cv2 as cv
import numpy as np
img_rgb = cv.imread('neon-text.png')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('Heart.png')
grayTemplate = cv.cvtColor(template, cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(img_gray,(21,21),0)

#Template matching
matchedTemplate = (cv.matchTemplate(img_gray,grayTemplate,cv.TM_CCOEFF_NORMED))


#Normalization of the image
image_norm = cv.normalize(matchedTemplate, None, norm_type=cv.NORM_MINMAX)

#Threshold of the image
imageThresh=cv.threshold(image_norm,25, 255,cv.THRESH_BINARY)

cv.imshow("grayImg",img_gray)
cv.imshow("Template",grayTemplate)
cv.imshow("BlurredImage",blur)
cv.imshow("matchedTemplate",matchedTemplate)
cv.imshow("normImage", image_norm)

#cv.imshow("imageNorm2",imageThresh)

cv.waitKey(0)
