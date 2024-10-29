def fun(a,b):
    return a+b
print(fun(5,11))

def mul(*Args):
    out=1
    for i in Args:
        out=i*out
    return out
print(mul(5,10,25,36))
listp=["apple","banana","pineapple","mangoes"]
def fruits(fr):
    for i in fr:
        print(i)
fruits(listp)

#we can use string also
fruits("Hello this is nazmul Haque Bhuiyan")

#factorial
def fact(num):
    if(num==0 or num==1):
        return 1
    else:
        return num*fact(num-1)

print(fact(4))

# fibonacci
def fibo(num):
    if(num==1 or num==0):
        return num
    else:
        return fibo(num-1)+fibo(num-2)
print(fibo(8))  #1 1 2 3 5 8 13 21


# lamda function
var =lambda a,b,c:a+b+c
print(var(5,10,25))

def func(n):
    return lambda a:a*n

var2=func(10)
print(var2(11))

# map function
numb=[1,3,5,8]
res=map(lambda x:x*x,numb)
print(list(res))

