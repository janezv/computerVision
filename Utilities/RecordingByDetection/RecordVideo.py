import cv2
from datetime import datetime

class Record:

    # x y so višina širina slike iz kamere
    def __init__(self, x, y) -> None:
        self.frame_size=(x,y)
        self.fourcc=cv2.VideoWriter_fourcc(*"mp4v") ## to je enako--> cv2.VideoWriter_fourcc("m","p","4","v")
        self.Video_Name="Null"
        #self.out=cv2.VideoWriter("Video.mp4", fourcc, 20, frame_size)
        pass

    def startRecording(self):
        current_time = datetime.now()
        # Sestavi ime iz časa, ko se začne 
        self.Video_Name="Video_" + str(current_time.hour) + "_" + str(current_time.minute) + "_" + str(current_time.second) +".mp4"
        self.out=cv2.VideoWriter(self.Video_Name, self.fourcc, 20, self.frame_size)

    def recording(self, frame):
        self.out.write(frame)

    def saveRecording(self):
        self.out.release()
