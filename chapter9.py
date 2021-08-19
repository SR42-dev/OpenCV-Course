# Face detection
'''
Notes :
    - Viola and Jones method
    - Positive & negative faces to train cascade
    - xml file holds cascades
    - cv2 has cascades in built, custom ones can be created as well
'''

import cv2

faceCascade = cv2.CascadeClassifier('resources/haarcascade_frontalface_default.xml') # imports cascade file from resources directory if it exists

img = cv2.imread('resources/lena.jpg')

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # grayscaling original image

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4) # image, scale factor, minimum neighbours

for (x, y, w, h) in faces :

    cv2.rectangle(img, (x,y), (x + w, y + h), (255, 0, 0), 2) # bounding box for detected face
    cv2.rectangle(imgGray, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow('Original w/ bounding box', img)
cv2.imshow('Result', imgGray)
cv2.waitKey(0)
