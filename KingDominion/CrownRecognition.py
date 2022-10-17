from pickletools import uint8
import cv2 as cv
import numpy as np
import math
from numpy import array
import math

FileName = "4.jpg"


img = cv.imread(FileName) 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
avrgIntensity=np.sum(gray)/(gray.shape[0]*gray.shape[1])
intImg=(110/avrgIntensity)*img
print(avrgIntensity)
cv.imshow("dfsa", intImg)
cv.imshow("sdfas",img)
tilesVertical = 5
tilesHorizontal = 5
height = img.shape[0] 
width = img.shape[1]
tileWidth = math.floor(width/5)
tileHeight= math.floor(height/5)
imgArray= np.array((5,5))
sliceList = []

def SliceImg():
    for x in range(5):
        sliceList.append([])
        for y in range(5):
            sliceList[x].append(img[y*tileHeight:(y+1)*tileHeight,x*tileWidth:(x+1)*tileWidth])

SliceImg()
img1=sliceList[0][0]
img2=sliceList[1][0]
img3=sliceList[4][4]

Red1 = img1[:, :, 2] 
Green1 = img1[:, :, 1] 
Blue1 = img1[:, :, 0] 

Red2 = img2[:, :, 2] 
Green2 = img2[:, :, 1] 
Blue2 = img2[:, :, 0] 

Red3 = img3[:, :, 2] 
Green3 = img3[:, :, 1] 
Blue3 = img3[:, :, 0] 

np.set_printoptions(suppress=True) 

height1 = img1.shape[0] 
width1 = img1.shape[1] 
height2 = img2.shape[0] 
width2 = img2.shape[1] 
height3 = img3.shape[0] 
width3 = img3.shape[1] 
avrgRed1=np.sum(Red1)/(height1*width1)
avrgGreen1=np.sum(Green1)/(height1*width1)
avrgBlue1=np.sum(Blue1)/(height1*width1)

avrgRed2=(np.sum(Red2))/(height1*width1)
avrgGreen2=(np.sum(Green2))/(height1*width1)
avrgBlue2=(np.sum(Blue2))/(height1*width1)

avrgRed3=np.sum(Red3)/(height3*width3)
avrgGreen3=np.sum(Green3)/(height3*width3)
avrgBlue3=np.sum(Blue3)/(height3*width3)
avrgRedTotal=(avrgRed1+avrgRed2+avrgRed3)/3
avrgBlueTotal=(avrgBlue1+avrgBlue2+avrgBlue3)/3
avrgGreenTotal=(avrgGreen1+avrgGreen2+avrgGreen3)/3
#print("Picture 1")
#print(avrgRed1)
#print(avrgGreen1)
#print(avrgBlue1)
#print("Picture 2")
#print(avrgRed2)
#print(avrgGreen2)
#print(avrgBlue2)
#print("Picture 3")
#print(avrgRed3)
#print(avrgGreen3)
#print(avrgBlue3)


#print("Red = "+  str(avrgRedTotal))
#print("Green = "+str(avrgGreenTotal))
#print("Blue = "+ str(avrgBlueTotal))

cv.imshow("1",img1)
cv.imshow("2",img2)
cv.imshow("3", img3)
cv.waitKey(0)

 

#cv.imshow("Image",img)
#cv.waitKey(0)

#print(bayerOutput)