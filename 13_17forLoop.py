for i in range(1,4): #range (start,end-1)
    print(i)

#for loop with else statement
for j in range(1,9): 
    print(j)
else:
    print("No Break\n")

#list
students=["John","Harry","Ron"]
for student in students:
    print(student)

for i in range(1,10):
    if(i==5):
        continue
    elif(i==8):
        break
    print(i)