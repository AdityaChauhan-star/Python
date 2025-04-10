#this function is used to append/insert the value at the last of list

a=["ram","shyam","gita","sita"]
print("list before append=",a)
a.append("mita")
print("list after append=",a)

#        or

a=[]
for i in range(5):
     x=input("enter the list")
     a.append(x)
print(a)
#        or

for i in a:
     print(i)
