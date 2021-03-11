import cv2 as cv

cats = cv.imread("./Photos/cats 2.jpg")

print(cats.shape)

resize = cv.resize(cats,(300,550))

crop = cats[0:200, 150:300]

cv.imshow("resized window", resize)
cv.imshow("normal window", cats)
cv.imshow("cropped window", crop)

cv.waitKey(0)