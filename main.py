import cv2


image = cv2.imread('02.png')

width = 1000
height = 800


resized_image = cv2.resize(image, (width, height))

# Display the original and resized images
cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

