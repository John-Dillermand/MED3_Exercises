from tracemalloc import start
from unicodedata import decimal
import numpy as np

startBit = 1000
startingPlace = 1

sMax = 16


max = 16
startBit = 3
startBit2= 3
number = np.zeros(4)
oneZero = 1

binaryCounter = np.array([0,0,0,0,1,0,0,0])

for i in range(16):
    
    startBit=startBit+1
    binaryCounter[startBit] = 1
    if startBit > 7:
        startBit = startBit + 1
        binaryCounter[startBit] = 0
        print(np.packbits(binaryCounter, axis=-1))  
    else:
        startBit2 = startBit2 + 1
        binaryCounter[startBit2] = 0
        print(np.packbits(binaryCounter, axis=-1))  

    



    
    print(np.packbits(binaryCounter, axis=-1))
    
    
    



for x in (0,16):
    value=8/max*5
    


b = np.packbits(binaryCounter, axis=-1)

print(b)