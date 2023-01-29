import cv2
from RecordVideo import Record
from datetime import datetime

cap=cv2.VideoCapture(1)

face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
#body_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_upperbody.xml") zaznava telesa ne dela dobro

detection=False
record_toggling=False
# start_time, za namen štoparice --> meri 6 s od izginotja obraza
start_time=datetime.now()


record = Record(int(cap.get(3)), int(cap.get(4)))  # podaj širino in višino iz kamere


while True:
    _, frame=cap.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.5,5)

    
    if not detection:
        pass
 
    for (x,y,width, height) in faces:
        cv2.rectangle(frame,(x,y),(x+width, y + height),(255,0,0),3)

    if len(faces) and not record_toggling:
        record.startRecording()
        record_toggling=True
        start_time=datetime.now()
    elif not len(faces) and record_toggling==True: # počakaj 6 s, če res ni zaznan obraz ugasni
        delta=datetime.now()-start_time
        print(delta.total_seconds()) 
        if delta.total_seconds() > 6:
             record_toggling=False
             record.saveRecording() # zaključi s snemanjem in shrani datoteko
    else:
        start_time=datetime.now()  # to bo zagotovilo reset štoparice, če se obraz pojavi nazaj pred 6s

    
    if record_toggling:
        record.recording(frame)
 

    cv2.imshow("Camera", frame)
    if cv2.waitKey(1)==ord('q'):
        break


cap.release()
cv2.destroyAllWindows()