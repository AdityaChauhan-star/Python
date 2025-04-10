a=int(input("enter first number"));
b=int(input("enter second number"));
c=int(input("enter second number"));
d=int(input("enter second number"));
e=int(input("enter second number"));
total=a+b+c+d+e
percent=(total/500)*100
print("Total marks=",total,"Percent=",percent)
if percent>=80:
    print("you have got grade A ")
elif percent>=60:
    print("you have got grade B")
elif percent>=40:
    print("you have got grade C")
else:
    print("you have got grade d")
    
