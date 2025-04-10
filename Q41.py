from tkinter import *
root=Tk()
def disappear():
     l.destroy()
root.title("aditya chauhan")
l=Label(text="This is a Label")
b=Button(text="Click Me", bg='Blue', activebackground='red', command=disappear)
b.bind('<Enter>', func=lambda e :b.config(bg="pink"))
b.bind('<Leave>', func=lambda e :b.config(bg="orange"))
b.pack()
l.pack()
mainloop()
