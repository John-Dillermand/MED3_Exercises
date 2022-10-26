import cv2 as cv

img = cv.imread('1.jpg',0)

def nothing(x):
    pass

cv.namedWindow("image")

#Create TrackBars
cv.createTrackbar('LowThresh', 'image', 0, 254, nothing)
cv.createTrackbar('HighThresh', 'image', 0, 255, nothing)


switch = 'OFF-ON'
cv.createTrackbar(switch, 'image',0,1,nothing)


while(1):
    cv.imshow("image",img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    #Get the current positions of the track bars
    lowThresh = cv.getTrackbarPos("LowThresh" ,"image")
    highThresh= cv.getTrackbarPos("HighThresh","image")
    s         = cv.getTrackbarPos(switch,"image")


    img[:] = [lowThresh,highThresh]

cv.destroyAllWindows()