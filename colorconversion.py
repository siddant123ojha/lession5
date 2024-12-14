import cv2
import matplotlib.pyplot as plt
image=cv2.imread("3x3 logo.png")
image_rgb=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("RGB Image")
plt.show()
gray_image=cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
plt.imshow(gray_image, cmap="gray")
plt.title("Gray image")
plt.show()

cropping=image[100:300,200:400]
cropping_rgb=cv2.cvtColor(cropping, cv2.COLOR_BGR2RGB)
plt.imshow(cropping_rgb)
plt.title("Cropped region")
plt.show()