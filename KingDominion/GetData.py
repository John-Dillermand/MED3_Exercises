from ctypes import sizeof
import cv2 as cv
import numpy as np
import math
from numpy import array
import math
import linecache

np.set_printoptions(suppress=True)

def compareValues(currentAverageRed,currentAverageGreen,currentAverageBlue):
    for nextLine in range (0,6):
        loadingCurrentAverageRed   = linecache.getline("dataSheet",2+nextLine*6)
        loadingCurrentAverageGreen = linecache.getline("dataSheet",3+nextLine*6)
        loadingCurrentAverageBlue  = linecache.getline("dataSheet",4+nextLine*6)
        crown                      = linecache.getline("dataSheet",5+nextLine*6)
        region                     = linecache.getline("dataSheet",6+nextLine*6)
        DSAverageRed   = (loadingCurrentAverageRed  [loadingCurrentAverageRed.find  ("=")+1:loadingCurrentAverageRed.find(".")])
        DSAverageGreen = (loadingCurrentAverageGreen[loadingCurrentAverageGreen.find("=")+1:loadingCurrentAverageGreen.find(".")])
        DSAverageBlue  = (loadingCurrentAverageBlue [loadingCurrentAverageBlue.find ("=")+1:loadingCurrentAverageBlue.find(".")])
        crown          = (crown [crown.find ("=")+1:crown.find(".")])
        region         = (region [region.find ("=")+1:region.find(".")])


        DSAverageRed   = int (DSAverageRed)
        DSAverageGreen = int (DSAverageGreen)
        DSAverageBlue  = int (DSAverageBlue)

        if DSAverageRed-10 < currentAverageRed < DSAverageRed+10 and DSAverageGreen-10 < currentAverageGreen < DSAverageGreen+10 and DSAverageBlue-10 < currentAverageBlue < DSAverageBlue+10:
            print("jonathan er retarded \n" +  crown +"\n" + region)


currentAverageRed = 100
currentAverageGreen = 141
currentAverageBlue = 31

compareValues(currentAverageRed,currentAverageGreen,currentAverageBlue)













