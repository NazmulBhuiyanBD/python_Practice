import numpy as np

arr=np.array([1,2,3,4,5])
print(arr)
print(type(arr))

#2d array
arr2d=np.array([[1,2,4,5],[7,8,9,12]])
print(arr2d)

# convert list as array 
lit=[1,2,3,4]
arr1=np.array(lit)
print(arr1)

# 3d array
arr3d=np.array([[[1,2,3,4],[4,5,6,7]],[[1,2,3,5],[5,6,8,9]]])
print(arr3d)

# print dimention of array
print(arr1.ndim)
print(arr2d.ndim)
print(arr3d.ndim)

print(arr1[0:2])   #(start:finish:jump)
print(arr2d[1,1:2])   #((row=2,col=2)start:finish)
print(arr2d[:,0])    # :→ Select all rows 0→ Select the first column

print(arr3d[1,1,1])
print(arr3d[0,1,1:3])

print(arr.shape)
print(arr2d.shape)
print(arr3d.shape)

# concate array 
arrc1=([1,2,3,5,6])
arrc2=([1,2,3,5,6])
arrc3=np.concatenate((arrc1,arrc2))
print(arrc3)



#concate 2d array
arr2d2=np.array([[1,2,4,5],[7,8,9,12]])
arr2d3=np.array([[5,2,9,25],[5,18,2,1]])
arr2dc=np.concatenate((arr2d2,arr2d3),axis=1)
arr2dc2=np.concatenate((arr2d2,arr2d3),axis=0)
print(arr2dc)
print(arr2dc2)


# # vs stack ,hstack 
# pika=np.vstack(arr2d2,arr2d3)
# pika=np.hstack(arr2d2,arr2d3)
# print(pika)

#creating array
arr=np.zeros((4,5))
print(arr)
arr=np.ones((4,5))
print(arr)

arr=np.full((2,2),'a')
print(arr)

# identity matrix
arr=np.eye(4)
print(arr)

#Array ->random integer
print(np.random.randint(10,100,(3,3))) #(low,high,size)

arr = np.linspace(1, 10, 20)
print(arr)


# addition,substruction,division,multiplication

arr5=np.array([1,2,5,6])
arr6=np.array([1,2,5,6])
print(np.add(arr5,arr6))

print(np.multiply(arr5,arr6))
# print(np.divide(arr5,arr6))

print(np.cbrt(8))
print(np.power(2,8))
print(np.max(arr))
print(np.min(arr))

