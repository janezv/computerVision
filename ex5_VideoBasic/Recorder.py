from turtle import width
import cv2 

cap=cv2.VideoCapture(0)

width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
framePerSecond=cap.get(cv2.CAP_PROP_FPS)
print("Withd:", width,"; Height: ",height)
print("; Frame Per Second: ", framePerSecond)

# WINDOWS -- *'DIVX'; MACOS -- *'XVID'
writer=cv2.VideoWriter('../DATA/myVideo.mp4', cv2.VideoWriter_fourcc(*'DIVX'),framePerSecond,(width,height)) #cv2.VideoWriter('imeFila.mp3',cv2.VideoWriter_fourcc(*'odvisnoOdOP'),frame/sec,(widht,height))

while True:

    ret, frame= cap.read()

    writer.write(frame)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()