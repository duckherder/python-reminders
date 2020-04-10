import pickle
import json

print("\nbytes are immutable sequence of integers in range 0 to 255")
my_string = 'hello you'
my_bytes = bytes(my_string, encoding='utf-8')
print("my_bytes type:", type(my_bytes))
print("my_bytes:", my_bytes)
try:
    my_bytes[0] = ord('d')
except TypeError:
    print("bytes are immutable so can not change values")

print("we can convert an integer list into a bytes as well provided 0 <= x <256")
my_bytes = bytes([0, 2, 3, 255])
print("my_bytes type:", type(my_bytes))
print("my_bytes:", my_bytes)

try:
    my_bytes = bytes([0, 2, 3, 256])
except ValueError:
    print("integer values in list must 0 <= x < 256!!")

print("\nbytearray are a mutable sequence of integers in range 0 to 255")
my_string = 'hello you'
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

print("\nwe can use pickle to snapshot and save any object")
print("default pickle protocol =", pickle.DEFAULT_PROTOCOL)
print("we can serialize an object to a bytes object using pickle.dumps()")
# you can use dump() to write to file
my_pickled_object_bytes = pickle.dumps(my_object)
print("pickled object type =", type(my_pickled_object_bytes))
print("pickled object:", my_pickled_object_bytes)

print("we can deserialize a pickled object using pickle.loads()")
# you can use load() to read from file
my_unpickled_object = pickle.loads(my_pickled_object_bytes)
print("value should match original object", my_unpickled_object.value)

print("\nwe can use json to convert dictionaries to readable strings and back again")
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
