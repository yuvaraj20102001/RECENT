import cv2 as cv2
import numpy as np

img=cv2.imread("CV BASICS/archive/data/sudoku.png")
cv2.imshow("Hello World",img)
img=cv2.resize(img,(350,350),None,interpolation=cv2.INTER_CUBIC)

cv2.imshow("Hello World",img)

''' img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) '''

ret,threshbin=cv2.threshold(img,100,255,cv2.THRESH_BINARY)
ret,threshbininv=cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV)
ret,threshtrunc=cv2.threshold(img,100,255,cv2.THRESH_TRUNC)
ret,threshtozero=cv2.threshold(img,100,255,cv2.THRESH_TOZERO)
ret,threshtozeroinv=cv2.threshold(img,100,255,cv2.THRESH_TOZERO_INV)

thresh=np.hstack([threshbin,threshbininv,threshtrunc,threshtozero,threshtozeroinv])
cv2.imshow("Thresholding",thresh)
''' 
athreshmean=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
# athreshgauss=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
#  '''
# athresh=np.hstack([athreshmean,athreshgauss])
# cv2.imshow("Adaptive threshold",athresh)

# ret,othresh=cv2.threshold(img,100,255,cv2.THRESH_OTSU)
# cv2.imshow("OTSU threshold",othresh)


if(cv2.waitKey(0)==13):
    cv2.destroyAllWindows()