from colorsys import rgb_to_hls
import cv2 as cv
import numpy as np
import math

img = cv.imread("753.jpg")


height = img.shape[0]
width = img.shape[1]


bgr = np.float32(img)/255


np.set_printoptions(suppress=True)

cv.inRange

HSIOutput = np.zeros ((height,width,3),np.uint8)


hue = np.zeros((height,width))

blue = bgr[:,:,0]
green = bgr[:,:,1]
red = bgr[:,:,2]


for i in range(0, height):
    for j in range(0, width):
        hue[i][j] = 0.5 * ((red[i][j] - green[i][j]) + (red[i][j] - blue[i][j])) / \
                    math.sqrt((red[i][j] - green[i][j])**2 +
                            ((red[i][j] - blue[i][j]) * (green[i][j] - blue[i][j])))
        hue[i][j] = math.acos(hue[i][j])

        if blue[i][j] <= green[i][j]:
            hue[i][j] = hue[i][j]
        else:
            hue[i][j] = ((360 * math.pi) / 180.0) - hue[i][j]

cv.imshow("Image",hue)
