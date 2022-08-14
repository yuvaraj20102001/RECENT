import cv2
from cv2 import BORDER_DEFAULT
import numpy as np

img=cv2.imread("CV BASICS/archive/data/sudoku.png")

# cv2.imshow("img",img)

img=np.zeros((5,5),np.uint8)
img[:,2]=255

print("Original image::\n")
print(img)

SobelY=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
SobelX=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])

imgX=cv2.filter2D(img,-1,SobelX)
imgY=cv2.filter2D(img,-1,SobelY)



print("Horizontal and Vertical edges::\n")
print(imgX,imgY,sep='\n\n')
# imgx = cv2.Sobel(img,-1,1,0,ksize=3)
     
#     # Calculation of Sobely

# imgy = cv2.Sobel(img,-1,0,1,ksize=3)

Sobel=np.sqrt(imgX**2+imgY**2)

# cv2.imshow("Sobel",Sobel)
# cv2.imshow("SobelX",imgX)
# cv2.imshow("SobelY",imgY)

# G=np.sqrt(imgX**2+imgY**2)

# print("Sobel includes both the edges::\n")
print(Sobel)

# print(G)
cv2.waitKey(0)