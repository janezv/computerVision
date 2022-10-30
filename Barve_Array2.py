import cv2
import numpy as np
import matplotlib.pyplot as plt
import random

cap=cv2.VideoCapture(1)
 
while 1:

    # prikaži samo rdeč spekter
    Bwork, image =cap.read()
    RedSpectrum=image[:,:,2]
    print("Rdeči spekter: ",RedSpectrum.shape)
    cv2.imshow('image',RedSpectrum)

    # put blue spectrum to the maximum
    Bwork, image =cap.read()
    blueArray=np.ones((480,640),dtype=np.uint64)
    blueArray=blueArray*255
    image[:,:,0]=blueArray
    cv2.imshow("Blue on Max", image)

    # put noice to the green spectrum
    Bwork, image =cap.read()
    blueArray=np.ones((480,640),dtype=np.uint64)
    for x in range(480):
        for y in range(640):
            image[x,y,1]=random.randint(0,250)
    cv2.imshow('Noice on Green spectrum',image)


    if cv2.waitKey(600) & 0xff==ord('q'):
        break