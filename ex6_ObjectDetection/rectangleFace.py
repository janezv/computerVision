import cv2
import numpy as np
import matplotlib.pyplot as plt

video=cv2.VideoCapture(1)

while 1:
    b, imgJaz=video.read()
    
    face_cascade = cv2.CascadeClassifier('../DATA/haarcascades/haarcascade_frontalface_default.xml')


    def detect_face(img):
        face_img=img.copy()

        face_rects=face_cascade.detectMultiScale(face_img, scaleFactor=1.5, minNeighbors=3)

        for (x,y,w,h) in face_rects:
            cv2.rectangle(face_img,(x,y),(x+w,y+h),(255,255,255),6)
        
        return face_img

    result = detect_face(imgJaz)

    cv2.imshow('jaz',result)

    if cv2.waitKey(700)& 0xFF == ord('q'):
        break


print('Konec')