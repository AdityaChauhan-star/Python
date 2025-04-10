class student:
     def __init__(self,marks):
          self.name=input("Enter Name")
          self.age=int(input("Enter your age"))
     def display_info(self):
          print(f"student name={self.name},student Age = {self.age}")
class Marks(student):
     def __init__(self):
          self.marks1=int(input("Enter marks in first subject:"))
          self.marks2=int(input("Enter marks in second subject:"))
          self.marks3=int(input("Enter marks in third subject:"))
          super().__init__([self.marks1,self.marks2,self.marks3])


     def display_marks(self):
          print(f"marks1 ={self.marks1},marks2 ={self.marks2},marks3 ={self.marks3}")

class Result(Marks):
     def __init__(self,total):
          self.t=total
          super().__init__()
     def display_result(self):
          print("Result=",((self.marks1+self.marks2+self.marks3)/self.t)*100)

r=Result(300)
r.display_info()
r.display_marks()
r.display_result()
