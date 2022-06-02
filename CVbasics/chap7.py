#convert into gray scale video
#reading a video
import cv2 as cv

cap = cv.VideoCapture('resources/video.mp4')

while(True):
    ret, frame = cap.read()
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #(thresh, binary) = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
    if ret == True:
        cv.imshow("video", grayframe)
        #to quit with q key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()
