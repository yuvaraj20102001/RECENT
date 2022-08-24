from pickletools import uint8
import numpy as np
import cv2

matrix=np.zeros((5,5,5,3),dtype=np.uint8)

mat_seperator=5
final_pallate=[]

for r in range(0,mat_seperator):
    for g in range(0,mat_seperator):
        for b in range(0,mat_seperator):
            r_approx=r/5*255
            g_approx=g/5*255
            b_approx=b/5*255
            final_pallate.append(np.array([r_approx,g_approx,b_approx],np.uint8))
print(len(final_pallate))
final_pallate=np.array(final_pallate)

cv2.imshow("final_pallate",final_pallate)
cv2.waitKey(0)
