# lst=[10,25,36,39,41,45,58]
# for item in lst:
#     print(item,end=" ")

# #we can print another way
# print()
# lenth=len(lst)
# for i in range (lenth):
#     print(lst[i],end="\t")

# #finding element
# print()
# key=int(input("Enter number to be searched "))
# found=False
# for i in lst:
#     if(i==key):
#         found=True
# if(found==True):
#     print("Element is found")
# else:
#     print("Not found")

# #sum of all elements
# print()
# print("Total is : ",sum(lst))

# #list element + operation
# print()
# l1=[1,2,3]
# l2=[5,6,7]
# l3=l1+l2
# print("L3=",l3)

# #list element * operation
# print()
# lst1=[1,2,3]
# lst2=lst1*2
# print(" * list operation ",lst2)    #here list will be show 10 times repeated


# #slice
# number=[51,52,53,54,55]
# sublist=number[1:3]     #starting index and ending index
# print(sublist)

# sublist2=number[::2]    #this will give 0,2,4 index of the list .here 2 is the increment
# print(sublist2)

# #append()
# list1=[]
# list1.append(13)
# list1.append(23)
# list1.append(33)
# print(list1)

# #clear()- make list empty
# print("after clear list")
# list1.clear()
# print(list1)

# #copy()
# list1=[1,2,3]
# list2=list1.copy()
# print(list2)
# print(id(list1))
# print(id(list2))

# list2=list1     #if we do this way then their id will be same. so they ar using the same resources
# print(id(list1))
# print(id(list2))

# #list.count(x)->number of occurence of x in list

# list1=[10,21,15,25,39,10]
# x=10
# print(list1.count(x))       #ans will be 2-->10 2time vissible

# #extend()
# list1=[1,2,3]
# list2=[4,5,6]
# list1.extend(list2)
# print(list1)

# #list.index(x)
# list1=[1,2,5]
# print(list1.index(2))

# #list1.insert(i,x) ---i=index, x=value
# list1=[1,2,5,9,11,6]
# x=55
# list1.insert(2,x)
# print(list1)

# # list1.pop()->reomove & returen the last element
# list1=[1,2,3,5,9,11]
# list1.pop()
# print(list1)

# #list1.remove(x)
# list1=[1,5,8,99,4,7,6,99]
# x=99
# list1.remove(x)
# print(list1)

# #reverse()
# list1=[1,5,8,9,7]
# list1.reverse()
# print(list1)

# #sort()
# list2=[55,85,12,11,5]
# list2.sort()
# print(list2)
# list2.sort(reverse=True)
# print(list2)

# #square
# squares=[x**2 for x in range(10)]
# print(squares)

# evenSquares=[x**2 for x in range(10) if x%2==0]
# print(evenSquares)

#maximum and minimum
li=[5,88,99,101,1,18,65,25]
max_li=max(li)
mini_li=min(li)
print("maximum ",max_li,"minimum ",mini_li)