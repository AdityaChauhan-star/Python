#this function is used to count the freqency of given object present in list
a=['ram','shyam','ram','gita','ram']
b=a.count('ram')
print("frequency=",b)


a=[]
for i in range(10):
     x=input("enter item to add in list")
     a.append(x)
x=input("enter value whose frequency you want")
b=a.count(x)
print("frequency of",x,"is =",b)
     
