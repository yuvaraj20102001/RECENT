import numpy as np 
import cv2 as cv

img1=cv.imread("CV BASICS/archive/data/aero1.jpg")
img2=cv.imread("CV BASICS/archive/data/aero3.jpg")


''' ADDITION OF IMAGE '''

# cv.imshow("gray img", img1)
# cv.imshow("Newimage", img2)
Add_img=cv.add(img1,img2)

np_add=np.add(img1,img2)
# cv.imshow("Add image",Add_img)
# cv.imshow("Numpy add",np_add)

print(img1.shape)


print("")
print(img1[0,0,:],img2[0,10,:])

print("Add image")
print("Numpy add",np_add[0,0,:])
print("CV add",Add_img[0,0,:])


print("")

''' SUBTRACTION OF IMAGE '''

# cv.imshow("gray img", img1)
# cv.imshow("Newimage", img2)
Sub_img=cv.subtract(img1,img2)

np_sub=np.subtract(img1,img2)
# cv.imshow("Add image",Add_img)
# cv.imshow("Numpy add",np_add)
print(img1[0,0,:],img2[0,10,:])

print("Sub image")
print("Numpy sub",np_sub[0,0,:])
print("CV sub",Sub_img[0,0,:])

print("")


''' MULTIPLICATION OF IMAGE '''

# cv.imshow("gray img", img1)
# cv.imshow("Newimage", img2)
Mul_img=cv.multiply(img1,img2)

np_mul=np.multiply(img1,img2)
cv.imshow("Mul image",Mul_img)
cv.imshow("Numpy mul",np_mul)
print(img1[0,0,:],img2[0,10,:])

print("Mul image")
print("Numpy mul",np_mul[0,0,:])
print("CV mul",Mul_img[0,0,:])

print("")

''' DIVISION OF IMAGE '''

# cv.imshow("gray img", img1)
# cv.imshow("Newimage", img2)
Div_img=cv.divide(img1,img2)

np_div=np.divide(img1,img2)
cv.imshow("Div image",Div_img)
cv.imshow("Numpy div",np_div)
print(img1[0,0,:],img2[0,10,:])

print("Div image")
print("Numpy div",np_div[0,0,:])
print("CV div",Div_img[0,0,:])

if(cv.waitKey(0)==ord('q')):
    cv.destroyAllWindows()