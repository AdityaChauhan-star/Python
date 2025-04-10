a=[]
size=int(input("enter the size of the list"))
for i in range(size):
     val=int(input("enter elements"))
     a.append(val)
even=0
odd=0
for i in range(size):
     if(a[i]%2==0):
          even=even+1
     else:
          odd=odd+1
print("total even=",even,"total odd=",odd)
