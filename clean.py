#!/usr/local/bin/python3

import numpy as np
from scipy import misc, ndimage
import matplotlib.pyplot as plt

im = misc.imread('in.png', flatten=True)
# sx = ndimage.sobel(im, axis=0, mode='constant')
# sy = ndimage.sobel(im, axis=1, mode='constant')
# sob = np.hypot(sx, sy)

# im = np.zeros((256, 256))
# im[64:-64, 64:-64] = 1

sx = ndimage.sobel(im, axis=0, mode='constant')
sy = ndimage.sobel(im, axis=1, mode='constant')
sob = np.hypot(sx, sy)

plt.imshow(sob)
plt.show()
