import imp


import cv2
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

pic = Image.open('../DATA/00-puppy.jpg')
# pic.show()
print(type(pic))

# translate picture to an array
pic_arr = np.asarray(pic)
print(type(pic_arr))
print(pic_arr.shape)
plt.imshow(pic_arr)
# plt.show()

# access just one channel
pic_red = pic_arr.copy()
plt.imshow((pic_red[:, :, 0]), cmap='gray')  # Red chanel values
plt.show()
plt.imshow((pic_red[:, :, 1]), cmap='gray')  # Green chanel values
plt.show()
plt.imshow((pic_red[:, :, 2]), cmap='gray')  # Blue chanel values
plt.show()
print(pic_red[:, :, 1])

# remove Green chanel
pic_red[:, :, 1] = 0
plt.imshow(pic_red)
plt.show()

# remove Blue chanel
pic_red[:, :, 2] = 0
plt.imshow(pic_red)
plt.show()
