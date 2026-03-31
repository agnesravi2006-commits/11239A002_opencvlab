import  cv2

img = cv2.imread("bex1.png")

if img is None:
    print("Error: Could not read the image.")
else:
    cv2.imshow("Original Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
