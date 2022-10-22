import cv2
import time

cap=cv2.VideoCapture('../DATA/myVideo.mp4')
framePerSecond=cap.get(cv2.CAP_PROP_FPS)

if cap.isOpened()==False:
    print('ERROR FILE NOT found or  wrong codec sed!')

while cap.isOpened():

    ret,frame =cap.read()

    if ret==True:
        # 20 Frame/second --> Namen je, da ni prehitro, da je prava hitrosto, torej hitrost Frame/s pri katerem je bil posnetek
        time.sleep(1/framePerSecond)
        cv2.imshow('frame',frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
