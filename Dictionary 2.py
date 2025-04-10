#change values in dict
dict1={"Brand":"Suzuki","Model":"Dzire","year":2020}
dict1["year"]=2018
print(dict1)

#check a key exists in dict or not
if "year" in dict1:
     print("yes,key is present")
else:
     print("no,key does not exist")

#adding new element in dict
dict1["color"]="white"
print(dict1)

