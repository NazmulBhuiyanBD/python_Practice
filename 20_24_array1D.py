#1D array

# import array as arr
# a = arr.array('d', [1.1, 3.5, 4.5])
# print(a)

from array import *
array1=array('i',[10,25,36,39,40])
array1.insert(1,60)     #in index 1 we insert 60 and 25 index will be 2

for x in array1:
    print(x)

array1.remove(39)
for x in array1:
    print(x)


#update value
array1[3]=50
array1[4]=60
for x in array1:
    print("after update the array ",x)
