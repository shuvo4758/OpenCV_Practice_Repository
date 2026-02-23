# find Contours
# contours, herarchy = cv2.findContours(image, mode, method)

# draw Contours
# cv2.drawContours(image, contours, contour_index, color, thickness)

import cv2

image = cv2.imread('triangle.avif')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY)

# find Contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# draw Contours
cv2.drawContours(image, contours, -1, (0, 255, 0), 5)

cv2.imshow('Contour image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()