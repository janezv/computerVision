import cv2
import numpy as np

arr=np.ones([700,500,3], np.uint8)

###########  blue ###################
blue=arr.copy()
blue[:,:,0]=np.ones([700,500], np.uint8)*255
cv2.imshow("blue",blue)
cv2.waitKey(900)

###########  green ###################
green=arr.copy()
green[:,:,1]=np.ones([700,500], np.uint8)*255
cv2.imshow("green",green)
cv2.waitKey(1200)

###########  red ###################
red=arr.copy()
red[:,:,2]=np.ones([700,500], np.uint8)*255
cv2.imshow("red",red)
cv2.waitKey()
