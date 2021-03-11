import cv2 as cv

dog = cv.VideoCapture(0)

while True:
    success, video = dog.read()
    cv.imshow("Doggy", video)
    if cv.waitKey(1) and 0xFF == ord('q'):
        break
