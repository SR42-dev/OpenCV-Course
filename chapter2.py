# Basic functions

import cv2
import numpy as np # here, for matrix manipulation

'''
# converting an image to greyscale

img = cv2.imread('resources/The Sci-Fi Archive.jpg')

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # <image variable>, <conversion method>
cv2.imshow('Greyscale Image', imgGray)
cv2.waitKey(0)
'''
'''
# converting an image to blurred greyscale

img = cv2.imread('resources/CaptureDP.png')

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgGrayBlur = cv2.GaussianBlur(imgGray, (7,7), 0) # <image variable>, <kernal size (odd square)>, <sigma x>
cv2.imshow('Blurred Greyscale Image', imgGray)
cv2.imshow('Greyscale Image', imgGray)
cv2.waitKey(0)
'''
'''
# Edge detection

img = cv2.imread('resources/CaptureDP.png')

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgGrayBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv2.Canny(img, 100, 100) # <image variable>, <threshold value(s)>

cv2.imshow('Blurred Greyscale Image', imgGray)
cv2.imshow('Greyscale Image', imgGray)
cv2.imshow('Canny Image', imgCanny) # edges highlighted

cv2.waitKey(0)
'''
'''
# Image dialation - Increasing thickness of edges to make up for faded boundaries not picked up by canny

img = cv2.imread('resources/CaptureDP.png')
kernel = np.ones((5,5), np.uint8) # 5x5 matrix of ones of type unsigned 8 bit integers

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgGrayBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv2.Canny(img, 100, 100)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1) # <Canny image variable>, <kernel (matrix)>, iterations = <thickness>

cv2.imshow('Blurred Greyscale Image', imgGray)
cv2.imshow('Greyscale Image', imgGray)
cv2.imshow('Canny Image', imgCanny)
cv2.imshow('Dilated Canny Image', imgDilation)

cv2.waitKey(0)
'''
'''
# Image erosion - Decreasing thickness of edges of a dilated image

img = cv2.imread('resources/CaptureDP.png')
kernel = np.ones((5,5), np.uint8) # 5x5 matrix of ones of type unsigned 8 bit integers

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgGrayBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv2.Canny(img, 100, 100)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDilation, kernel, iterations=1) # similar parameters to dilate()

cv2.imshow('Blurred Greyscale Image', imgGray)
cv2.imshow('Greyscale Image', imgGray)
cv2.imshow('Canny Image', imgCanny)
cv2.imshow('Dilated Canny Image', imgDilation)
cv2.imshow('Eroded Canny Image', imgEroded) 

cv2.waitKey(0)
'''