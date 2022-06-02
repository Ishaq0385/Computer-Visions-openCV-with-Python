# This repository includes computer vision openCV in python Starting from basics
## Import opencv:

import cv2 as cv

## 1- chap1.py & chap2.py:
### Reading and displaying an image in a window and Also resizing a window
* **code:** <br/>
import cv2 as cv <br/>
#resizing the image<br/>
img = cv.imread("resources/img1.jpeg")<br/>
img1 = cv.resize(img,(400,300))<br/>
cv.imshow("first image", img)<br/>
cv.imshow("first image", img1)<br/>
cv.waitKey(0)<br/>
cv.destroyWindow()*


## 3- Chap3.py:

### Converting image into gray scale

* **code:** <br/>
 gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)*

![c1](https://user-images.githubusercontent.com/99035981/171577874-bd8bece0-56b5-4040-be65-86b65c3127f9.PNG)


## 4- chap4.py:
### converting image into black and white image
* **code:** <br/>
import cv2 as cv <br/>
#resizing the image<br/>
img = cv.imread("resources/img1.jpeg")<br/>
img1 = cv.resize(img,(400,300))<br/>
cv.imshow("first image", img)<br/>
cv.imshow("first image", img1)<br/>
cv.waitKey(0)<br/>
cv.destroyWindow()* 

![c2](https://user-images.githubusercontent.com/99035981/171580630-51480125-4388-45ab-8c08-75c2a0b91b6b.PNG)

## 5- chap5.py:
### writing an image/ storing and image into a folder
* **code:** <br/>
import cv2 as cv<br/>
from cv2 import imwrite<br/>
img = cv.imread("resources/img1.jpeg")<br/>
img = cv.resize(img,(400,300))<br/>
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)<br/>
imwrite('resources/image_gray.png', gray)<br/>
cv.waitKey(0)<br/>
cv.destroyWindow()*

![c3](https://user-images.githubusercontent.com/99035981/171581723-c6c817e6-2af9-4c02-b31f-5c8dbfca65a2.PNG)

## 6- chap6.py:
### reading video from a folder and display in window
* **code:** <br/>
import cv2 as cv<br/>
cap = cv.VideoCapture('resources/video.mp4')<br/><br/><br/>
**#indicator(are we reading video or not)**<br/>
if (cap.isOpened() == False):<br/>
    print("ERROR IN READING VIDEO")<br/>
**#reading and playing video**<br/>
while(cap.isOpened()):<br/>
    ret,frame = cap.read()<br/>
    if ret == True:<br/>
        cv.imshow("video", frame)<br/>
        **#quiting form window by pressing 'q'** <br/>
        if cv.waitKey(1) & 0xFF == ord('q'):<br/>
            break<br/>
    else:<br/>
        break<br/>
cap.release()<br/>
cv.destroyAllWindows()* 

## 7- chap7.py:
### Converting video into gray scale
* **code:** <br/>
import cv2 as cv<br/>
cap = cv.VideoCapture('resources/video.mp4')<br/>
while(True):<br/>
    ret, frame = cap.read()<br/>
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)<br/>
    #(thresh, binary) = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)<br/>
    if ret == True:<br/>
        cv.imshow("video", grayframe)<br/>
         **#quiting form window by pressing 'q'** <br/>
        if cv.waitKey(1) & 0xFF == ord('q'):<br/>
            break<br/>
    else:<br/>
        break<br/>
cap.release()<br/>
cv.destroyAllWindows()*

