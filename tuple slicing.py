#Tuple is immutable and written in round brackects or very similar to list
#slicing of tuple is same as list
t=(1,2,3,4,5,6,7,8,9,0)
print(t[0:5])
print(t[2:8])

#traversing 
tuple1=(1,2,3,4)
for t in tuple1:
     print(t)

tuple2=(1,2,3,4)
for i in range(len(tuple1)):
     print(tuple1[i])
#joining tuple
tuple1=(1,2,3,4,5,4,5,6)
tuple2=(0,9,8,7,6,8,)
tuple3=tuple1+tuple2
print(tuple3)
