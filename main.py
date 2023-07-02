import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('02.png')

width = 1000
height = 800


resized_image = cv2.resize(image, (width, height))

gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
equalized = clahe.apply(gray)


# Display the original and resized images
cv2.imshow('Original Image', resized_image)
cv2.imshow('Resized equalized', equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()

