import cv2

image = cv2.imread("hanuman.jpg")


class Scale:
    def __init__(self):
        self.scale = 0.1

    def rescale_Frame(self, frame):
        #this fncth for existing image and video
        self.width = int(frame.shape[1]*self.scale)
        self.height = int(frame.shape[0]*self.scale)
        self.dimension = (self.width, self.height)
        return cv2.resize(frame, self.dimension, interpolation=cv2.INTER_AREA)

    def changeRes(self, width, height):
        #this fncth for live video
        self.capture.set(3, width)
        self.capture.set(4, height)


resized_image = Scale().rescale_Frame(image)
cv2.imshow("Original", resized_image)
capture = cv2.VideoCapture(0)

while (1):
    ret, frame = image.read()
    frame = Scale().rescale_Frame(frame)
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
