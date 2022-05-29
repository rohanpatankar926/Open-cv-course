import cv2 as cv
import numpy as np

image=cv.imread("image.jpg")
cv.imshow("Original",image)

b,g,r=cv.split(image)
cv.imshow("Blue",b)
cv.imshow("Green",g)
cv.imshow("Red",r)
cv.waitKey(0)

blank_img=np.zeros(image.shape[:2],dtype=np.uint8)

blue=cv.merge([b,blank_img,blank_img])
green=cv.merge([blank_img,g,blank_img])
red=cv.merge([blank_img,blank_img,r])
cv.waitKey(0)

def new_func(image, b, g, r):
    print(image.shape)
    print(r.shape)
    print(g.shape)
    print(b.shape)
new_func(image, b, g, r)


def new_func1(b, g, r):
    merged=cv.merge([r,g,b])
    return merged
cv.imshow("Merged",new_func1(b, g, r))
cv.waitKey(0)
