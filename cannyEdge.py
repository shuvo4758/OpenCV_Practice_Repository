# edges = cv2.Canny(image, threshold1, threahold2)
# image must be in GrayScale

import cv2

image = cv2.imread('flower.jpeg', cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(image, 50, 150)

cv2.imshow('Original image', image)
cv2.imshow('After applying Median blur', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()

