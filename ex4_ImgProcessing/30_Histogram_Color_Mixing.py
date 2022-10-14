from pickletools import uint8
import numpy
import cv2
import matplotlib.pyplot as plt

img = numpy.ones([480,640,3],numpy.uint8)

img[:,:,0] = numpy.ones([480,640])*255
img[:,:,1] = numpy.ones([480,640])*200
img[:,:,2] = numpy.ones([480,640])*10

cv2.imwrite('color_img.jpg', img)
cv2.imshow("image", img)
img.astype('int8')


hist_values0=cv2.calcHist(img,channels=[0],mask=None, histSize=[250], ranges=[0,280])
plt.plot(hist_values0)
plt.show()
cv2.waitKey()
