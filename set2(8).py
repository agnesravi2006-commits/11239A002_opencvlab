import cv2
import matplotlib.pyplot as plt

img = cv2.imread("img.png")
if img is None:
    print("Image not found!")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.hist(gray.ravel(), 256, [0,256])
plt.title("Grayscale Histogram")

plt.subplot(1,2,2)
for i, col in enumerate(['b','g','r']):
    plt.plot(cv2.calcHist([img],[i],None,[256],[0,256]), color=col)
plt.title("Color Histogram")
plt.xlim([0,256])

plt.tight_layout()
plt.show()