import cv2
import numpy as np

import matplotlib.pyplot as plt

blank_img = np.zeros(shape=(512, 512, 3), dtype=np.int16)
blank_img.shape


cv2.rectangle(blank_img, pt1=(384, 0), pt2=(
    510, 150), color=(0, 255, 0), thickness=10)

plt.imshow(blank_img)
plt.show()
