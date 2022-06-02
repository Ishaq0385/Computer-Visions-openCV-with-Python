#writing images



import cv2 as cv
from cv2 import imwrite

img = cv.imread("resources/img1.jpeg")
img = cv.resize(img,(400,300))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imwrite('resources/image_gray.png', gray)

cv.waitKey(0)
cv.destroyWindow()