import cv2
import numpy as np

img=cv2.imread("Face-recoginition/filter/1.jpg")

print(img.dtype)
B,G,R=cv2.split(img)

cv2.imshow("B",B)
cv2.imshow("G",G)
cv2.imshow("R",R)

cv2.imshow("img",img[:,:,1])

if(cv2.waitKey(0)==13):
    cv2.destroyAllWindows()