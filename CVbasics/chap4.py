#image into black and white image
import cv2 as cv

img = cv.imread("resources/img1.jpeg")
img = cv.resize(img,(400,300))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# O  & 1 are binary
(thresh, binary) = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
cv.imshow("original image", img)
cv.imshow("gray", gray)
cv.imshow("Black and white", binary)
cv.waitKey(0)
cv.destroyWindow()