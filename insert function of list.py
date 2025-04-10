#this function is used to insert an element at the given index

a=['ram',5,10]
a.insert(1,'hello')
print(a)

#implement

a=[]
for i in range(5):
     x=input("enter element in list")
     a.append(x)
print("list before insertion=",a)
index=int(input("enter index where you want to insert"))
element=input("enter element you want to insert")
a.insert(index,element)
print("list after insertion=",a)
