from xml.dom.minidom import Element
import numpy as np
import cv2 as cv

img = cv.imread("1.jpg")

#initialise variables with a default
lowerTresh = 0
higherTresh = 255

bino_thresh     = 5
canny_thresh    = 5
dialation       = 0
erode           = 0

# functions that update a variable, 
# then call image processing function
def change_lowerTresh(val):
    global lowerTresh
    lowerTresh = val
    thresh_callback()

#def change_higherTresh(val):
#    global higherTresh
#    higherTresh = val
#    thresh_callback()

def change_bino(val):
    global bino_thresh
    bino_thresh = val
    thresh_callback()

def change_dialation(val):
    global dialation
    dialation = val
    thresh_callback()

def change_erode(val):
    global erode
    erode = val
    thresh_callback()



def grayScale(val):
    imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# your function that processes the image



source_window = 'Source'
cv.namedWindow(source_window)


def thresh_callback():
    imggray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    cv.imshow("Source",imggray)
    
    ret,imggray = cv.threshold(imggray,lowerTresh,higherTresh,cv.THRESH_BINARY)
    imgErode     = cv.erode(src=imggray,dst=None,kernel=cv.getStructuringElement(cv.MORPH_RECT,(3,3)),iterations=erode)
    imgDialat     = cv.dilate(src=imgErode,dst=None,kernel=cv.getStructuringElement(cv.MORPH_RECT,(3,3)),iterations=dialation)





    cv.imshow("Source",imgDialat)









max_thresh = 255
thresh = 100
# create trackbars
cv.createTrackbar('Thres:', source_window, thresh, max_thresh, change_lowerTresh)
#cv.createTrackbar('higherTresh:', source_window, thresh, max_thresh, change_higherTresh)
cv.createTrackbar('Erode:', source_window, 0, 5, change_erode)
cv.createTrackbar('Dialation:', source_window, 0, 5, change_dialation)


thresh_callback()

cv.waitKey(0) & 0xFF  
cv.destroyAllWindows()