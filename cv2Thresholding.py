#!/usr/local/bin/python3

# brew install opencv3 --with-contrib --with-python3
#
# his formula is keg-only, which means it was not symlinked into /usr/local.
#
# opencv3 and opencv install many of the same files.
#
# If you need to have this software first in your PATH run:
# echo 'export PATH="/usr/local/opt/opencv3/bin:$PATH"' >> ~/.bash_profile
#
# For compilers to find this software you may need to set:
# LDFLAGS:  -L/usr/local/opt/opencv3/lib
# CPPFLAGS: -I/usr/local/opt/opencv3/include
# For pkg-config to find this software you may need to set:
# PKG_CONFIG_PATH: /usr/local/opt/opencv3/lib/pkgconfig
#
#
# If you need Python to find bindings for this keg-only formula, run:
#     echo /usr/local/opt/opencv3/lib/python3.5/site-packages >> /usr/local/lib/python3.5/site-packages/opencv3.pth
#     mkdir -p /Users/flg/.local/lib/python3.5/site-packages
#     echo 'import site; site.addsitedir("/usr/local/lib/python3.5/site-packages")' >> /Users/flg/.local/lib/python3.5/site-packages/homebrew.pth


import cv2
import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
from matplotlib import pyplot as plt


# Thresholding
# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html#thresholding

# simple Thresholding

img = cv2.imread('nonuniform-picture.png',0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)


# adaptive Thresholding

img2 = cv2.medianBlur(img,5)

ret,th1 = cv2.threshold(img2,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img2,255,cv2.ADAPTIVE_THRESH_MEAN_C, \
                            cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                            cv2.THRESH_BINARY,11,2)


# Otsu's thresholding
ret2,oth1 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,oth2 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV', 'Global Thresholding (v = 127)',
          'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding',"Otsu's Thresholding","Otsu's Thresholding (Gaussian)"]
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5, th1, th2, th3, oth1, oth2]

for i in range(11):
    plt.subplot(4,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
