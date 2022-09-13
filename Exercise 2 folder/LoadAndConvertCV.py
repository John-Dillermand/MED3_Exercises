import cv2 as cv
import numpy as np

input_image = cv.imread("Rb.jpg")
output_image = np.zeros(input_image.shape, dtype=input_image.dtype)





cv.imshow("Input image", input_image)
cv.imshow("Output image", output_image)
cv.waitKey(0)