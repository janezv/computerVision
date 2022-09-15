from math import sqrt
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

drawing = False
ix, iy = -1, -1


def draw_cicrle(event, x, y, flags, params):

    global ix, iy, drawing

    if event == cv2.EVENT_RBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            r = int(sqrt((x-ix)**2+(y-iy)))
            print(r)
            cv2.circle(img, (ix, iy), r, (255, 0, 0))

    elif event == cv2.EVENT_RBUTTONUP:
        drawing = False
        r = int(sqrt((x-ix)**2+(y-iy)))
        cv2.circle(img, (ix, iy), r, (255, 0, 0))


cv2.namedWindow('my_wind')
cv2.setMouseCallback('my_wind', draw_cicrle)

img = cv2.imread("dog_backpack.jpg")
#cv2.circle(img, (100, 100), 30, (255, 0, 0))


while True:
    cv2.imshow('my_wind', img)

    if cv2.waitKey(500) & 0xFF == 27:
        break
