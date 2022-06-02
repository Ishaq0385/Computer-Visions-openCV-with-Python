#reading a video
import cv2 as cv

cap = cv.VideoCapture('resources/video.mp4')

#indicator
if (cap.isOpened() == False):
    print("ERROR IN READING VIDEO")
#reading and playing video

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        cv.imshow("video", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()
