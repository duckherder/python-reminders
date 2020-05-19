"""Various types of mutable and immutable containers supported by Python."""

print("\nlists...")
# you create a simple list of the same type
my_simple_list = [0, 1, 2]              # list of integers
print(my_simple_list)

# you can create lists with different types
my_mixed_list = [0, 'bob', 3.0, 4 + 5j]
print(my_mixed_list)

# lists can contain lists
my_nested_list = [[0, 1, 2], ['bob', 0], 4.0]
print(my_nested_list)

# use repetition or generators to create big lists
print("can create lists using repetition e.g. vector = [0] * 100")
vector = [0] * 100
print("vector length = %d" % len(vector))
print("..or [1, 2, 3] * 3")
print([1, 2, 3] * 3)

print("can create lists using a list comprehension")
bob_list = ["bob" for i in range(4)]
print(bob_list)

print("can concatenate lists using += operator")
my_simple_list += my_mixed_list
print(my_simple_list)

# you can access any member using a zero indexed integer
print("list access using [n]")
print(my_mixed_list[0])
print(my_mixed_list[3])

print("lists are mutable so you change values in the list")
my_mixed_list[0] = 'sam'
my_mixed_list[1] = 19
print(my_mixed_list)

print("you can append new members to the end of a list")
my_simple_list.append(3)
print(my_simple_list)

print("you can delete a specific element from a list")
del my_simple_list[1]
print(my_simple_list)

print("or remove the first matching object in the list")
my_numbers = [1, 1, 1, 2, 2]
print(my_numbers)
my_numbers.remove(1)
print(my_numbers)

print("get the number of objects in a list using count() method")
print(my_numbers.count(2))
print(my_numbers.count('sally'))

print("you can find the first matching objects using index() method")
print(my_numbers.index(2))
try:
    print(my_numbers.index('sally'))
except ValueError:
    print("..which will raise a ValueError exception if not in the list")

my_list = [2, 1, 4, 3]
print("you can sort a list using sorted() built in function")
print("my_list = ", my_list)
print("sorted list =", sorted(my_list))
print("reverse sorted list =", sorted(my_list, reverse=True))

print("create an empty list")
my_empty_list = []
# using list() directly will create an empty list it is slower (apparently)...
my_other_empty_list = list()
# ...and really this is for casting other iterables to a list

print("you can see all available list functions and attributes using dir()")
print(dir(list))

print("\ntuples...")
my_tuple = ("a", "b", "c", 1, 2, "bob", 9.0)
print("can be accessed just like lists")
print(my_tuple)

# tuples can be created without parentheses as comma separated
# note if only one element you must use a comma e.g. .. = "w",
my_comma_tuple = "w", 34, "how", 8.76
print(my_comma_tuple)                           # ...or ("w",)
print(type(my_comma_tuple))

# tuples are immutable
print("difference is that tuples are immutable")
try:
    my_tuple[0] = "d"
except TypeError:
    print("...and will raise an exception if you try to modify them!")

print("concatenation is possible but only if you are creating a new tuple")
my_cat_tuple = my_tuple + my_comma_tuple + (34,)
print(my_cat_tuple)
print(len(my_cat_tuple))

# but many of the functions that modify a list are not valid for a tuple
print("you can see all available tuple functions and attributes using dir()")
print(dir(tuple))

print("\ndictionaries...")
# dictionaries are in key:value pairs
# you can use any type for both keys and values
print("use key:value pairs. keys can be a string, number or tuple. value can be of any type")
my_dict = {1: 2, 2: 6.0, 'bob': 4, (56, 78): 'odd'}
print(my_dict)
print(type(my_dict))

print("dicts are unordered but can be accessed using [key]")
print(my_dict[1])
print(my_dict[2])
print(my_dict['bob'])
try:
    print(my_dict['tim'])
except KeyError:
    print("invalid keys will raise an exception")

print("they are mutable so you can modify and add to a dictionary")
my_dict[2] = 'new_value'
my_dict['new_key'] = 2+5j
print(my_dict)

print("you can see all available list functions and attributes using dir()")
print(dir(dict))
print("some of the more useful are")
print("keys(): get keys from dictionary e.g. ", my_dict.keys())
print("get(): get key value from dictionary e.g. %d" % my_dict.get('bob'))
print("items(): get list of tuples from dictionary e.g. ", my_dict.items())

print("\nsets...")
print("sets are unordered and un-indexed so no [] access")
bob = {6, 7, 8}
dick = {8, 9}
print("bob =", bob)
print("dick =", dick)
print("they contain only one version of an object - duplicates are removed")
animals = {"dog", "cat", "dog"}
print("animals =", animals)
print("you can do many of the basic operations you can perform on a normal mathematical set")
print("difference between bob and dick = ", bob-dick)
print("difference using difference() = ", bob.difference(dick))
print("you can see all available list functions and attributes using dir()")
print(dir(set))
bob.add(5)
print("adding to bob: ", bob)
print("intersection of bob and dick: ", bob.intersection(dick))
print("intersection using '&' operator: ", bob & dick)
print("union of bob and dick: ", bob.union(dick))
print("union using '|' operator: ", bob | dick)
