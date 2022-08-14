import cv2 as cv2
import numpy as np

def draw_circle(events,x,y,flags,param):
    if events==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),50,(255,255,0),5)


img=np.zeros((512,512,3),np.uint8)

cv2.namedWindow("Mouse Events",cv2.WINDOW_NORMAL)
print(cv2.setMouseCallback("Mouse Events",draw_circle))

while(1):
    cv2.setMouseCallback("Mouse Events",draw_circle)
    cv2.imshow("mouse_event",img)
    if(cv2.waitKey(10) & 0xFF ==27):
        break
cv2.destroyAllWindows()