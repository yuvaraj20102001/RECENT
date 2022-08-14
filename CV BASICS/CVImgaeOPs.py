import re
import numpy as np
import cv2 as cv2




path2="CV BASICS/archive/data/messi5.jpg"
roi_img=cv2.imread(path2)

ball = roi_img[280:340, 330:390]
roi_img[273:333, 100:160] = ball


ball1= roi_img[280:340, 330:390]
roi_img[223:283, 110:170] = ball1



cv2.imshow("roi_img",roi_img)

# cv2.imshow("ball",ball1)




#Borders

constant= cv2.copyMakeBorder(roi_img,10,10,10,10,cv2.BORDER_CONSTANT,value=(0,0,255))
replicate= cv2.copyMakeBorder(roi_img,10,10,10,10,cv2.BORDER_REPLICATE)
reflect= cv2.copyMakeBorder(roi_img,10,10,10,10,cv2.BORDER_REFLECT)
reflect101= cv2.copyMakeBorder(roi_img,10,10,10,10,cv2.BORDER_REFLECT101)
wrap= cv2.copyMakeBorder(roi_img,10,10,10,10,cv2.BORDER_WRAP)

# borders= np.hstack([constant,replicate])

cv2.imshow("constant",constant)
cv2.imshow("replicate",replicate)
cv2.imshow("reflect",reflect)
cv2.imshow("reflect101",reflect101)

cv2.imwrite("replicate.jpg",replicate)

print(replicate[1,:10,:])
print(replicate[1,10:,:])
print(replicate[1,-10:,:])
cv2.imshow("wrap",wrap)
x=cv2.waitKey(0)
if x==ord('q'):
    cv2.destroyAllWindows()