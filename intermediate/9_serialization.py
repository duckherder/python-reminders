"""Serialization is the process of converting objects, for example, into a character stream."""

import pickle
import json

print("\nbytes are immutable sequence of integers in range 0 to 255...")
my_string = 'hello you'
print("my_string =", my_string)
my_bytes = bytes(my_string, encoding='utf-8')       # note encoding style
print("my_bytes type:", type(my_bytes))
print("my_bytes:", my_bytes)
try:
    my_bytes[0] = ord('d')
except TypeError:
    print("bytes are immutable so you can not change any values")

print("\nwe can convert an integer list into a bytes as well provided 0 <= x <256...")
my_integer_list = [0, 2, 3, 255]
print("my_integer_list =", my_integer_list)
my_bytes = bytes(my_integer_list)
print("my_bytes type:", type(my_bytes))
print("my_bytes:", my_bytes)

my_integer_list = [0, 2, 3, 256]
print("my_integer_list =", my_integer_list)
try:
    my_bytes = bytes(my_integer_list)
except ValueError:
    print("ValueError exception raised: integer values in list must be 0 <= x < 256!!")

print("\nbytearray is a mutable sequence of integers in range 0 to 255...")
my_string = 'hello you'
print("my_string =", my_string)
my_bytes = bytearray(my_string, encoding='utf-8')
print("my_bytes type:", type(my_bytes))
print("my_bytes:", my_bytes)
my_bytes[0] = ord('d')
print("my_bytes modified:", my_bytes)


class MyClass:
    def __init__(self, initial_value):
        self.string = 'hello world'
        self.value = initial_value

    def increment(self):
        self.value += 1


my_object = MyClass(5)
my_object.increment()           # self.value becomes 6

print("\nwe can use the pickle module to snapshot and save any object...")
print("default pickle protocol =", pickle.DEFAULT_PROTOCOL)
print("my_object.value =", my_object.value)
print("we can serialize an object to a bytes object using pickle.dumps()")
# you can use dump() to serialize and write direct to a file
my_pickled_object_bytes = pickle.dumps(my_object)
print("pickled object type =", type(my_pickled_object_bytes))
print("pickled object:", my_pickled_object_bytes)

print("we can deserialize a pickled object using pickle.loads()")
# you can use load() to read from file
my_unpickled_object = pickle.loads(my_pickled_object_bytes)
print("value in un-pickled object should match original object:", my_unpickled_object.value)

print("\nwe can use json to convert dictionaries to readable strings and back again...")
my_dictionary = {
    'name': 'bob',
    'age': 19,
    'scores': [3, 6, 4, 5, 7],
    'references':
        {
            'name': 'sally',
            'reference': 'terrible student'
    }
}
print(my_dictionary)
my_json_string = json.dumps(my_dictionary, indent=4)
print("my_json_string is of type", type(my_json_string))
print("my_json_string:", my_json_string)

my_recovered_dictionary = json.loads(my_json_string)
if my_recovered_dictionary == my_dictionary:
    print("recovered object from JSON matches original dictionary")
