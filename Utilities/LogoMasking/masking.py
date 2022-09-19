
import string
import cv2
import numpy as np
#import matplotlib.pyplot as plt


class MaskingLogo:
    imagePath: string
    logoPath: string

    # initi with default images
    def __init__(self, image: string = 'dog_backpack.png', logo: string = 'watermark_no_copy.png') -> None:
        self.imagePath, self.logoPath = image, logo

    def resizeSmall(self, imgLarge, imgSmall):
        # plt.imshow(imgLarge)
        # plt.show()
        img = imgSmall
        if not ((imgLarge.shape[0] > imgSmall.shape[0]) and (imgLarge.shape[1] > imgSmall.shape[1])):
            while not ((imgLarge.shape[0] > imgSmall.shape[0]) and (imgLarge.shape[1] > imgSmall.shape[1])):
                nsize = [int(imgSmall.shape[0]*0.4),
                         int(imgSmall.shape[1]*0.4)]
                imgSmall = cv2.resize(imgSmall, dsize=nsize)
            img = imgSmall
        return img

    def maskSmall(self, img):
        img2gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        #cv2.imshow('img2gray', img2gray)
        mask_inv = cv2.bitwise_not(img2gray)
        #cv2.imshow('mask_inv', mask_inv)
        fg = cv2.bitwise_or(img, img, mask=mask_inv)
        #cv2.imshow('fg', fg)
        return fg

    def logoRegionOfInterest(self, imgLarge, imgSmall):
        # plt.imshow(imgLarge)
        # plt.show()
        #cv2.imshow('imgSmall', imgSmall)
        # Region of interest naj bo zgornji desni kot
        roi = imgLarge[0:imgSmall.shape[0],
                       imgLarge.shape[1]-imgSmall.shape[1]:imgLarge.shape[1]]
        #cv2.imshow('roi', roi)
        final_rio = cv2.bitwise_or(roi, imgSmall)
        #cv2.imshow('final_rio', final_rio)
        imgLarge[0:imgSmall.shape[0],
                 imgLarge.shape[1]-imgSmall.shape[1]:imgLarge.shape[1]] = final_rio
        return imgLarge

    def savePicture(self, image):
        pathArray = self.imagePath.split(".")
        newPathArray = pathArray[:-1]
        # conver Array to string
        newPathString = ""
        for ele in newPathArray:
            newPathString += ele
        newPathString = newPathString + "WithLogo.png"
        cv2.imwrite(newPathString, image)
        print(newPathString)

    def mainProgram(self):
        mainImage = cv2.imread(self.imagePath)
        logo = cv2.imread(self.logoPath)
        #cv2.imshow('logo', logo)
        logo = self.resizeSmall(mainImage, logo)
        #cv2.imshow('logo', logo)
        logo = self.maskSmall(logo)
        #cv2.imshow('logo', logo)
        mainImage = self.logoRegionOfInterest(mainImage, logo)
        self.savePicture(image=mainImage)

#        cv2.waitKey()
