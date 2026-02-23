# cv2.bitwise_and(image1, imag2)
# cv2.bitwise_or(image1, imag2)
# cv2.bitwise_not(image1)

# image1 and image2 height,width must be same
# use only black and white images

import cv2
import numpy as np

image1 = np.zeros((300, 300), dtype='uint8')
image2 = np.zeros((300, 300), dtype='uint8')

cv2.circle(image1, (150, 150), 100, 255, -1)
cv2.rectangle(image2, (100, 100), (250, 250), 255, -1)

bitwise_and = cv2.bitwise_and(image1, image2)
bitwise_or = cv2.bitwise_or(image1, image2)
bitwise_not = cv2.bitwise_not(image1)

cv2.imshow('image1', image1)
cv2.imshow('image2', image2)
cv2.imshow('bitwise_and', bitwise_and)
cv2.imshow('bitwise_or', bitwise_or)
cv2.imshow('bitwise_not', bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()
