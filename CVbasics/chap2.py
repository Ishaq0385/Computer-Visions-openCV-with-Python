import cv2 as cv

#resizing the image
img = cv.imread("resources/img1.jpeg")
img1 = cv.resize(img,(800,600))
cv.imshow("first image", img)
cv.imshow("first image", img1)
cv.waitKey(0)
cv.destroyWindow()



