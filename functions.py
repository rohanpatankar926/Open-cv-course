import cv2

image=cv2.imread("hanuman.jpg")
cv2.imshow("Original",image)

#Converying to grayscale
gray_scale=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray_scale)
cv2.waitKey(0)

#blurring an image
blur=cv2.GaussianBlur(image,(9,9),cv2.BORDER_DEFAULT)#window size)
cv2.imshow("Blur",blur)
cv2.waitKey(0)

#Edge cascade
edge=cv2.Canny(image,100,200)
cv2.imshow("Edge",edge)
cv2.waitKey(0)

#Dialated of image
dilate=cv2.dilate(edge,None,iterations=1)
cv2.imshow("dialated",dilate)

#eroding
erode=cv2.erode(dilate,None,iterations=1)
cv2.imshow("Eroded",erode)
cv2.waitKey(0)

#resize
resized=cv2.resize(image,(300,300))
cv2.imshow("Resized",resized)
cv2.waitKey(0)

#cropping
cropped=image[120:500,0:200]
cv2.imshow("Cropped",cropped)
cv2.waitKey(0)