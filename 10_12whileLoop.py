#while Loop
i=0
while(i<3):
    print("Hello i=",i)
    i+=1
#While with else    
i=5
while(i<9):
    print("Hello i=",i)
    i+=1
else:
    print("No Break")

#count digit
n=int(input("Enter n"))
count=0

while(n>0):
    count+=1
    n=n//10     # Use integer division to avoid floating-point numbers
print("Count of digit :",count)


#multiplication table
num=int(input("Enter the number :"))
i=1
while(i<=10):
    print(num,"X",i,"=",num*i)
    i+=1


#sum of 10 natural number
i=1
total=0
while(i<=10):
    total+=i
    i+=1
print("Sum of Natural Number is :",total)