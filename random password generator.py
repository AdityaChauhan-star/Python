#                                    TASK - 3

#                               Password Generator

#   A password generator is a useful tool that generates strong and random passwords
#   for users. This project aims to create apassword generator application using
#   Python, allowing users tospecify the length and complexity of the password.





import random
import string

print ('Welcome to password generator')
n = int(input('How many numbers do you want ? '))
l = int(input("How many letters do you want ? "))
c = int(input("How many capital letters do you want ? "))
s = int(input('How many symbols do you want to have in your password ? '))

letters = random.choices(string.ascii_lowercase, k = l)
cap = random.choices(string.ascii_uppercase, k = c)
r = random.choices(range(0, 10), k = n)
sym = random.choices(string.punctuation, k = s)

p = (letters + r + sym + cap)
random.shuffle(p)
print("your password is")

for item in p:
    print (item, end = '')
