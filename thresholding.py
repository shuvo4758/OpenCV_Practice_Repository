# ret, thresholded_image = cv2.threshold(image, thresh_value, max_value, method)
# thresh_value = 0 to 255 (best --> 100, 120, 150)
# max_value = 255
# image must be in GrayScale

import cv2

image = cv2.imread('person.jpeg', cv2.IMREAD_GRAYSCALE)

ret, thresholded_image = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)

cv2.imshow('Original image', image)
cv2.imshow('Thresholded image', thresholded_image)

cv2.waitKey(0)
cv2.destroyAllWindows()