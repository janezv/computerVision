
import re
import cv2
import numpy as np
import matplotlib.pyplot as plt

flat_chess=cv2.imread('DATA/flat_chessboard.png')
flat_chess=cv2.cvtColor(flat_chess,cv2.COLOR_BGR2RGB)

plt.subplot(321)
plt.imshow(flat_chess)

gray_flat_chess=cv2.cvtColor(flat_chess,cv2.COLOR_BGR2GRAY)

plt.subplot(322)
plt.imshow(gray_flat_chess,cmap='gray')


real_chess=cv2.imread('DATA/real_chessboard.jpg')
real_chess=cv2.cvtColor(real_chess,cv2.COLOR_BGR2RGB)
plt.subplot(323)
plt.imshow(real_chess)


gray_real_chess=cv2.cvtColor(real_chess,cv2.COLOR_BGR2GRAY)
plt.subplot(324)
plt.imshow(gray_real_chess,cmap="gray")
plt.show(block=False)
plt.pause(1.5)

## Harris Corner detection
gray=np.float32(gray_flat_chess)
dst=cv2.cornerHarris(src=gray,blockSize=2,ksize=3,k=0.04)

dst=cv2.dilate(dst,None)
#kjerkoli je vrednost več kot procent max() Harris obdelave naj bo rdeče
flat_chess[dst>0.01*dst.max()]=[255,0,0]
plt.subplot(325)
plt.imshow(flat_chess)


gray=np.float32(gray_real_chess)
dst=cv2.cornerHarris(src=gray,blockSize=2,ksize=3,k=0.04)
dst=cv2.dilate(dst,None)
#kjerkoli je vrednost več kot procent max() Harris obdelave naj bo rdeče
real_chess[dst>0.01*dst.max()]=[255,0,0]
plt.subplot(326)
plt.imshow(real_chess)

# Make it full Screen
wm = plt.get_current_fig_manager()
wm.window.state('zoomed')

plt.show(block=False)
plt.pause(4)
print("Konec")
