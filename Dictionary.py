#Dictionaries are written within curly brackets,they have key and values
dict1={"Brand":"Suzuki","Model":"Dzire","year":2020}
print(dict1)

#accessing elements
print("accessing elements=")

x=dict1["Model"]
print(x)

y=dict1.get("Model")
print(y)

#Loop through a dictionary
print("Loop through a dictionary=")

for x in dict1:
     print(x)

for x in dict1:
     print(dict1[x])
