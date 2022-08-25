# Strings: ordered, immutable, text representation
my_string = """Hello

World"""
print(my_string)

my_char = my_string[5]
print(my_char)

my_sub = my_string[::-1]
print(my_sub)

name = "Kevin"
greeting = "Hello"

sentence = greeting + " " + name
print(sentence)

for i in name:
    print(i)


# Whitespace, Replacing, Finding
whitestring = "        Hey There Hello Hi     "
whitestring = whitestring.strip()
print(whitestring)

print(whitestring.upper())
print(whitestring.find("ell"))
print(whitestring.replace("Hi", "Howdy"))


# Splitting and Joining
string_convert = "how,are,you,doing"
my_list = string_convert.split(",")
print(my_list)
new_string = " ".join(my_list)
print(new_string)

# %, .format(), f-Strings

var = "Tom"
the_string = "the variable is %s" % var
print(the_string)


myname = "Kevin"
my_new_string = "the variable is {}".format(myname)
print(my_new_string)


var1 = 124
var2 = 3.12435315
fstring = f"the first variable is {var1} and the second is {var2*2}"
print(fstring)
