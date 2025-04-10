import tkinter as tk

def submit_form():
    name = entry_name.get()
    age = entry_age.get()
    email = entry_email.get()
    branch = entry_branch.get()
    
    print("Name:", name)
    print("Age:", age)
    print("Email:", email)
    print("Branch:",branch)
     # Clear the input fields after submission
    #entry_name.delete(0, tk.END)
   # entry_age.delete(0, tk.END)
    #entry_email.delete(0, tk.END)
    #entry_branch.delete(0, tk.END)

window = tk.Tk()
window.title("Student Registration Form")

# Create labels and entry fields for name, age, and email,branch
label_name = tk.Label(window, text="Name:")
label_name.pack()
entry_name = tk.Entry(window)
entry_name.pack()

label_age = tk.Label(window, text="Age:")
label_age.pack()
entry_age = tk.Entry(window)
entry_age.pack()

label_email = tk.Label(window, text="Email:")
label_email.pack()
entry_email = tk.Entry(window)
entry_email.pack()

label_branch = tk.Label(window, text="Branch:")
label_branch.pack()
entry_branch = tk.Entry(window)
entry_branch.pack()

# Create submit button
submit_button = tk.Button(window, text="Submit", command=submit_form)
submit_button.pack()

window.mainloop()
