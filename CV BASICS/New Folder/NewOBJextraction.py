import numpy as np
import cv2



org_img=cv2.resize(cv2.imread("CV BASICS/CVfiles/objsep/Contoso7.jpeg"),(500,500))

b,g,r=cv2.split(org_img)

hsv_img=cv2.cvtColor(org_img,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(org_img)

cv2.imshow("h",h)
cv2.imshow("s",s)
cv2.imshow("v",v)

cv2.calcHist(h,[0],None,[180],[0,180])
cv2.calcHist(s,[1],None,[256],[0,255])
hist=cv2.calcHist(v,[2],None,[256],[0,255])

print(np.unique(hist))

cv2.imshow("img",org_img)
print(org_img.shape)
print(org_img.dtype)
cv2.waitKey(0)
