# Dictionary: Key-Value pairs, Unordered, Mutable
mydict = {"name": "Kevin", "age": 32, "city": "Wimbledon"}
print(mydict)

mydict2 = dict(name="Mary", age="27")
print(mydict2)

value = mydict["name"]
print(value)

mydict2["email"] = "mary@emails.com"

mydict.update(mydict2)
print(mydict)
