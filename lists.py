# Lists: ordered, mutable, allows duplicate elements
mylist = ["potato ", "banana", "cherry", "apple"]
print(mylist)

mylist2 = [5, True, 7, 33, 343.53, "apple"]
print(mylist2[2])

mylist.insert(0, "lemon")
for i in mylist:
    if i == "banana":
        print("yes")
    else:
        print("no")
