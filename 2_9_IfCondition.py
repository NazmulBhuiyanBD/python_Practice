# > < ==

x=int(input("what is x?"))
y=int(input("what is y?"))
if(x<y):
    print("x is less than y")
elif(x>y):
    print("x is greater than y")
else:
    print("x is equal to y")


#nested if statement
number=int(input("Enter any value"))
if(number>=0):
    if(number==0):
        print("Number is Zero")
    else:
        print("Number is positive")
else:
    print("Number Is Negative")