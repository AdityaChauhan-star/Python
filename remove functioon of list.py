#this function is used to delete an element from the given list

a=[5,"ram",10,"ravi",10]
a.remove(10)
print(a)

#program to implement

a=[]
for i in range(6):
     b=input("enter element")
     a.append(b)
print("list before removal of element",a)
element=input("enter element you want to remove")
a.remove(element)
print("list after removal of the element",a)
