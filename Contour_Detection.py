import cv2 
import numpy as np
image=cv2.imread("hanuman.jpg")
# cv2.imshow("Hanuman",image)

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray",gray)

blur=cv2.GaussianBlur(gray,(5,5),0)

canny=cv2.Canny(image,100,200)
# cv2.imshow("Canny",canny)


ret,thresh=cv2.threshold(gray,127,255,0)
cv2.imshow("Threshold",thresh)

contours,heirarchies=cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
print(len(contours))

zeros=np.zeros(image.shape,dtype="uint8")

cv2.drawContours(zeros,contours,-1,(0,0,255),1)
cv2.imshow("Contours",zeros)
cv2.waitKey(0)