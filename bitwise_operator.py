import cv2 as cv
import numpy as np

blank=np.zeros((512,512),np.uint8)
rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),(255),-1)

circle=cv.circle(blank.copy(),(200,200),100,(255,255,255),-1)

cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)

#bitwise_and-->intersecting regions
bitwise_and=cv.bitwise_and(rectangle,circle)
cv.imshow('Bitwise_and',bitwise_and)
cv.waitKey(0)
#takes the bitwise_and of the rectangle and circle and displays it in the window named bitwise_and 

#bitwise_or-->non intersecting regions and intersection of the two regions
bitwise_or=cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwise_or',bitwise_or)
cv.waitKey(0)
#takes the union of the two images and shows the result in the window named bitwise_or 

#bitwise_xor
bitwise_xor=cv.bitwise_xor(rectangle,circle)
cv.imshow('Bitwise_xor',bitwise_xor)
cv.waitKey(0)

#biwise_not
bitwise_not=cv.bitwise_not(rectangle)
cv.imshow('Bitwise_not',bitwise_not)
cv.waitkey(0)
