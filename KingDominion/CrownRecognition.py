from ctypes import sizeof
import cv2 as cv
import numpy as np
import math
from numpy import array
import math
import linecache

np.set_printoptions(suppress=True)



currentAverageRed = 100
currentAverageGreen = 141
currentAverageBlue = 31

DSAverageRed   = 0
DSAverageGreen = 0
DSAverageBlue  = 0





for nextLine in range (0,6):
    loadingCurrentAverageRed = linecache.getline("dataSheet",2+nextLine*6)
    loadingCurrentAverageGreen = linecache.getline("dataSheet",3+nextLine*6)
    loadingCurrentAverageBlue = linecache.getline("dataSheet",4+nextLine*6)
    DSAverageRed   = (loadingCurrentAverageRed  [loadingCurrentAverageRed.find  ("=")+1:loadingCurrentAverageRed.find(".")])
    DSAverageGreen = (loadingCurrentAverageGreen[loadingCurrentAverageGreen.find("=")+1:loadingCurrentAverageGreen.find(".")])
    DSAverageBlue  = (loadingCurrentAverageBlue [loadingCurrentAverageBlue.find ("=")+1:loadingCurrentAverageBlue.find(".")])
    DSAverageRed   = int (DSAverageRed)
    DSAverageGreen = int (DSAverageGreen)
    DSAverageBlue  = int (DSAverageBlue)

    if DSAverageRed-10 < currentAverageRed < DSAverageRed+10 and DSAverageGreen-10 < currentAverageGreen < DSAverageGreen+10 and DSAverageBlue-10 < currentAverageBlue < DSAverageBlue+10:
        print("jonathan er retarded")


