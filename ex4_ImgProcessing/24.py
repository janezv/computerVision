import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('DATA/dog_backpack.png')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread('DATA/watermark_no_copy.png')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

img2 = cv2.resize(img2, (300, 300))
plt.imshow(img2)
plt.show()

start_y = img1.shape[0]-img2.shape[0]
start_x = img1.shape[1]-img2.shape[1]

print("start_y: ", start_y)
print("y: ", img1.shape[0])
print("start_x: ", start_x)
print("x: ", img1.shape[1])

img1[start_y:img1.shape[0],
     start_x:img1.shape[1]] = img2
plt.imshow(img1)
plt.show()
cv2.waitKey(1000)
