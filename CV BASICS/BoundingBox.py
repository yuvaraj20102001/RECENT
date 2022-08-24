
from email.mime import image
import numpy as np
import cv2
import os
img=cv2.imread("CV BASICS/CVfiles/objsep/Contoso4.jpeg",0)
img=cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))
# hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# h,s,v=cv2.split(hsv)
gry_img=cv2.GaussianBlur(img,(5,5),0,0)

print(gry_img.shape)

thresh=cv2.threshold(gry_img,0, 255, cv2.THRESH_BINARY)[1]
# thresh=cv2.adaptiveThreshold(gry_img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,2)
# canny=cv2.Canny(thresh,0,255,cv2.THRESH_BINARY)
# dil=cv2.dilate(thresh,(3,3))

# cnt,hierarchy=cv2.findContours(dil,cv2.CHAIN_APPROX_SIMPLE,cv2.RETR_EXTERNAL)
# print(len(cnt))

# cv2.drawContours(img,cnt,255,(0,255,255),3)


# erode=cv2.erode(canny,(5,5))
cv2.imshow("img",img)
# cv2.imshow("img1",gry_img)
cv2.imshow("img2",thresh)
# cv2.imshow("img3",dil)
# cv2.imshow("img4",canny)


''' 
org_img1=cv2.imread("CV BASICS/CVfiles/objsep/Contoso1.jpeg")
# org_img2=cv2.imread("CV BASICS/CVfiles/objsep/Contoso2.jpeg")
org_img2=cv2.imread("CV BASICS/CVfiles/objsep/Contoso2.jpeg")
org_img3=cv2.imread("CV BASICS/CVfiles/objsep/Contoso3.jpeg")
org_img4=cv2.imread("CV BASICS/CVfiles/objsep/Contoso4.jpeg")
org_img5=cv2.imread("CV BASICS/CVfiles/objsep/Contoso5.jpeg")
cv2.imshow("img1",org_img1)
cv2.imshow("img2",org_img2)
cv2.imshow("img3",org_img3)
cv2.imshow("img4",org_img4)
cv2.imshow("img5",org_img5) '''

# images = os.listdir("CV BASICS/CVfiles/objsep")
# for i in images:
#     img = cv2.imread("CV BASICS/CVfiles/objsep/"+i)
#     cv2.imshow(f"img{i}",img)


cv2.waitKey(0)
