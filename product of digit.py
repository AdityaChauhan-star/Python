i=int(input("enter number"))
prod=1
while (i>0):
    prod=prod*(i%10)
    i=i//10
print('PRODUCT OF DIGIT=',prod)
