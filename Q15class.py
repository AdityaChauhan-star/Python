class ABC:
     def __init__(self,var):
          self.var=var
     def __str__(self):
          return "value is "+str(self.var)
obj=ABC(100)
print(obj)
print("Getting attribute",getattr(obj,'var'))
print("checking for attribte",hasattr(obj,'var'))
setattr(obj,'var',200)
print("After setting value",obj.var)
setattr(obj,'nvar',500)
print("after setting new attribute",obj.nvar)
delattr(obj,'var')
print("After deleting attribute",obj.nvar)
