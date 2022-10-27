from inspect import BoundArguments
from pickletools import uint8
from turtle import width
import cv2 as cv
import numpy as np
from collections import deque


img = cv.imread('shapes.png',0)
height, width = img.shape[0], img.shape[1]


currrent_ID = 1


#crosshair_list = ["crosshair_top","crosshair_bot","crosshair_right","crosshair_left"]
#    for crosshair_position in crosshair_list:
#        print(crosshair_position)

grass_array = np.zeros((height,width))


def ignite_fire(x,y):


    burn_queue = [(1,2),(1,3)]

    top      = img [1-x,y]
    bot      = img [1+x,y]

    right    = img [x,1+y]
    left     = img [x,1-y]

    top = 1
    bot = 1
    right = 1
    left   = 1


    
    crosshair_top   = 1
    crosshair_bot   = 1
    crosshair_right = 1    
    crosshair_left  = 1


    if crosshair_top == top:
        burn_queue.append((1-x,y))

    if crosshair_left == left:
        burn_queue.append((x,1-y))

    if crosshair_bot == bot:
        burn_queue.append((1+x,y))

    if crosshair_right == right:
        burn_queue.append((x,1-y))



    current_burn = burn_queue.pop()
    print(type(current_burn))

    #grass_array(current_burn) = 1



    

    






ignite_fire(1,2)







ret, thresh = cv.threshold(img,127,255,cv.THRESH_BINARY)
kernel = np.ones((5,5))
offset = len(kernel) //2

erodeImage = np.zeros((height,width),np.uint8)
dilationImage = np.zeros((height,width),np.uint8)

#for x in range(offset,width-offset):
#    for y in range(offset,height-offset):
#        print("")
#



#cv.imshow("Zeros", grass_array)
#cv.imshow("shapes", img)
#cv.waitKey(0)