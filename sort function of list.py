#this function is used to arrange the elements in either in ascending or descending order

a=[5,2,8,3,7]
a.sort()
print(a)

#program to implement

a=[]
size=int(input("enter the size of the list"))
for i in range(size):
     x=input("enter element in the list")
     a.append(x)
a.sort()
print(a)
