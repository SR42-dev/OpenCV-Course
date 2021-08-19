# Joining images

import cv2
import numpy as np

'''
img = cv2.imread('resources/CaptureDP.PNG')
imgHor = np.hstack((img, img)) # 2 images with same number of channels (RGB, HSV, etc)
imgVer = np.vstack((img, img)) # Creates 2D array with vertical stacking
cv2.imshow('Horizontal', imgHor)
cv2.imshow('Vertical', imgVer)
cv2.waitKey(0)
'''