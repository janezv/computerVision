import numpy as np
import matplotlib.pyplot as plt

import cv2

img = cv2.imread('./00-puppy.jpg')
print(type(img))
print(img.shape)
plt.imshow(img)
# plt.show()

fix_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(fix_img)
# plt.show()


img_gray = cv2.imread('00-puppy.jpg', cv2.IMREAD_GRAYSCALE)
print(img_gray.shape)
plt.imshow(img_gray, cmap='gray')
# plt.show()

# RESIZE IMAGE
plt.imshow(fix_img)
plt.show()
print("*** Before and after reshaping:")
print(fix_img.shape)
new_img = cv2.resize(fix_img, (300, 400))
plt.imshow(new_img)
plt.show()

# RESIZE IMAGE BY RATIO
w_ratio = 0.8
h_ratio = 0.2
new_img2 = cv2.resize(fix_img, (0, 0), fix_img, w_ratio, h_ratio)
plt.imshow(new_img2)
plt.show()
print(new_img2.shape)


# flip image
new_img = cv2.flip(fix_img, 0)
plt.imshow(new_img)
plt.show()
new_img = cv2.flip(fix_img, 1)  # flip around vertical axes
plt.imshow(new_img)
plt.show()
new_img = cv2.flip(fix_img, -1)  # flip around vertical and horizontal axes
plt.imshow(new_img)
plt.show()

# save image
cv2.imwrite('new_image.jpg', fix_img)
