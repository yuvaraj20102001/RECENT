import numpy as np
import cv2
import matplotlib.pyplot as plt


org_img=cv2.resize(cv2.imread("CV BASICS/CVfiles/objsep/Contoso4.jpeg"),(500,500))



print(org_img.shape)
print(org_img.dtype)

hsv=cv2.cvtColor(org_img,cv2.COLOR_BGR2HSV)
cv2.imshow("org_img",hsv)
roi=org_img[150:190,150:190]
roihsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)


M = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )
I = cv2.calcHist([roihsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )

# plt.plot(M,I)
# R=M/I

# h,s,v=cv2.split(roihsv)
# B=R[h.ravel(),s.ravel()]


# B = np.minimum(B,1)
# B = B.reshape(roihsv.shape[:2])



# # apply a convolution with a circular disc
# disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
# cv2.filter2D(B,-1,disc,B)
# B = np.uint8(B)
# cv2.normalize(B,B,0,255,cv2.NORM_MINMAX)



# # Use thresholding to segment out the region
# ret,thresh = cv2.threshold(B,10,255,0)

# # Overlay images using bitwise_and
# thresh = cv2.merge((thresh,thresh,thresh))
# res = cv2.bitwise_and(roi,thresh)

# # Display the output
# cv2.imshow('a',res)


print(roi.shape)
cv2.imshow("roi",roihsv)

cv2.waitKey(0)













