import cv2 as cv

dog = cv.VideoCapture("./Videos/dog.mp4")

while True:
    success, video = dog.read()
    cv.imshow("Doggy", video)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

# release the capturing device
capture.release()
# close the window
cv.destroyAllWindows()