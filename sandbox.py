#!/usr/local/bin/python3

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('in.png', cv2.IMREAD_GRAYSCALE)
# img = cv2.medianBlur(img, 3)
# img = cv2.Laplacian(img, cv2.CV_64F)
# res, img = cv2.threshold(img,20,255,cv2.THRESH_BINARY)
img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,20)
plt.imshow(img)
plt.show()
