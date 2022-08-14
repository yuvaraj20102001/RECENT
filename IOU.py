import numpy as np

def IOU(BoxesA,BoxesB):
    Intersectx1=max(BoxesA[0],BoxesB[0])
    Intersecty1=max(BoxesA[1],BoxesB[1])
    Intersectx2=min(BoxesA[2],BoxesB[2])
    Intersecty2=min(BoxesA[3],BoxesB[3])
    IntersectArea=max(0,Intersectx2-Intersectx1+1)*max(0,Intersecty2-Intersecty1+1)

    BoxAArea=max(0,BoxesA[2]-BoxesA[0]+1)*max(0,BoxesA[3]-BoxesA[1]+1)
    BoxBArea=max(0,BoxesB[2]-BoxesB[0]+1)*max(0,BoxesB[3]-BoxesB[1]+1)
    UnionArea=BoxAArea+BoxBArea-IntersectArea

    iou=IntersectArea/float(UnionArea)
    
    print(IntersectArea,UnionArea,iou)


BoxesA=np.array([[39, 63, 203, 112]])

BoxesB=np.array([[54, 66, 198, 114]])

# [39, 63, 203, 112], [54, 66, 198, 114]
	# , [49, 75, 203, 125], [42, 78, 186, 126],
	# , [31, 69, 201, 125], [18, 63, 235, 135],
	# , [50, 72, 197, 121], [54, 72, 198, 120],







import numpy as np

BoxesA=np.array([[39, 63, 203, 112],
                 [49, 75, 203, 125],
                 [31, 69, 201, 125],
                 [50, 72, 197, 121],
                 [35, 51, 196, 110]])

BoxesB=np.array([[54, 66, 198, 114],
                 [42, 78, 186, 126],
                 [18, 63, 235, 135],
                 [54, 72, 198, 120],
                 [36, 60, 180, 108]])


BoxesA=(BoxesA).reshape(5,1,4)
BoxesB=(BoxesB).reshape(1,5,4)

x=list(np.broadcast(BoxesA,BoxesB))

x=np.array(x).reshape(25,4,2)
print(x)
print("")
# print(x[0,:])
Ix1=(np.max(x[:,0],axis=1))
Iy1=(np.max(x[:,1],axis=1))
Ix2=(np.max(x[:,2,:],axis=1))
Iy2=(np.max(x[:,3],axis=1))

# Ix1=np.max(x[:,:,:,0],axis=1)
# print("Ix1:::",Ix1)
# print("")
# # Iy1=np.max(x[:,1],axis=1)
# print("Iy1:::",Iy1)
# print("")
# # Ix2=np.max(x[:,2],axis=1)
# print("Ix2:::",Ix2)
# print("")
# # Iy2=np.max(x[:,3],axis=1)
# print("Iy2:::",Iy2)
# # print(BoxesA,BoxesB)

# print("")


# IntersectArea=np.abs(Ix2-Ix1)*np.abs(Iy2-Iy1)


# print("")
# print(IntersectArea)



BoxA=x[:,:,1]
BoxB=x[:,:,0]



print("\n")

BoxAPointx=np.abs(BoxA[:,2]-BoxA[:,0])
BoxAPointy=np.abs(BoxA[:,3]-BoxA[:,1])
BoxBPointx=np.abs(BoxB[:,2]-BoxB[:,0])
BoxBPointy=np.abs(BoxB[:,3]-BoxB[:,1])

print(BoxAPointx,BoxAPointy,BoxBPointx,BoxBPointy)
print("\n")

BoxAArea=np.multiply(BoxAPointx,BoxAPointy)
BoxBArea=np.multiply(BoxBPointx,BoxBPointy)

print("\n")
print(BoxAArea,BoxBArea)

UnionArea=BoxAArea+BoxBArea-IntersectArea
print("\n")
print(UnionArea,IntersectArea)



iou=np.divide(IntersectArea,UnionArea.astype('float64'))

print("\n")
print(iou.reshape(5,5))








































import numpy as np

BoxesA=np.array([[39, 63, 203, 112],
                 [49, 75, 203, 125],
                 [31, 69, 201, 125],
                 [50, 72, 197, 121],
                 [35, 51, 196, 110]])

BoxesB=np.array([[54, 66, 198, 114],
                 [42, 78, 186, 126],
                 [18, 63, 235, 135],
                 [54, 72, 198, 120],
                 [36, 60, 180, 108]])


BoxesA=(BoxesA).reshape(5,1,4)
BoxesB=(BoxesB).reshape(1,5,4)

x=list(np.broadcast(BoxesA,BoxesB))

x=np.array(x).reshape(25,4,2)
print(x)
print("")
# print(x[0,:])
Ix1=(np.max(x[:,0],axis=1))
Iy1=(np.max(x[:,1],axis=1))
Ix2=(np.max(x[:,2,:],axis=1))
Iy2=(np.max(x[:,3],axis=1))

# Ix1=np.max(x[:,:,:,0],axis=1)
# print("Ix1:::",Ix1)
# print("")
# # Iy1=np.max(x[:,1],axis=1)
# print("Iy1:::",Iy1)
# print("")
# # Ix2=np.max(x[:,2],axis=1)
# print("Ix2:::",Ix2)
# print("")
# # Iy2=np.max(x[:,3],axis=1)
# print("Iy2:::",Iy2)
# # print(BoxesA,BoxesB)

# print("")


# IntersectArea=np.abs(Ix2-Ix1)*np.abs(Iy2-Iy1)


# print("")
# print(IntersectArea)



BoxA=x[:,:,1]
BoxB=x[:,:,0]



print("\n")

BoxAPointx=np.abs(BoxA[:,2]-BoxA[:,0])
BoxAPointy=np.abs(BoxA[:,3]-BoxA[:,1])
BoxBPointx=np.abs(BoxB[:,2]-BoxB[:,0])
BoxBPointy=np.abs(BoxB[:,3]-BoxB[:,1])

print(BoxAPointx,BoxAPointy,BoxBPointx,BoxBPointy)
print("\n")

BoxAArea=np.multiply(BoxAPointx,BoxAPointy)
BoxBArea=np.multiply(BoxBPointx,BoxBPointy)

print("\n")
print(BoxAArea,BoxBArea)

UnionArea=BoxAArea+BoxBArea-IntersectArea
print("\n")
print(UnionArea,IntersectArea)



iou=np.divide(IntersectArea,UnionArea.astype('float64'))

print("\n")
print(iou.reshape(5,5))
