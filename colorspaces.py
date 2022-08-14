import numpy as np
import cv2 as cv2



img=np.random.randint(50,255,(5,5,3),np.uint8)
print(img,end="\n\n\n")


# # RGB IMAGE--> GRY IMAGE
# img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgB=img[:,:,0]
# imgG=img[:,:,1]
# imgR=img[:,:,2]
# cv2.imshow("cvt COLOR",img1)
# imgGray=(imgB+imgR+imgG)//3
# imgGray2= ((0.3 * imgR) + (0.59 * imgG) + (0.11 * imgB)).astype(np.uint8)
# print(imgGray2)
# cv2.imshow("average",imgGray)
# cv2.imshow("Gray percentage",imgGray2)



# RGB IMAGE--> HSV IMAGE
img2=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

print(img2)
cv2.imshow("HSV",img2)



cv2.imshow("Original",img)
if(cv2.waitKey(0)==13):
    cv2.destroyAllWindows()
