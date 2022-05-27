import cv2 
image=cv.imread('4ca727e8cbb9d1c97b3abfe932313a1b.jpg')
cv2.imshow('Original',image)
cv2.waitKey(0)

#reading vidcam using videocamera
# define a video capture object
vid = cv2.VideoCapture(0)
while(True):
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    # Display the resulting frame
    cv2.imshow('frame', frame)
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# After the loop release the cap object
# vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

#reading images from a folder
vid=cv2.VideoCapture("/home/pi/Desktop/images")

while(True):
    ret,fram=vid.read()
    cv2.imshow("Video",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()

