# cv2.filter2D(scr, ddepth, kernel)

import cv2
import numpy as np

image = cv2.imread('lowResolution.jpg')

sharpen_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

sharped_image = cv2.filter2D(image, -1, sharpen_kernel)

cv2.imshow('Original image', image)
cv2.imshow('After applying Sharpening', sharped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
