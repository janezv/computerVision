import cv2
import numpy as np
import matplotlib.pyplot as plt

video=cv2.VideoCapture(0)

while 1:
    b, imgJaz=video.read()
    
    eye_cascade = cv2.CascadeClassifier('DATA/haarcascades/haarcascade_eye.xml')


    def detect_eyes(img):
        face_img=img.copy()

        eyes_rects=eye_cascade.detectMultiScale(face_img,scaleFactor=1.5, minNeighbors=2)

        for (x,y,w,h) in eyes_rects:
            cv2.rectangle(face_img,(x,y),(x+w,y+h),(255,255,255),6)
        
        return face_img

    result = detect_eyes(imgJaz)

    cv2.imshow('jaz',result)

    if cv2.waitKey(700)& 0xFF == ord('q'):
        break


print('Konec')