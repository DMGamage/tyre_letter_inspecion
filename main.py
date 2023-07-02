import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('02.png')

width = 1000
height = 800


resized_image = cv2.resize(image, (width, height))

gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# Initialize default parameter values
kernel_size = (5, 5)
sigma = 0
alpha = 1.5
beta = -0.5


clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
equalized = clahe.apply(gray)

unsharp = cv2.addWeighted(gray,1.5,equalized,-0.5,0)

cv2.namedWindow('Unsharp Masking')

cv2.createTrackbar('Kernel Size', 'Unsharp Masking', 5, 20, lambda x: None)
cv2.createTrackbar('Sigma', 'Unsharp Masking', 0, 10, lambda x: None)
cv2.createTrackbar('Alpha', 'Unsharp Masking', 15, 30, lambda x: None)
cv2.createTrackbar('Beta', 'Unsharp Masking', 5, 10, lambda x: None)

while True:
    # Get current trackbar positions
    kernel_size_value = cv2.getTrackbarPos('Kernel Size', 'Unsharp Masking')
    sigma_value = cv2.getTrackbarPos('Sigma', 'Unsharp Masking')
    alpha_value = cv2.getTrackbarPos('Alpha', 'Unsharp Masking') / 10.0
    beta_value = cv2.getTrackbarPos('Beta', 'Unsharp Masking') / 10.0

    # Update parameters if changed
    if kernel_size_value % 2 == 1 and kernel_size_value != kernel_size[0]:
        kernel_size = (kernel_size_value, kernel_size_value)
    if sigma_value != sigma:
        sigma = sigma_value
    if alpha_value != alpha:
        alpha = alpha_value
    if beta_value != beta:
        beta = beta_value

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, kernel_size, sigma)

    # Calculate the sharpened image
    unsharp = cv2.addWeighted(gray, alpha, blurred, beta, 0)

    cv2.imshow('Original Image', blurred)
    cv2.imshow('Resized equalized', unsharp)



    if cv2.waitKey(1) == 27:
        break



# Display the original and resized images

cv2.waitKey(0)
cv2.destroyAllWindows()

