"this is a string"
'This is also a string'

#title() method
# This method returns the string where each word begins with a capital letter

name = "ada lovelace"
print(name.title())

#lower() method
# This method returns the string in lower case

name = "Ada Lovelace"
print(name.lower())

#upper() method
#This method returns the string in upper case

name = "Ada lovelace"
print(name.upper())

# Use \n to print the string in new line
print("Languages:\nPython\nJavaScrpt")

# use \t to print the string with 8 whitespaces
print("Languages:\tPython\tJavaScript")
print("Languages:\n\tPython\n\tJavaScript")

# strip() method
#This method is used to trim the string whitespaces from left and right sides.

fav_language = " Python "
print(fav_language.strip())

#lstrip() method
#This method is used to trim the left side whitespaces only
fav_language = " Python "
print(fav_language.lstrip())

#rstrip() method
#This method is used to trim the right side whitespaces only
fav_language = " Python "
print(fav_language.rstrip())

# use + operator to concatenate 2 strings

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

#Accessing characters from a string (slicing)

a = "Python String"
print(a[0])
print(a[1])
print(a[-1])
print(a[-2])
print(a[0:13])
print(a[ : ])
print(a[1: ])
print(a[ : 9])

######## Python strings are immutable. So, they wont support item assignment. 

'''a = "Python"
a[0] = "x"
'''
# we can create a new string by concatenating a new first letter
a = "Python"
b = "x" + a[1: ]
print(b)


# using * operator in strings

a = "Python"
b = "<" + a*2 + ">"

print(b)

# len() method
# use len method to get the length of the string

a= "Python"
print(len(a))

## Traverse a string with while loop

a = "STRING"
i = 0

while i < len(a):
    c = a[i]
    print(c)
    i = i+1

## Traverse a string with for loop

a = "Python"
i = 0

for i in range(0,len(a)):
    b = a[i]
    print(b)

### method1 to reverse a string

txt = "Hello world"
print(txt[::-1])

## method 2 to reverse a string, using for loop

txt = "Hello Python"
newtxt = ""

for i in txt:
    newtxt = i + newtxt
print(newtxt)


# capitalize() method
# capitalize method is used to return the string with first letter as upper case

name = "inida is my country"
print(name.capitalize())


# casefold() method
# casefold method is used to return the string in lower case.

name = "Hello, And Welcome To My World"
print(name.casefold())

# count() method
# count method is used to return the number of times the substring appears in the string.

txt = "I love apples, apples are my favourite fruit"
print(txt.count("apples"))

# endswith() method
# endswith method returns true if the string ends with the specified value, otherwise False

txt = "Hello, welcome to my world!"
print(txt.endswith("my world!"))

# find() method
# find method returns the position of first occurence of the specified substring. If the string is not in the string, it reurns -1
# find and index methods perform the same, but index method returns error if the specified string is not present.

txt = "Hello world, welcome to my world!"
print(txt.find("world"))
print(txt.find("hai"))

# index() method
'''txt = "Hello world, welcome to my world!"
print(txt.index("world"))
print(txt.index("hai"))
'''
# isalnum() method
# isalnum method returns True if all the characters in the string are alpha numeric

txt = "pythonprogramming123"
print(txt.isalnum())

txt = "python programming"
print(txt.isalnum())

# isalpha() method
# isalpha method returns True if the characters in the string are alphabets
txt = "python"
print(txt.isalpha())

txt1 = "this is python"
print(txt.isalpha())

# isdecimal() method
# isdecimal method returns true if the characters in the string are decimals
txt = "123"
print(txt.isdecimal())

# islower() method
# islower method returns true if the string is in lower case

txt = "This is String"
print(txt.islower())

# isupper() method
# isupper method returns True if the string is in upper case

txt = "PYTHON"
print(txt.isupper())

# startswith() method
# startswith method returns True if the string started with specified value

txt = "This is python!"
print(txt.startswith("This"))

# join() method
# join method joins the elements of an iterable and returns a string. Here the iterable may be a list/set/tuple or a dictionary.

list1 = ["This", "is", "Python", "Program"]
x = "#".join(list1)
print(x)

# partition() method
# partition method splits the string and returns a tuple

txt = "I could eat bananas all day"
print(txt.partition("bananas"))

# replace() method
# replace method returns a new string where the specified value is replaced with the specified string

txt = "I like apples, and I eat apples"
print(txt.replace("apples","bananas"))

# zfill()
# zfill method add zeros at the begining of the string until it reached specified length

txt = "Python"
print(txt.zfill(10))
