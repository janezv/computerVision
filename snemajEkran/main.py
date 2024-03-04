# https://www.youtube.com/watch?v=NyLF8nHIquM&t=87s

from Tools import prtScr
from Tools import assembleVideo
import time

print("Vpiši število Slik")
numberOfFrames = input()
numberOfFrames = int(numberOfFrames)
print("Vpiši št Slik / Sekundo v vidu (cca 0.5 -7)")
print("Najboljši rezultat je 7.25 F/s")
FramesPerSecodn = input()
FramesPerSecodn = float(FramesPerSecodn)
cnt: int = 0
FolderName: str = 'Images'

while 1:
    cnt = cnt+1
    cntStr = str(cnt)
    imgFullName = FolderName+'/Img_'+cntStr+'.png'
    print(cnt)
    prtScr(imgFullName)
    # time.sleep(0.7)

    if cnt % numberOfFrames == 0:
        assembleVideo(FolderName, FramesPerSecodn)
        break
