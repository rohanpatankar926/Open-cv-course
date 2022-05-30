import cv2 as cv

image=cv.imread("sunny.jpg")
cv.imshow("Original",image)

gray_img=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray_img)

haar_cascade=cv.CascadeClassifier("haarcascade_frontalface.xml")

faces_rect=haar_cascade.detectMultiScale(gray_img,scaleFactor=1.1,minNeighbors=3)

for (x,y,z,w) in faces_rect:
    cv.rectangle(image,(x,y),(x+z,y+w),(0,255,0),2)



cv.waitKey(0)
