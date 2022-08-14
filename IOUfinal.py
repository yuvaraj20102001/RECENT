import numpy as np


m1,n1=list(map(int,input("Enter the size of Box 'A' ::").split(",")))
print("Enter the box 'A'elements ::")
BoxesA=np.array([[input().split(",")]for _ in range(m1)],int)
BoxesA=np.squeeze(BoxesA)

m2,n2=list(map(int,input("Enter the size of Box 'B' ::").split(",")))
print("Enter the box 'B'elements ::")
BoxesB=np.array([[input().split(",")]for _ in range(m2)],int)
BoxesB=np.squeeze(BoxesB)



BoxesA=(BoxesA).reshape(m1,1,4)
BoxesB=(BoxesB).reshape(1,m2,4)

x=list(np.broadcast(BoxesA,BoxesB))

x=np.array(x).reshape((m1*m2),4,2)

Ix1=(np.max(x[:,0],axis=1))
Iy1=(np.max(x[:,1],axis=1))
Ix2=(np.min(x[:,2],axis=1))
Iy2=(np.min(x[:,3],axis=1))


Ix=np.array(list(np.broadcast(0,(Ix2-Ix1)+1)))
Iy=np.array(list(np.broadcast(0,(Iy2-Iy1)+1)))


IntersectArea=np.max(Ix,axis=1)*np.max(Iy,axis=1)


BoxA=x[:,:,0]
BoxB=x[:,:,1]

BoxAX=np.array(list(np.broadcast(0,(BoxA[:,2]-BoxA[:,0])+1)))
BoxAY=np.array(list(np.broadcast(0,(BoxA[:,3]-BoxA[:,1])+1)))
BoxBX=np.array(list(np.broadcast(0,(BoxB[:,2]-BoxB[:,0])+1)))
BoxBY=np.array(list(np.broadcast(0,(BoxB[:,3]-BoxB[:,1])+1)))    

BoxAPointx=np.max(BoxAX,axis=1)
BoxAPointy=np.max(BoxAY,axis=1)
BoxBPointx=np.max(BoxBX,axis=1)
BoxBPointy=np.max(BoxBY,axis=1)


BoxAArea=np.multiply(BoxAPointx,BoxAPointy)
BoxBArea=np.multiply(BoxBPointx,BoxBPointy)


UnionArea=BoxAArea+BoxBArea-IntersectArea
print("\n")

iou=np.divide(IntersectArea,UnionArea.astype('float64'))

print("\n")
print(iou.reshape(m1,m2))

