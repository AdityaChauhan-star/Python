# min  Ist method
a=[]
size=int(input("enter size of the list"))
for i in range(size):
     val=int(input("enter number"))
     a.append(val)
minval=min(a)
print("first min value in the list is=",minval)
a.remove(minval)
smin=min(a)
print("second min value of list is=",smin)

# min   second method
a=[]
size=int(input("enter size of the list"))
for i in range(size):
     val=int(input("enter number"))
     a.append(val)
a.sort()
print("list after sorting=",a)
print("first min number of list=",a[0])
print("second min number of list=",a[1])

# for print max number a[size-1] or a[size-2]
