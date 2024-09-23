tuple1=(1,2,5,6)
print(tuple1)

country=("Usa","UK","Canda","Germany","india")

if "Germany" in country:
    print("Germany is present")
else:
    print("germany is not present")


#range of Index
tple=("pen","pencil","eraser","sharpner","marker","noteBook","stapler")
print(tple[1:4])    #(start:end:jumper)
print(tple[2:5:2])
print(tple[3:])

#manupulate tuple
country=("spain","italy","india","england","bangladesh","germany")
temp=list(country)
print(temp)     #it will convert into list

temp.append("Russia")
temp.pop(2)
print(temp)

country=tuple(temp)     #now convert into tuple
print(country)

#unpacking tuple
info=("john",21,"stanford")
(name,age,university)=info
print("name :",name)
print("age :",age)
print("studies ",university)