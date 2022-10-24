import imp
import cv2
import time
import matplotlib.pyplot as plt

### GLOBAL VARIABLES
centerPoint=(0,0)
clicked=False

 # mouse callback function
def draw_circle(event,x,y,flags,param):
    global clicked, centerPoint
    if event==cv2.EVENT_LBUTTONDOWN:
        centerPoint=(x,y)
        clicked=True




cv2.namedWindow('frameWind')
cv2.setMouseCallback('frameWind', draw_circle) 

cap=cv2.VideoCapture(1)

while 1:
    b, frame=cap.read()

    if clicked:
        cv2.circle(img=frame, center=centerPoint,radius=50, color=(255,0,0),thickness=8)

    cv2.imshow('frameWind',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

