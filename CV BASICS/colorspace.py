import numpy as np
import cv2 as cv2

BGR_img=cv2.imread("CV BASICS/archive/data/messi5.jpg")
cv2.imshow("BGR_img", BGR_img)

HSV_img=cv2.cvtColor(BGR_img,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV_img", HSV_img)

HSV_img[:,:,0]-=20


cv2.imshow("HSV!!_img", HSV_img)
HSV_img=cv2.cvtColor(HSV_img,cv2.COLOR_HSV2BGR)
cv2.imshow("HSV!_img", HSV_img)
if(cv2.waitKey(0) ==13):
    cv2.destroyAllWindows()