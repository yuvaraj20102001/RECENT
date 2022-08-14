import  cv2 as cv2
import numpy as np

img=np.ones((9,9),dtype=np.uint8)

img[:,5]=200
img[5,:]=200
print(img)
Gx=cv2.Sobel(img,-1,dx=1,dy=0,ksize=3)
Gy=cv2.Sobel(img,-1,dx=0,dy=1,ksize=3)
theta=(np.arctan2(Gy,Gx)*180/np.pi ) % 180
img=Gx+Gy
print(Gx,Gy,sep='\n\n')

print(theta)

print(img)

if(cv2.waitKey(0)==13):
    cv2.destroyAllWindows()