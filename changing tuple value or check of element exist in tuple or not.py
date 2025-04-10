x=("Apple","Banana","Cherry")
y=list[x]
print(y)
y[1]=("Kiwi")
x=tuple(y)
print(x)


if 'Apple' in x:
     print("yes")
else:
     print("no")
