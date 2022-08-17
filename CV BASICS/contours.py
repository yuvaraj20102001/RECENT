import numpy as np
import cv2

hand=cv2.imread("CV BASICS/CVfiles/hand.jpg")

hand1=cv2.cvtColor(hand,cv2.COLOR_BGR2GRAY)
cv2.imshow("hand1",hand1)
hand1=cv2.GaussianBlur(hand1,(5,5),0)
_,thresh=cv2.threshold(hand1,230,255,cv2.THRESH_BINARY_INV)


cv2.imshow("thresh",thresh)

contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(hand,contours,-1,(50,105,100),3)

hull=[]
cv2.imshow("hand",hand)
for i in range(len(contours[1:])):
    hull.append(cv2.convexHull(contours[i],False))
    cv2.drawContours(hand,hull,i,(0,255,0),1,8)

cv2.imshow("hand2",hand)
# epsilon = 0.1*cv2.arcLength(contours,True)
# approx = cv2.approxPolyDP(contours,epsilon,True)

# cv2.drawContours(hand,approx,-1,(50,105,100),3)
# cv2.imshow("hand2",hand)
print(contours)

cv2.waitKey(0)