import cv2 as cv

park = cv.imread("./Photos/park.jpg")

gray = cv.cvtColor(park, cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(park, (7,7),0)

cv.imshow("gray park", gray)
cv.imshow("normal park", park)
cv.imshow("blur park", blur)

cv.waitKey(0)

# ctrl + alt + down arrow
# cmd + opt + down arrow 