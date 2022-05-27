import cv2 as cv
import numpy as np

img = cv.imread('hanuman.jpg')
cv.imshow('Hanuman', img)

# Translation
class Transformation:
    def __init__(self):
        pass
    
    def translate(self,img, x, y):
        self.transMat = np.float32([[1,0,x],[0,1,y]])
        self.dimensions = (img.shape[1], img.shape[0])
        return cv.warpAffine(img, self.transMat, self.dimensions)
    
    # Rotation
    def rotate(self,img, angle, rotPoint=None):
        (self.height,self.width) = img.shape[:2]

        if rotPoint is None:
            self.rotPoint = (self.width//2,self.height//2)
        
        self.rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
        self.dimensions = (self.width,self.height)

        return cv.warpAffine(img, self.rotMat, self.dimensions)


# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = Transformation().translate(img, -100, 100)
cv.imshow('Translated', translated)


rotated = Transformation().rotate(img, -45)
cv.imshow('Rotated', rotated)

rotated_rotated = Transformation().rotate(img, -90)
cv.imshow('Rotated Rotated', rotated_rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)