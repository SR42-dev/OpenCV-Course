# Shapes & text

import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8) # 0 denotes black, 3 denotes third dimension matrix
print(img.shape) # shape returns height, width and channels
print(img)
img[200:300, 100:300] = 255, 0, 0 # assigns colour blue to specific range of pixels in 2D (here, a rectangle)

# cv2.line(img,(0,0), (300,300), (0, 255, 255), 3) # base image, start point, end point, color code, thickness
cv2.line(img,(0,0), (img.shape[1],img.shape[0]), (0, 255, 255), 3)

cv2.rectangle(img, (0,0), (450,450), (0,0,255), 2) # image, diagonal start, diagonal end, color, thickness
cv2.rectangle(img, (0,0), (250,250), (0,0,255), cv2.FILLED) # cv2.FILLED fills color of boundary in defined rectangle

cv2.circle(img, (450,50), 30, (255,255,0), 5) # base image, centre coordinates, color, thickness
cv2.circle(img, (450,200), 30, (255,255,0), cv2.FILLED) # base image, centre coordinates, color, fill status

cv2.putText(img, "OpenCV", (300,200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1) # base image, text, origin coordinates, font, scale(size, decimals allowed), color, thickness
cv2.putText(img, "OpenCV", (300,300), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 150, 0), 1)
cv2.putText(img, "OpenCV", (300,400), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 5)

cv2.imshow("Image", img)

cv2.waitKey(0)