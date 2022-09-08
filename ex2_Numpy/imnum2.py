import imp


import cv2
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

pic = Image.open('../DATA/00-puppy.jpg')
pic.show()
print(type(pic))
