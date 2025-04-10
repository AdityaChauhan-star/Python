n=int(input("enter number to check armstrong or not"))
i=n
count=0
while (i>0):
    count=count+1
    i=i//10
sum=0
i=n
while (i>0):
    digit=i%10
    x=1
    pro=1
    while (x<=count):
        pro=pro*digit
        x=x+1
    sum=sum+pro
    i=i//10
if (sum==n):
    print("number is armstrong")
else:
    print("not armstrong")
