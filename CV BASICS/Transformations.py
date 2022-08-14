import cv2 as cv2


import numpy as np


Org_img=cv2.imread("Face-recoginition/filter/input.jpg")
Org_img=cv2.resize(Org_img,(480,480))
Org_mat=np.arange(9.0).reshape((3,3))


resize_mat1=cv2.resize(Org_mat,(5,5),interpolation=cv2.INTER_AREA)

resize_mat2=cv2.resize(Org_mat,(5,5),interpolation=cv2.INTER_CUBIC)

resize_mat3=cv2.resize(Org_mat,(5,5),interpolation=cv2.INTER_NEAREST)

resize_mat4=cv2.resize(Org_mat,(5,5),interpolation=cv2.INTER_LINEAR)

resize_mat5=cv2.resize(Org_mat,(5,5),interpolation=cv2.INTER_LANCZOS4)

print(resize_mat1)
print(resize_mat2)
print(resize_mat3)
print(resize_mat4)
print(resize_mat5)


Transl=np.float32([[1,0,100],[0,1,50]])
rotate=np.float32([[0,-1,400],[1,0,50]])
scaled=np.float32([[0.5,0,0],[0,0.5,0]])

(rows,cols,ch)=Org_img.shape
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)
print(M)
dst1 = cv2.warpAffine(Org_img,rotate,(cols,rows))
dst2= cv2.warpAffine(Org_img,Transl,(cols,rows))
dst3= cv2.warpAffine(Org_img,scaled,(cols,rows))

cv2.imshow("rotation", dst1)
cv2.imshow("scale", dst3)
cv2.imshow("translation", dst2)
# Org_mat=cv2.resize(Org_mat,None,fx=0.5,fy=0.5)



if(cv2.waitKey(0)==13):
    cv2.destroyAllWindows()
