#this function is used to delete the last element of the list

a=[]
for i in range(5):
     x=int(input("enter element in the list"))
     a.append(x)
a.pop()
print(a)
