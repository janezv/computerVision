import cv2

def ask_for_tracker():
    print("What Tracker API would you like to use?")
    print("0: ")
    print("1: ")
    print("2: ")
    print("3: ")
    choice = input("Please select your tracker:")

    if choice == '0':
        tracker = cv2.TrackerMIL_create()
    if choice == '1':
        tracker = cv2.TrackerKCF_create()
    if choice == '2':
        tracker = cv2.TrackerCSRT_create()
    if choice == '3':
        tracker = cv2.TrackerKCF_create()

    return tracker

tracker = ask_for_tracker()
str(tracker).split()[0][1:]

cap=cv2.VideoCapture(0)
ret, frame=cap.read()

# draw frame on image that will be our desired ROI
roi=cv2.selectROI(frame,False)

ret=tracker.init(frame, roi)

while True:
    ret, frame = cap.read()

    success, roi=tracker.update(frame)

    (x,y,w,h)=tuple(map(int,roi))

    if success:
        p1=(x,y)
        p2=(x+w,y+h)
        cv2.rectangle(frame, p1,p2,(0,255,0),3)
    else:
        cv2.putText(frame,"napaka", (200,400),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,2,(0,0,255),7)

    cv2.imshow("frame",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()








