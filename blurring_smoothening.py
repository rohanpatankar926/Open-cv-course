import cv2 as cv

image =cv.imread("image.jpg")
cv.imshow("Original",image)

#averaging the image
average=cv.blur(image,(7,7))
cv.imshow("Average",average)
cv.waitKey(0)

#Gaussian Blur
gb=cv.GaussianBlur(image,(7,7),0)
cv.imshow("Gaussian Blur",gb)
cv.waitKey(0)

#Median blur
mb=cv.medianBlur(image,7)
cv.imshow("Median Blur",mb)
cv.imshow("Median Blur",mb)
#medium same thing as avg but faster it find medium of the medium it is the best technique compared to avg and gaussian blur.
cv.waitKey(0)

#Bilateral Blur
bl=cv.bilateralFilter(image,7,45,45)
#applies blurring it detrain the edges in the image
cv.imshow("Bilateral Blur",bl)
cv.waitKey(0)