# https://www.youtube.com/watch?v=NyLF8nHIquM&t=87s

from Tools import prtScr
from Tools import assembleVideo
import time

cnt: int = 0
FolderName: str = 'Images'

while 1:
    cnt = cnt+1
    cntStr = str(cnt)
    imgFullName = FolderName+'/Img_'+cntStr+'.png'
    print(cnt)
    prtScr(imgFullName)
    # time.sleep(0.7)

    if cnt % 30 == 0:
        assembleVideo(FolderName)
        break
