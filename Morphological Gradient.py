import cv2
import numpy as np

img = cv2.imread("img.png", 0)

if img is None:
    print("Image not found!")
    exit()

kernel = np.ones((5,5), np.uint8)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.imshow("Original", img)
cv2.imshow("Morphological Gradient", gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()