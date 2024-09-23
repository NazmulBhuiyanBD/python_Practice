from array import *
arr=[[11,12,1,5],[9,88,25,69],[10,15,18,14],[85,89,96,]]
print(arr[0])
print(arr[2][2])

#insert
print()
print("after inserting")
arr.insert(2,[10,25,35,55,65])

for i in arr:
    for j in i:
        print(j,end=" ")
    print()

#deletion
print()
print("after deletion")
del arr[3]
for i in arr:
    for j in i:
        print(j,end=" ")
    print()

#udate
print()
print("after updating")
arr[2]=[5,6,7,8,9]
for i in arr:
    for j in i:
        print(j,end=" ")
    print()