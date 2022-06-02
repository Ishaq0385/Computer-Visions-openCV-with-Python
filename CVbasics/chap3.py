import cv2 as cv

#converting into grayscale image
img = cv.imread("resources/img1.jpeg")
img = cv.resize(img,(800,600))


gray_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("first image", img)
cv.imshow("grsy  image", gray_img)
cv.waitKey(0)
cv.destroyWindow()



