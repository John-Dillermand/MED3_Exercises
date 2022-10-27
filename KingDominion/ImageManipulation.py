from xml.dom.minidom import Element
import numpy as np
import cv2 as cv

img = cv.imread("1.jpg")

#initialise variables with a default
lowerTresh = 0
higherTresh = 255


dialation       = 0
erode           = 0
minEdge         = 1
maxEdge         = 1
apatureSize     = 5


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


def change_minEdge(val):
    global minEdge
    minEdge = val
    thresh_callback()

def change_maxEdge(val):
    global maxEdge
    maxEdge = val
    thresh_callback()

def change_apatureSize(val):
    global apatureSize
    apatureSize = val
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
    imgErode     = cv.erode(src=imggray,dst=None,kernel=cv.getStructuringElement(cv.MORPH_RECT,(5,5)),iterations=erode)
    imgDialat     = cv.dilate(src=imgErode,dst=None,kernel=cv.getStructuringElement(cv.MORPH_RECT,(5,5)),iterations=dialation)
    #denoised = cv.fastNlMeansDenoising(src=imgDialat,h=apatureSize,templateWindowSize=7,searchWindowSize=21)
    #edges = cv.Canny(imgDialat,minEdge,maxEdge,apatureSize)

    #edges = cv.Canny(src=imgDialat,dst=None,threshold1=minEdge,threshold2=maxEdge,apertureSize=apatureSize,L2gradient=False)
    cv.imshow("Source",imgDialat)









max_thresh = 255
thresh = 100
# create trackbars
cv.createTrackbar('Thres:', source_window, thresh, max_thresh, change_lowerTresh)
#cv.createTrackbar('higherTresh:', source_window, thresh, max_thresh, change_higherTresh)
cv.createTrackbar('Erode:', source_window, 0, 5, change_erode)
cv.createTrackbar('Dialation:', source_window, 0, 5, change_dialation)
cv.createTrackbar('MinEdge:', source_window, 0, 200, change_minEdge)
cv.createTrackbar('MaxEdge:', source_window, 0, 200, change_maxEdge)
#cv.createTrackbar('ApatureSizeEdge:', source_window, 0, 10, change_apatureSize)

thresh_callback()

cv.waitKey(0) & 0xFF  
cv.destroyAllWindows()