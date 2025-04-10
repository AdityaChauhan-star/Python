#clear()- to delete all the values of dict not keys.so,the empty dict exist
dict1={"Brand":"Suzuki","Model":"Dzire","year":2020}
dict1.clear()
print(dict1)

#copy()- to copy the dictionary
dict={"Brand":"Suzuki","Model":"Dzire","year":2020}
x=dict.copy()
print(x)

#formkeys()- to form dictionary with specified keys and values
x=("first key","second key","third key")
y=0
dict2=dict.fromkeys(x,y)
print(dict2)

#setdefault()- to insert the key if not exist or return the value
dict4={"Brand":"Suzuki","Model":"Dzire","year":2020}
x=dict4.setdefault("brand""tata")
print(x)

dict=dict.setdefault("place""new delhi")
print(dict)

#update()- to insert the specified item in dict
dict2={"Brand":"Suzuki","Model":"Dzire","year":2020}
dict2.update({"location":"saket"})
print(dict2)













