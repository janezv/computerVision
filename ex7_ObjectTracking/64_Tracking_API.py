import cv2

# Global variables
xs= -1
ys = -1
xe=-1
ye=-1
drawing = False
rioSet=False


tracker = cv2.TrackerCSRT_create()

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
        tracker = cv2.legacy_TrackerMOSSE()
    

video = cv2.VideoCapture(1)
b, img = video.read()


def draw_rectangle(event, x, y, flags, params):
    global xs, ys, xe, ye, drawing, img
    global rioSet
      
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        xs = x
        ys = y     
              
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            xe=x
            ye=y
        return   
      
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        rioSet=True
        return 

cv2.namedWindow(winname = "Title of Popup Window")
cv2.setMouseCallback('Title of Popup Window', draw_rectangle)
while True:
    b, img = video.read()
    if drawing:
        cv2.rectangle(img, pt1 =(xs, ys), pt2 =(xe, ye),
                color =(0, 0, 255),
                thickness =3)
    cv2.imshow('Title of Popup Window',img)
    if cv2.waitKey(10)==ord('q') or rioSet==True:
        break

print("******* Konec ***** ")
rioImg=img[ys:ye, xs:xe]
cv2.imshow('rio',rioImg)
cv2.waitKey()
