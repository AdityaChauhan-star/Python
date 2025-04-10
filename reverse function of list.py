#this function is used to reverse the element present in the list

a=[5,'ram',10,'ravi',10]
a.reverse()
print(a)

#program to implement

a=[]
size=int(input("enter the size of the list"))
for i in range(size):
     x=input("enter element in the list")
     a.append(x)
a.reverse()
print(a)
