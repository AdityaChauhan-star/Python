#Task 1 : Calculator

#  Create a basic calculator that can performbasic arithmetic operations such as
#  addition,subtraction, multiplication, and division.usingfunctions.

import tkinter as tk

window = tk.Tk()
window.geometry('300x150')
window.title("simple calcultor")

tk.Label(window, text="First Number:").grid(row=0, column=0)
n1 = tk.Entry(window, width=20)

tk.Label(window, text="Second Number:").grid(row=1, column=0)
n2 = tk.Entry(window, width=20)

tk.Label(window, text="result =").grid(row=2, column=0)
r = tk.Label(window, bg='white', width=15)  # Remove the comma at the end of this line

def add():
    num1 = n1.get()
    num2 = n2.get()
    s = float(num1) + float(num2)
    r.configure(text=s)

def sub():
    num1 = n1.get()
    num2 = n2.get()
    s = float(num1) - float(num2)
    r.configure(text=s)

def mul():
    num1 = n1.get()
    num2 = n2.get()
    s = float(num1) * float(num2)
    r.configure(text=s)

def div():
    num1 = n1.get()
    num2 = n2.get()
    s = float(num1) / float(num2)
    r.configure(text=s)

bt1 = tk.Button(window, text="+", command=add, width=4).grid(row=0, column=2)
bt2 = tk.Button(window, text="-", command=sub, width=4).grid(row=1, column=2)
bt3 = tk.Button(window, text="*", command=mul, width=4).grid(row=0, column=3)
bt4 = tk.Button(window, text="/", command=div, width=4).grid(row=1, column=3)

n1.grid(row=0, column=1)
n2.grid(row=1, column=1)
r.grid(row=2, column=1)

window.mainloop()
