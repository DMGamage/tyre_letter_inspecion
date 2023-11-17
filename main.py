import cv2
import numpy as np

# Load the image
image = cv2.imread('result.png')
resized_image = cv2.resize(image, (1024, 1024))

# Convert the image to HSV color space
hsv_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2HSV)

# Extract the V (Value) channel
v_channel = hsv_image[:, :, 2]

# Convert the image to LAB color space
lab_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2LAB)

# Extract the L (Luminance) channel
l_channel = lab_image[:, :, 0]

# Apply histogram equalization to the selected channels
equalized_v_channel = cv2.equalizeHist(v_channel)
equalized_l_channel = cv2.equalizeHist(l_channel)

# Apply Canny edge detector to the enhanced V channel
edges = cv2.Canny(equalized_v_channel, 30, 100)

# Display the original image, enhanced image, and edges
cv2.imshow('Original Image', resized_image)
cv2.imshow('Enhanced V Channel', equalized_v_channel)
cv2.imshow('Canny Edges', edges)

# Wait for a key event and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
