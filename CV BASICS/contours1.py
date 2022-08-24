import cv2
import numpy as np
import random

img=cv2.imread("Face-recoginition/rect2.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
print(thresh.shape)
contours,heirarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(img,contours[1:],-1,(0,100,100),1)
# print(contours)

for contour in contours[1:]:
    # contour=contour.ravel()
    # approx=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    cont=contour.ravel()
    # print(len(approx))
    color = random.sample(range(255),3)
    print(color)

    for j in range(1,len(cont),2):
        cv2.circle(img,(cont[j-1],cont[j]),10,color,1)
        





cv2.imshow("img",img)
cv2.waitKey(0)
