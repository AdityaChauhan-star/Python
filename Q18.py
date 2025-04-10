class point:
     def __init__(self,x,y):
          self.x=x
          self.y=y
class location(point):
     def __init__(self,x,y):
          super().__init__(x,y)
     def Location(self):
          print(f"Reflection on y axis = ({-self.x},{self.y})")
     def destination(self):
          print(f"Destination from origin = {((self.x)**2 +(self.y)**2)**0.5}")        
p=location(3,4)
p.Location()
p.destination()
