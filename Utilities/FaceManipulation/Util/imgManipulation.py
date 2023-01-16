import cv2
import keyboard  # using module keyboard

class manipulation:
     
    def enlargeImg(self,img):
        img.shape
        enlarged_image = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_LINEAR)
        return enlarged_image

    def scaleImg(self,img, faktorScale):
        faktorScale=faktorScale+0.08 # Malo povečaj faktor zmanjšanja-Experimenting
        imgCopy=img.copy()
        scaled_image = cv2.resize(imgCopy, None, fx=faktorScale, fy=faktorScale, interpolation=cv2.INTER_LINEAR)
        #cv2.imshow('imgHf',scaled_image)
        return scaled_image

    def scaleImg2(self,img, faktorScale):
        faktorScale=faktorScale+0.16
        imgCopy=img.copy()
        scaled_image = cv2.resize(img, None, fx=faktorScale, fy=faktorScale, interpolation=cv2.INTER_LINEAR)
        #cv2.imshow('imgHf',scaled_image)
        return scaled_image

    def embedHorseImg(self,x1,y1,x2,y2,img, imgSmall):
        w = abs(x1-x2)
        h = abs(y1-y2)
        img=imgSmall.copy()
        imgSmall.shape[0]
        imgSmall.shape[1]
        # print("Slika ime w = {0}, h= {1}".format(*[w,h]))
        # print("Slika s konjem ima dimenzije w = {0}, h= {1}".format(*[imgSmall.shape[0], imgSmall.shape[1] ]))
        if img.shape[0] > w:
            k=w/imgSmall.shape[0]
            imgOut=self.scaleImg(img, k)
        if imgOut.shape[1]> h:
            k=h/imgSmall.shape[1]
            imgOut=self.scaleImg(imgOut, k)
        return imgOut, imgOut.shape[0], imgOut.shape[1]

    def embedImg(self,x1,y1,x2,y2,img, imgSmall):
        w = abs(x1-x2)
        h = abs(y1-y2)
        img=imgSmall.copy()
        img.shape[0]
        img.shape[1]
        # print("Slika ime w = {0}, h= {1}".format(*[w,h]))
        # print("Slika s konjem ima dimenzije w = {0}, h= {1}".format(*[imgSmall.shape[0], imgSmall.shape[1] ]))
        if img.shape[0] > w:
            k=w/img.shape[0]
            imgOut=self.scaleImg2(img, k)
        if imgOut.shape[1]> h:
            k=h/imgOut.shape[1]
            imgOut=self.scaleImg2(imgOut, k)
        return imgOut, imgOut.shape[0], imgOut.shape[1]
    

    def manipulateImg(self,img, dimension ):
        x,y,w,h = dimension
        
        # Read the last key press from the console input buffer
        if keyboard.is_pressed('h'):
            imgHf = cv2.imread('Util\HorseFace.jpg')
            imgOut, h, w = self.embedHorseImg(x-30,y-90,x+w+40, y+h+50,img, imgHf)
            img[y-90:y-90+h,x-30:x-30+w]=imgOut
        elif keyboard.is_pressed('m'):
            imgMf = cv2.imread('Util\monkeyFace.jpg')
            imgOut, h,w = self.embedImg(x-30,y-90,x+w+40, y+h+50,img, imgMf)
            img[(y-75):(y-75+h),(x-95):(x-95+w)]=imgOut
        else:
            cv2.rectangle(img,(x-30,y-90),(x+w+40, y+h+50),(255,255,255),6)
        return img