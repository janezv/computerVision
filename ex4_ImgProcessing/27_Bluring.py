
from tkinter import font
import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_img():
    img=cv2.imread('./data/bricks.jpg').astype(np.float32) / 255
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return img

def reset_img():
    img=load_img()
    font=cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img, text='bricks', org=(10,600),fontFace=font,fontScale=10,color=(255,0,0),thickness=4)
    print('reset')


img=load_img()
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, text='bricks', org=(10,600),fontFace=font,fontScale=10,color=(255,0,0),thickness=4)

cv2.imshow('im',img)

displayArr=np.ones(shape=(5,5),dtype=np.float32)/25
print(displayArr)

dst=cv2.filter2D(img,-1,displayArr)
cv2.imshow('dA',dst)


imgama=np.power(img,0.25)
cv2.imshow('gama',imgama)

blurred=cv2.blur(img,ksize=(10,10))
cv2.imshow('blurred',blurred)


blurred_img_g=cv2.GaussianBlur(img,(5,5),10)
cv2.imshow('gaussianBlur',blurred_img_g)


mediam_result=cv2.medianBlur(img,5)
cv2.imshow('mediam_result',mediam_result)


img=cv2.imread('DATA/sammy.jpg')
cv2.imshow('img',img)

noise_img=cv2.imread('DATA/sammy_noise.jpg')
noise_img2=cv2.cvtColor(noise_img,cv2.COLOR_RGB2BGR)
cv2.imshow('noise_img',noise_img2)

median=cv2.medianBlur(noise_img2,5)
cv2.imshow('popravek noise z medianBlur',median)

reset_img()
blur=cv2.bilateralFilter(noise_img2,9,75,75)
cv2.imshow('sigma blur',blur)

while 1:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()





