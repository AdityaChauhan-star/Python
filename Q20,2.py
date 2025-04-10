class Distance:
     def __init__(self,km,m):
          self.km=km
          self.m=m
     def distance(self):
          return self.km*1000+self.m
class School(Distance):
     def __init__(self,km,m):
          super().__init__(km,m)
     def display(self):
          print(f"Distance between house and school = {self.distance()}m")
class office(Distance):
     def __init__(self,km,m):
          super().__init__(km,m)
     def display(self):
          print(f"Distance between house and office = {self.distance()}m")
a=School(10,5)
b=office(15,90)
a.display()
b.display()
