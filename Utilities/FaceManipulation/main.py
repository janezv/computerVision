import Util.imgManipulation as Manipulation
import cv2

video=cv2.VideoCapture(1)


while 1:
    b, img=video.read()
    
    face_cascade = cv2.CascadeClassifier('Util/DATA/haarcascades/haarcascade_frontalface_default.xml')
    #face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    imgManipulation=Manipulation.manipulation()
    imgL = imgManipulation.enlargeImg(img)

    def detect_face(img):
        face_img=img.copy()

        face_rects=face_cascade.detectMultiScale(face_img, scaleFactor=1.5, minNeighbors=3)

        for (x,y,w,h) in face_rects:
            dimension=(x,y,w,h)
            face_img = imgManipulation.manipulateImg(face_img, dimension)
            
        
        return face_img

    result = detect_face(imgL)

    def displayImg(img):
        # cv2.namedWindow('Img',cv2.WND_PROP_FULLSCREEN) 
        # cv2.setWindowProperty("Img", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN) 
        cv2.imshow('Img',img)
    displayImg(result)

    if cv2.waitKey(1)& 0xFF == ord('q'):
        break