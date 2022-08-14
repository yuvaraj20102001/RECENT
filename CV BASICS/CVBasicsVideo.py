from cv2 import destroyAllWindows, waitKey
import numpy as np
import cv2 as cv2


code=cv2.VideoWriter_fourcc(*'MJPG')
out=cv2.VideoWriter('Output.mp4',code,20.0,(480,480))

cap=cv2.VideoCapture(0)
if cap.isOpened()==0:
    print("Capture not opened")
    exit()

while True:
    ret,frame=cap.read()
    if not ret:
        print("Frames not returned")
        break

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray video captured",gray)
    out.write(gray)

    if(cv2.waitKey(1)==ord('q')):
        break
cap.release()
out.release()
destroyAllWindows()