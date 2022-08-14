import numpy as np
import cv2 as cv2


# img = cv2.imread("Face-recoginition/filter/input.jpg")
img=np.random.randint(50,255,(5,5,3),np.uint8)
# kernel = np.ones((3,3),np.float32)
# kernel=np.array()

cv2.imshow("img1",img)
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(img)
print("")


print(" ")
# dst = cv2.filter2D(img,-1,kernel)


# print(kernel)

# print(dst)
dst=cv2.medianBlur(img,5)
cv2.imshow("Convoluted",dst)
cv2.imshow("img",img)
# print(dst)

if(cv2.waitKey(0)==13):
    cv2.destroyAllWindows()