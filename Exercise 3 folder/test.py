import cv2 as cv
import numpy as np
import time

## Read as BGR
img = cv.imread("Rb.jpg")

## (1) Loop to calculate
ts = time.time()
H,W = img.shape[:2]
gray = np.zeros((H,W), np.uint8)
for i in range(H):
    for j in range(W):
        gray[i,j] = np.clip(0.07 * img[i,j,0]  + 0.72 * img[i,j,1] + 0.21 * img[i,j,2], 0, 255)

t = (time.time() -ts)
print("Loop: {:} ms".format(t*1000))

## (2) matrix multiply
ts = time.time()
w = np.array([[[ 0.07, 0.72,  0.21]]])
gray2 = cv.convertScaleAbs(np.sum(img*w, axis=2))
t = (time.time() -ts)
print("Loop: {:} ms".format(t*1000))

## (3) display
cv.imshow("img", img)
cv.imshow("gray", gray)
cv.imshow("gray2", gray2)
cv.waitKey()