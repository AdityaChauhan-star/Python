a=input("enter string")
print(a[-1::-1])

# reverse a string using for loop

a=input("enter string")
for i in range((len(a)-1),-1,-1):
    print(a[i],end='')
