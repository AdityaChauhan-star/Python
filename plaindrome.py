i=int(input("enter number"))
rev=0
x=i
while(i>0):
    rev=(rev*10)+i%10
    i=i//10
if(x==rev):
    print("plaindrome number")
else:
    print("not plaindrome")
