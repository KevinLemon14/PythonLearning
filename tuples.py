# Tuple: ordered, immutable, allows duplicate elements
mytuple = ("Max", 28, "Boston")
print(mytuple)

item = mytuple[0]
print(item)

appletuple = ("a", "p", "p", "l", "e")

print(appletuple.index("l"))


unpacktuple = "Max", 28, "Boston"

name, age, city = unpacktuple

print(name)
print(age)
