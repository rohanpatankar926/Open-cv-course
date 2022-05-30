import cv2 as cv
import matplotlib.pyplot as plt
image=cv.imread("image.jpg")
cv.imshow("Original",image)

gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
# cv.imshow("Gray",gray)

#grayscale histogram
gray_hist=cv.calcHist([gray],[0],None,[256],[0,256])
plt.title("Gray Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
# plt.plot(gray_hist)
plt.xlim([0,256])

#Color Histogram
plt.title("Gray Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
color=("b","g","r")
for i,col in enumerate(color):
    hist=cv.calcHist([image],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])

plt.show()
