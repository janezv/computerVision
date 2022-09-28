import cv2
import numpy as np
import matplotlib.pyplot as plt


def resizeSmall(imgLarge, imgSmall):
    img = imgSmall
    if not ((imgLarge.shape[0] > imgSmall.shape[0]) and (imgLarge.shape[1] > imgSmall.shape[1])):
        while not ((imgLarge.shape[0] > imgSmall.shape[0]) and (imgLarge.shape[1] > imgSmall.shape[1])):
            nsize = [int(imgSmall.shape[0]*0.4), int(imgSmall.shape[1]*0.4)]
            imgSmall = cv2.resize(imgSmall, dsize=nsize)
        img = imgSmall
    return img


def maskSmall(img):
    img2gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cv2.imshow('img2gray', img2gray)
    mask_inv = cv2.bitwise_not(img2gray)
    cv2.imshow('mask_inv', mask_inv)
    fg = cv2.bitwise_or(img, img, mask=mask_inv)
    cv2.imshow('fg', fg)
    return fg


def logoRegionOfInterest(imgLarge, imgSmall):
    #cv2.imshow('imgLarge', imgLarge)
    #cv2.imshow('imgSmall', imgSmall)
    # Region of interest naj bo zgornji desni kot
    roi = imgLarge[0:imgSmall.shape[0],
                   imgLarge.shape[1]-imgSmall.shape[1]:imgLarge.shape[1]]
    cv2.imshow('roi', roi)
    final_rio = cv2.bitwise_or(roi, imgSmall)
    cv2.imshow('final_rio', final_rio)
    imgLarge[0:imgSmall.shape[0],
             imgLarge.shape[1]-imgSmall.shape[1]:imgLarge.shape[1]] = final_rio
    return imgLarge


img1 = cv2.imread("..\data\dog_backpack.jpg")
img2 = cv2.imread("../data/watermark_no_copy.png")


img2resized = resizeSmall(img1, img2)

img2log = maskSmall(img2resized)
outImg = logoRegionOfInterest(img1, img2log)
cv2.imshow('outImg', outImg)

cv2.waitKey(0)
