a=[]
size=int(input("enter the size of the list"))
for i in range(size):
     val=int(input("enter element"))
     a.append(val)
print("list=",a)
sum=0
for i in range(size):
     sum=sum+a[i]
print("sum of list elements=",sum)
