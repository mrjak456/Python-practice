# Python List
#----------------

# an empty list
my_list = []

# list of integers
my_list = [1, 2, 3, 4]

#list with mixed data types

my_list = [1,"hello", 2.5, True]

# Accessing a list using index [] operator

my_list = [1,"hello", 2.5, True]
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])

# Negative indexing
print("--------The below is output of negative indexing")
my_list = [1,"hello", 2.5, True]
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])
print(my_list[-4])

# Nested list
print("-------Acessing elements from nested list")
n_list = ["Happy", [2,0,1,5]]
print(n_list[0])
print(n_list[1])
print(n_list[1][0])
print(n_list[1][1])
print(n_list[1][2])
print(n_list[1][3])

# Slicing a list using the slicing operator ":" colon
print("----Slicing the elements using slicing operator : ")
my_list = ['p','r','o','g','r','a','m','i','z']
print(my_list[2:7])
print(my_list[:])
print(my_list[:7])
print(my_list[1:])

# Examples to change values to a list
print("-----Examples to change the values to a list")
odd = [2, 4, 6, 8]
odd[0] = 1
print(odd)

odd[1:] = [3, 5, 7]
print(odd)

# concatenation using '+' operator
print("---concatenating 2 lists")
odd = [1,3,5,7]
even = [2,4,6,8]
numbers = odd + even
print(numbers)

# using * operator
print(["sunday"]*7)

# append() method:
# using append() method, we can add 1 item to a list
print("----append method")
odd = [1,3,5]
odd.append(7)
print(odd)

# extend() method:
# using extend method, we can add multiple items to a list
print("------extend method")
odd = [1, 3, 5, 7]
odd.extend([9, 11, 13, 15])
print(odd)

# insert() method
# we can insert an item at the desired location
print("----inserting an item in the desired location")
odd = [2,4,6,10,12]
odd.insert(3,8)
print(odd)

# del keyword
# we can delete one or more items from a list using the keyword del.
# we can even delete the entire list also

my_list = ['p','r','o','g','r','a','m']
print(my_list)
del my_list[0]
del my_list[2]
print(my_list)
my_list = ['p','r','o','g','r','a','m']
del my_list[2:4]
print(my_list)
my_list = ['p','r','o','g','r','a','m']
del my_list
# print(my_list)  # it prints a name error as the list is already deleted

# remove() method
# remove method is used to remove the specified item from the list
my_list = ['p','r','o','g','r','a','m']
my_list.remove('p')
print(my_list)
my_list.remove('m')
print(my_list)

# pop() method
# pop method is used to remove the item at the specified index
# pop method removes and returns the last item if the index is ot specified
my_list = ['p','r','o','g','r','a','m']
my_list.pop(0)
print(my_list)
print(my_list.pop())
print(my_list)

# clear() method
# clear method is used to empty a list
my_list = ['p','r','o','g','r','a','m']
my_list.clear()
print(my_list)

# index() method
# index method returns the index of the first matched item

my_list = ['p','r','o','g','r','a','m']
print(my_list.index("r"))

# count() method
# count method returns the count of the number of items passed as an argument

my_list = ['p','r','o','g','r','a','m']
print(my_list.count("r"))

# sort() method
# sort method sorts the items in a list in ascending order
my_list = ['p','r','o','g','r','a','m']
my_list.sort()
print(my_list)

# reverse() method
# reverse method reverses the order of items
my_list = ['p','r','o','g','r','a','m']
my_list.reverse()
print(my_list)

# copy() method
# copy method returns a shallow copy of the list.

old_list = ['p','r','o','g','r','a','m']
new_list = old_list.copy()
print(new_list)

# The problem in copying lists using the "=" operator is, if we modify new_list, old_list will also be modified.Because the new list is referencing or pointing to the same old_list object.
new_list.append('s')
print(new_list)
print(old_list)
