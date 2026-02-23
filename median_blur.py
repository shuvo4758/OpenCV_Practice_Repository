import cv2

image = cv2.imread('noisy.jpeg')

blurred_image = cv2.medianBlur(image, 11)


cv2.imshow('Original image', image)
cv2.imshow('After applying Median blur', blurred_image)

cv2.waitKey(0)
cv2.destroyAllWindows()