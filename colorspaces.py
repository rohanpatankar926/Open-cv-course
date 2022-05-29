import cv2

image=cv2.imread("image.jpg")
cv2.imshow("Original",image)

# Converying to grayscale
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray",gray)

resized=cv2.resize(gray,(10000,10000))
# cv2.imshow("Resized",resized)
cv2.waitKey(0)

# BGR to HSV
hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV",hsv)
cv2.waitKey(0)

#bgr to rgb
rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
cv2.imshow("RGB",rgb)
cv2.waitKey(0)

#reversing a color
#hsv to bgr
hsv_bgr=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
cv2.imshow("HSV to BGR",hsv_bgr)
cv2.waitKey(0)

lab_bgr=cv2.cvtColor(hsv,cv2.COLOR_LAB2BGR)
cv2.imshow("LAB to BGR",lab_bgr)
cv2.waitKey(0)