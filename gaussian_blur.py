# blurred_image = cv2.GaussianBlur(image, (kernel_size_x, kernel_size_y), sigma)
# kernel_size_x, kernel_size_y --> always odd (3, 3) or (5,5)
# sigma --> blur intensity

import cv2

image = cv2.imread('nature.jpeg')

cv2.imshow('Original image', image)
blurred_image = cv2.GaussianBlur(image, (21,21), 6)

cv2.imshow('After applying Gaussian blur', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()