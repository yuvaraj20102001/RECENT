import numpy as np
import cv2 as cv2
Black_img=np.ones((512,512,3),np.uint8)

cv2.line(Black_img,(0,0),(511,511),(255,0,0),5)
cv2.line(Black_img,(255,511),(255,0),(255,0,0),5)

cv2.line(Black_img,(0,512),(512,0),(255,0,0),5)

cv2.circle(Black_img,(255,255),30,(255,255,0,),5)
cv2.rectangle(Black_img,(0,0),(50,50),(255,255,0,),5)

cv2.ellipse(Black_img,(255,255),(100,50),0,0,360,(255,0,255),4)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(Black_img,[pts],True,(0,255,255))
cv2.imshow("Black_img", Black_img)
if(cv2.waitKey(0)==ord('q')):
    cv2.destroyAllWindows()
