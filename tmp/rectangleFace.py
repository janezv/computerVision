import cv2
import numpy as np
import matplotlib.pyplot as plt
import keyboard  # using module keyboard


video=cv2.VideoCapture(1)

def enlargeImg(img):
    img.shape
    enlarged_image = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_LINEAR)
    return enlarged_image

def scaleImg(img, faktorScale):
    faktorScale=faktorScale+0.08 # Malo povečaj faktor zmanjšanja-Experimenting
    imgCopy=img.copy()
    scaled_image = cv2.resize(imgCopy, None, fx=faktorScale, fy=faktorScale, interpolation=cv2.INTER_LINEAR)
    #cv2.imshow('imgHf',scaled_image)
    return scaled_image

def scaleImg2(img, faktorScale):
    faktorScale=faktorScale+0.16
    imgCopy=img.copy()
    scaled_image = cv2.resize(img, None, fx=faktorScale, fy=faktorScale, interpolation=cv2.INTER_LINEAR)
    #cv2.imshow('imgHf',scaled_image)
    return scaled_image

def displayImg(img):
    # cv2.namedWindow('Img',cv2.WND_PROP_FULLSCREEN) 
    # cv2.setWindowProperty("Img", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN) 
    cv2.imshow('Img',img)

def embedHorseImg(x1,y1,x2,y2,img, imgSmall):
    w = abs(x1-x2)
    h = abs(y1-y2)
    img=imgSmall.copy()
    imgSmall.shape[0]
    imgSmall.shape[1]
    # print("Slika ime w = {0}, h= {1}".format(*[w,h]))
    # print("Slika s konjem ima dimenzije w = {0}, h= {1}".format(*[imgSmall.shape[0], imgSmall.shape[1] ]))
    if img.shape[0] > w:
        k=w/imgSmall.shape[0]
        imgOut=scaleImg(img, k)
    if imgOut.shape[1]> h:
        k=h/imgSmall.shape[1]
        imgOut=scaleImg(imgOut, k)
    return imgOut, imgOut.shape[0], imgOut.shape[1]

def embedImg(x1,y1,x2,y2,img, imgSmall):
    w = abs(x1-x2)
    h = abs(y1-y2)
    img=imgSmall.copy()
    img.shape[0]
    img.shape[1]
    # print("Slika ime w = {0}, h= {1}".format(*[w,h]))
    # print("Slika s konjem ima dimenzije w = {0}, h= {1}".format(*[imgSmall.shape[0], imgSmall.shape[1] ]))
    if img.shape[0] > w:
        k=w/img.shape[0]
        imgOut=scaleImg2(img, k)
    if imgOut.shape[1]> h:
        k=h/imgOut.shape[1]
        imgOut=scaleImg2(imgOut, k)
    return imgOut, imgOut.shape[0], imgOut.shape[1]
   

def manipulateImg(img, dimension ):
    x,y,w,h = dimension
    
    # Read the last key press from the console input buffer
    if keyboard.is_pressed('h'):
        imgHf = cv2.imread('HorseFace.jpg')
        imgOut, h, w = embedHorseImg(x-30,y-90,x+w+40, y+h+50,img, imgHf)
        img[y-90:y-90+h,x-30:x-30+w]=imgOut
    elif keyboard.is_pressed('m'):
        imgMf = cv2.imread('monkeyFace.jpg')
        imgOut, h,w = embedImg(x-30,y-90,x+w+40, y+h+50,img, imgMf)
        img[(y-75):(y-75+h),(x-95):(x-95+w)]=imgOut
    else:
        cv2.rectangle(img,(x-30,y-90),(x+w+40, y+h+50),(255,255,255),6)
    return img
    

while 1:
    b, img=video.read()
    
    face_cascade = cv2.CascadeClassifier('DATA/haarcascades/haarcascade_frontalface_default.xml')
    imgL = enlargeImg(img)

    def detect_face(img):
        face_img=img.copy()

        face_rects=face_cascade.detectMultiScale(face_img, scaleFactor=1.5, minNeighbors=3)

        for (x,y,w,h) in face_rects:
            dimension=(x,y,w,h)
            face_img = manipulateImg(face_img, dimension)
            
        
        return face_img

    result = detect_face(imgL)

    displayImg(result)

    if cv2.waitKey(1)& 0xFF == ord('q'):
        break


print('Konec')