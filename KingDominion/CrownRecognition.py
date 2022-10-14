from ctypes import sizeof
import cv2 as cv
import numpy as np
import math
from numpy import array
import math
import linecache

FileName = "LabeledData\YellowBlank1.png"
crown    = 0
crown = str(crown)

regions = ["sand", "water", "grass"]

img = cv.imread(FileName)


height = img.shape[0]
width = img.shape[1]




Red = img[:, :, 2]
Green = img[:, :, 1]
Blue = img[:, :, 0]
np.set_printoptions(suppress=True)

averageRed    = str(((np.sum(Red))  /(height*width)))
averageGreen  = str(((np.sum(Green))/(height*width)))
averageBlue   = str(((np.sum(Blue)) /(height*width)))

averageRGB = ["RED=",averageRed,"GREEN=",averageGreen,"BLUE=",averageBlue]

currentAverageRed = 0
currentAverageGreen = 0
currentAverageBlue = 0



class Tile:
    def __init__(self, name, R, G, B, crowns, region):
        self.name = name
        self.R = R
        self.G = G
        self.B = B
        self.crowns = crowns
        self.region = region


# Making the tile
currentTile = Tile(FileName,averageRed,averageGreen,averageBlue,crown,"sand")












#printToData = ["FileName=",FileName,",""RED=",averageRed,",","GREEN=",averageGreen,",","BLUE=",averageBlue,",","region=",",","Crown=",crown]
dataSheet = open("dataSheet", "w")

printToData = ["FileName=",currentTile.name,"\n"
                "RED=",currentTile.R,"\n",
                "GREEN=",currentTile.G,"\n",
                "BLUE=",currentTile.B,"\n",
                "crown=",str(currentTile.crowns),"\n",
                "region=",currentTile.region,"\n"]

dataSheet.writelines(printToData)

dataSheet.close()


dataSheet = open("dataSheet", "r")

currentLine = dataSheet.read()
#print(currentLine)
#print(currentLine.find("RED="))



dataSheet.read(38)

dataSheet.close()



nextLine=0
currentAverageRed = linecache.getline("dataSheet",2+nextLine)
currentAverageGreen = linecache.getline("dataSheet",3+nextLine)
currentAverageBlue = linecache.getline("dataSheet",4+nextLine)


#getAveragesFromFile()

print(currentAverageRed)
print(currentAverageGreen)
print(currentAverageBlue)
