import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.ones([480,640,3], np.uint8)

### Modra prevladujoca barva
img[:,:,0] = np.ones([480,640])*255
img[:,:,1] = np.ones([480,640])*40
img[:,:,2] = np.ones([480,640])*10
cv2.imshow('prevladujoca Modra', img)

### Zelena prevladujoca barva
img[:,:,0] = np.ones([480,640])*1
img[:,:,1] = np.ones([480,640])*140
img[:,:,2] = np.ones([480,640])*2
cv2.imshow('prevladujoca Zelena', img)

### Rdeča prevladujoca barva
img[:,:,0] = np.ones([480,640])*10
img[:,:,1] = np.ones([480,640])*20
img[:,:,2] = np.ones([480,640])*255
cv2.imshow('prevladujoca Rdeca', img)

### Rdeča-Modra barva
img[:,:,0] = np.ones([480,640])*127
img[:,:,1] = np.ones([480,640])*20
img[:,:,2] = np.ones([480,640])*127
cv2.imshow('Rdeca-Modra', img)

cv2.waitKey()