from cv2 import MORPH_GRADIENT, erode
import numpy as np
import cv2 as cv2

img = cv2.imread("CV BASICS/archive/data/butterfly.jpg")
img=np.random.randint(50,255,(5,5),np.uint8)
print(img,end="\n")
kernel=np.ones((3,3),np.uint8)
dil=cv2.dilate(img,kernel)
ero=cv2.erode(img,kernel)
# cv2.imshow("dilated",dil)
# cv2.imshow("eroded",ero)
open=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
# cv2.imshow("opening",open)

close=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
# cv2.imshow("closing",close)

grad= cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
# cv2.imshow("grad",grad)

tophat=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)

blackhat=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)

print(dil,ero,open,close,grad,tophat,blackhat,sep="\n\n")
if(cv2.waitKey(0)==13):
    cv2.destroyAllWindows()
