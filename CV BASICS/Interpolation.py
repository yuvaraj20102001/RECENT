import cv2
import numpy as np

img=np.ones((9,9),dtype=np.uint8)
img[3:6,]=255
img[:,3:6]=255
img[4]=1
img[:,4]=1
print(img)

print("\n\n")

img1=cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
img2=cv2.resize(img,None,fx=0.25,fy=0.25,interpolation=cv2.INTER_AREA)
img3=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_AREA)

img1=cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_LINEAR)
img2=cv2.resize(img,None,fx=0.25,fy=0.25,interpolation=cv2.INTER_LINEAR)
img3=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_LINEAR)

cv2.imshow("img",img)
cv2.imshow("img1",img1)
cv2.imshow("img3",img3)

print(img1,img2,img3,sep='\n\n')

if(cv2.waitKey(0)==13):
    cv2.destroyAllWindows()