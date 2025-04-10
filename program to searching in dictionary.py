studentsDB={}
#ask input from user and 'q' to exit
while True :
     line=input("please input the ID and name seprated by comma or q to exit")
     if line=="q":
          break
     id,name=line.split(',')
     studentsDB.update({id:name})
#output
for x,y in studentsDB.items():
     print(x,y)
#searching a key
key=input("enter id to search")
if key in studentsDB:
     print("key=",key,"value=",studentsDB[key])
else:
     print("key is not found")
