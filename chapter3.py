# Resizing & cropping
import cv2

'''
# Resizing

img = cv2.imread('resources/CaptureDP.png')
print(img.shape) # prints height, width, channels (3 means B, G & R)

imgResize = cv2.resize(img, (100, 100)) # (<width>,<height>)
print(imgResize.shape)

cv2.imshow("Image", img)
cv2.imshow("ResizedImage", imgResize)

cv2.waitKey(0)
'''

'''
# Resizing
# Image - matrix of pixels aka 2D array

img = cv2.imread('resources/CaptureDP.png')
print(img.shape)

imgResize = cv2.resize(img, (200, 200))
print(imgResize.shape)

imgCropped = img[0:200, 200:500] # height first, then width

cv2.imshow("Image", img)
cv2.imshow("Resized Image", imgResize)
cv2.imshow("Cropped Image", imgCropped)

cv2.waitKey(0)
'''


