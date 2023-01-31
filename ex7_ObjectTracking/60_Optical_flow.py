import cv2
import numpy as np


cap=cv2.VideoCapture(1)

ret, frame1 = cap.read()

# Grab a grayscale image (We will refer to this as the previous frame)
prvsImg = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

hsv_mask = np.zeros_like(frame1)
hsv_mask[:,:,1] = 255

while True:
    ret, frame2 = cap.read()

    nextImg = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    flow=cv2.calcOpticalFlowFarneback(prvsImg,nextImg,None,0.5,3,15,3,5,1.2,0)

    mag, ang = cv2.cartToPolar(flow[:,:,0], flow[:,:,1],angleInDegrees=True)  # spremeni [y,x] -> polar system [magnitude , angle]

    hsv_mask[:,:,0]=ang/2    # chanel 0 je Hue --> Torej barva med 0-360° kjer je 44°=Oranžna, 0° & 360°=Rdeča
    hsv_mask[:,:,2]=cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX) # chanel 2 je Value

    bgr=cv2.cvtColor(hsv_mask, cv2.COLOR_HSV2BGR)
    cv2.imshow('frame',bgr)

    k= cv2.waitKey(10) & 0xFF #esc
    if k == 27:
        break

    prvsImg=nextImg

    
cap.release()
cv2.destroyAllWindows()