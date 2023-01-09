import cv2
import numpy as np


video=cv2.VideoCapture(1)

while 1:
    b, imgJaz=video.read()
    


    cv2.imshow('jaz',imgJaz)

    if cv2.waitKey(700)& 0xFF == ord('q'):
        break


print('Konec')