import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('1.jpg')        

#Templates
templateForest = cv.imread('crownForest.jpg')  





tilesInImage = 5**2

height, width = img.shape[0], img.shape[1]

tileHeight = round(height / 5)
tileWidth  = round(width / 5)





#Slice the mf image and it in TileHolder
tileHolder = []
matchingHolder = []
for i in range(0,500,100):
    for j in range(0,500,100):
        currenImage = img[i:tileHeight+i,j:tileWidth+j]
        tileHolder.append(currenImage)


templateMatchResult = cv.matchTemplate(img,templateForest,cv.TM_CCOEFF_NORMED)

#cv.matchTemplate(img,templateForest,cv.TM_SQDIFF)



(minVal, maxVal, minLoc, maxLoc) = cv.minMaxLoc(templateMatchResult)
(startX, startY) = maxLoc

endX = startX + templateForest.shape[1]
endY = startY + templateForest.shape[0]
cv.rectangle(img, (startX, startY), (endX, endY), (255, 0, 0), 2)




cv.imshow("show",img)
cv.imshow("Template",cv.matchTemplate(img,templateForest,cv.TM_CCOEFF_NORMED))
cv.waitKey(0)




#Show the mf

#for i in range(8,9):
#    cv.imshow("show",tileHolder[i])
#    cv.imshow("Template",cv.matchTemplate(tileHolder[9],templateForest,cv.TM_CCOEFF))
#    cv.waitKey(0)




