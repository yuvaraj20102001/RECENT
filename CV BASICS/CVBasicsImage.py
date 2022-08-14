import cv2 as cv2
import numpy as np

path="CV BASICS/CVfiles/RGB.jpeg"
img2=cv2.resize(cv2.imread(path,-1),(302,342))
img0=cv2.resize(cv2.imread(path,0),(302,342))
img1=cv2.resize(cv2.imread(path,1),(302,342))

cv2.imshow("Gray scale",img0)
cv2.imshow("Colored",img1)


# cv2.imshow("Unchanged",img2)
print(img2.shape)
img=cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
hsvimg=cv2.imread("CV BASICS/CVfiles/HSV.jpeg")
cv2.imshow("HSV scale",hsvimg)

H,S,V=cv2.split(hsvimg)
print(hsvimg.shape)
HSV=np.hstack([H,S,V])
cv2.imshow("HSV",HSV)



k=cv2.waitKey(0)

if(k==ord('x')):
    cv2.destroyAllWindows()
