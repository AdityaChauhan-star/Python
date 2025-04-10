#values()- it return values of dict
dict1={"Brand":"Suzuki","Model":"Dzire","year":2020}
x=dict1.values()
print(x)

#items()- it return the values along with keys
x,y,z=dict1.items()
print(x,y,z)

for x,y in dict1.items():
     print(x,y)

#pop()- remove the element with specified key name
dict1.pop("Model")
print(dict1)

#popitem()- to remove the last element of dict

dict1.popitem()
print(dict1)

#del()- remove the element with specified key name
del.dict1("Brand")
print(dict1)
