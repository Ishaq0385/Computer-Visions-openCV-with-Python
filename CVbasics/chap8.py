#convert into gray scale video
#reading a video
import cv2 as cv
from cv2 import imwrite

cap = cv.VideoCapture('resources/video.mp4')
q
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
#writing format, codec, video writer object anf file output
out = cv.VideoWriter("resources/out_video.avi", cv.VideoWriter_fourcc('M', 'j', 'p', 'G'), 10, (frame_width, frame_height), isColor = False)


while(True):
    ret, frame = cap.read()

    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #(thresh, binary) = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
    if ret == True:
        out.write(grayframe)
        cv.imshow("video", grayframe)
        #to quit with q key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv.destroyAllWindows()
