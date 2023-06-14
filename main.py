import cv2
image = cv2.imread('01.jpg',0)
blurred_image = cv2.GaussianBlur(image, (3, 3), 0)   #Please Check or addded Median Filter

cv2.imshow('Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

