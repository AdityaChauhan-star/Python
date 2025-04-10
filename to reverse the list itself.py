a=[]
size=int(input("enter the size of the list"))
for i in range(size):
     val=int(input("enter number "))
     a.append(val)
i=0
j=size-1
while(i<j):
     t=a[i]
     a[i]=a[j]
     a[j]=t
     i=i+1
     j=j-1
print("list after reverse")
for i in range(size):
     print(a[i])
