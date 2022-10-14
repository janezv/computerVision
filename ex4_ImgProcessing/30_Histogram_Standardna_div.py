from pickletools import uint8
import numpy
import cv2
import matplotlib.pyplot as plt
import random


img = numpy.ones([960,1280,3],numpy.uint8)

for x in range(960):
    for y in range(1280):
        img[x,y,0]=random.randint(200,250)

for x in range(960):
    for y in range(1280):
        img[x,y,1]=random.randint(110,130)

for x in range(960):
    for y in range(1280):
        img[x,y,2]=random.randint(35,40)


cv2.imshow("image", img)


hist_values0=cv2.calcHist(img,channels=[0],mask=None, histSize=[250], ranges=[0,280])
plt.plot(hist_values0)
plt.show()
cv2.waitKey()
