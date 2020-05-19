"""Difference between shallow and deep copying of objects in Python."""

import copy

my_list = [1, 2, 3]
my_other_list = my_list
print("\nmy_other_list = my_list...")
print("my_list is at", id(my_list))
print("my_other_list is also at", id(my_other_list))
my_list[0] = 99
print("my_list[0] = 99 so my_other_list =", my_other_list)

my_list_copy = copy.copy(my_list)
print("\nmy_list_copy = copy.copy(my_list) -> creates a new list - same as my_list.copy() list method...")
print("my_list and my_list_copy at different addresses")
print("my_list is at", id(my_list))
print("my_list_copy is at", id(my_list_copy))

print("now modifying elements in my_list does not affect my_list_copy and vice versa")
my_list[0] = 10
my_list_copy.append(4)
print("my_list[0] = 10")
print("my_list_copy.append(4)")
print("my_list =", my_list)
print("my_list_copy =", my_list_copy)

# https://docs.python.org/2/library/copy.html
print("\nbut what about compound objects - 'objects that contain other objects, like lists or class instances'...")
my_compound_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("my_compound_list =", my_compound_list)
my_compound_list_copy = copy.copy(my_compound_list)
print("my_compound_list_copy = copy.copy(my_compound_list) performs a **shallow** copy")
print("....so the lists have different addresses")
print("my_compound_list is at", id(my_compound_list))
print("my_compound_list_copy is at", id(my_compound_list_copy))
print("....but the individual elements are bound to the same address")
print("my_compound_list[0] is at", id(my_compound_list[0]))
print("my_compound_list_copy[0] is at", id(my_compound_list_copy[0]))

print("....so changing elements in my_compound_list changes my_compound_list_copy")
my_compound_list[0][0] = 10
print("my_compound_list[0][0] = 10")
print("my_compound_list =", my_compound_list)
print("my_compound_list_copy =", my_compound_list_copy)
print("....but modifying my_compound_list, such as adding elements, does not change my_compound_list_copy")
my_compound_list.append([10, 11, 12])
print("my_compound_list =", my_compound_list)
print("my_compound_list_copy =", my_compound_list_copy)

my_compound_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
my_compound_list_copy = copy.deepcopy(my_compound_list)
print("\nmy_compound_list_copy = copy.deepcopy(my_compound_list) performs a **deep** copy...")
print("....so the lists have different addresses")
print("my_compound_list is at", id(my_compound_list))
print("my_compound_list_copy is at", id(my_compound_list_copy))
print("....and the individual elements are bound to the different addresses")
print("my_compound_list[0] is at", id(my_compound_list[0]))
print("my_compound_list_copy[0] is at", id(my_compound_list_copy[0]))

print("....so changing elements in my_compound_list no longer changes my_compound_list_copy")
my_compound_list[0][0] = 10
print("my_compound_list[0][0] = 10")
print("my_compound_list =", my_compound_list)
print("my_compound_list_copy =", my_compound_list_copy)

print("\ncare needs to be taken when using repetition to create compound objects...")
my_repetition_list = [[1, 2, 3]] * 3
print("my_repetition_list =", my_repetition_list)
print("but repetition is based on shallow copies so odd (unexpected) things happen when you do..")
my_repetition_list[0][0] = 99
print("my_repetition_list[0][0] = 99")
print(my_repetition_list)
