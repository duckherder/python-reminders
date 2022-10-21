"""Hashing and equivalence are tightly"""

# first a reminder about mutable objects and equivalence
from typing import ValuesView


a = "my string"
b = "my string"

if a is b:
    print("\nimmutable objects such as strings are same object (a is b).........")
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"id(a) ={id(a)} ")
    print(f"id(b) ={id(b)} ")
    print("immutable objects such as strings are also equivalent")
    print(f"a == b: {a==b}")

a = [1,2,3]
b = [1,2,3]

if a is not b:
    print("\nin built mutual objects such as lists with same value are different objects (a is not b)......")
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"id(a) ={id(a)} ")
    print(f"id(b) ={id(b)} ")
    print("in built mutual objects such as lists are equivalent")
    print(f"a == b: {a==b}")

class MyClass:

    def __init__(self, name):
        self.name = name

a = MyClass("my string")
b = MyClass("my string")

if a is not b:
    print("\nmutable user objects are not the same object (a is not b)......")
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"id(a) ={id(a)} ")
    print(f"id(b) ={id(b)} ")
    print("mutuable user objects with __eq__ are not equivalent")
    print(f"a == b: {a==b}")

class MyEquivClass:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

a = MyEquivClass("my string")
b = MyEquivClass("my string")

print("\nmutable user objects that implement __eq__ not the same but can be equivalent......")
print(f"a = {a}")
print(f"b = {b}")
print(f"a == b: {a==b}")

# these different types are also different in terms of hashability
print("\nhashing a string...")
print("hash('my string'): ", hash('my string'))
print("'my string'.__hash__(): ", 'my string'.__hash__())

# if an object is hashable it means it can be used a key in a dictionary
print("\nimmutable in built objects can be used in a dictionary....")
my_dict = {'my string': 45, 'my other string': True}
print(my_dict)

# in built mutable objects are not hashable
try:
    hash([1,2,3])
except TypeError:
    print("\ninbuilt mutable objects are not hashable e.g. hash([1,2,3])....")

try:
    my_dict = {[1,2,3]: True}
except:
    print("as such, inbuilt mutable objects can not be keys e.g. {[1,2,3]: True}")

print("\nwhat about user defined mutable classes....")
hash(MyClass)
hash(MyEquivClass)
m_dict = {MyEquivClass, 'hello class'}
print("..classes are hashable! e.g. {MyEquivClass, 'hello class'} even if they only implement __eq__")

print("\ndefault user defined mutable class instances are also hashable....")
print("hash(MyClass('my string') =", hash(MyClass('my string')))
print("this is because the hash is based on the id")

try:
    hash(MyEquivClass('my string'))
except TypeError:
    print("\nbut user objects that only implement __eq__ are not e.g. hash(MyEquivClass('my string'))....")

class MyEquivAndHashClass:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

print("\n if __eq__ and __hash__ are implemented mutable class instances are also hashable....")
print("hash(MyEquivAndHashClass('my string') =", hash(MyEquivAndHashClass('my string')))
_my_dict = {MyEquivAndHashClass('my string'): True}
print("and used in a dictionary ", _my_dict)

# but you need hash and equivalence to use same information
# else weird stuff will happen


# dictionaries work by using hashing/has tables
# the key is converted to a hash code