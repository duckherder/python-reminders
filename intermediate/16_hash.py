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
a = MyEquivAndHashClass('bob')
b = MyEquivAndHashClass('bob')
print(f"a = {a}")
print(f"b = {b}")
print(f"now equivalent a == b: {a==b}")
_my_dict = {a: True}
print("and can used in a dictionary _my_dict = {a: True}", _my_dict)
print("and updating dictionary with either a or b as the are the same thing")
_my_dict[a] = False
print("_my_dict[a] = False _my_dict becomes ", _my_dict)
_my_dict[b] = True
print("_my_dict[b] = True _my_dict becomes ", _my_dict)

print("\nso what happens to the dictionary if the key changes...")
print("lets change a.name = 'tim'")
a.name = 'tim'
print(f"no longer equivalent a == b: {a==b} as you would expect")
print(_my_dict)
try:
    condition = _my_dict[a]
except KeyError:
    print("however key is now different (different hash) so will not found e.g. condition = _my_dict[a]")
_my_dict[a] = False
print("if you try to update dictionary _my_dict[a] = False new key-pair created")
print(_my_dict)
print("which is slightly weird as we now have two keys for same object id")
print("but ok as we are saying tim and bob are not the same person so use different key")
_my_dict[b] = 'change from bool'
print("updating dictionary _my_dict[b] now create a further third new entry!")
print(_my_dict)

# but you need hash and equivalence to use same information
# else weird stuff will happen
class MyBadEquivAndHashClass:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name+str(self.age))

print("\nso what happens when two objects have different hash computation to equivalence....")
a = MyBadEquivAndHashClass('bob', 15)
b = MyBadEquivAndHashClass('bob', 16)
print(f"a = {a}")
print(f"b = {b}")
print(f"again these are equivalent a == b: {a==b}")
print(f"but what happens in dictionary")
_my_dict = {a: True}
print("and can used in a dictionary _my_dict = {a: True}", _my_dict)
_my_dict[a] = False
print("_my_dict[a] = False _my_dict becomes ", _my_dict)
_my_dict[b] = True
print("_my_dict[b] = True _my_dict becomes ", _my_dict)
print("so this weird as a and b are supposedly equivalent but now 2 keyed items in dictionary")

print("\nso if you want to use a mutable user object as a dictionary key...")
print("\nthen __hash__ and __eq__ should match modifiable entities!")
class MyGoodEquivAndHashClass:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __hash__(self):
        return hash(self.name+str(self.age))

a = MyGoodEquivAndHashClass('bob', 15)
b = MyGoodEquivAndHashClass('bob', 15)
a == b
print(f"a = {a}")
print(f"b = {b}")
print(f"again these are equivalent a == b: {a==b}")
_my_dict = {a: 0}
_my_dict[a] = 1
_my_dict[b] = 2
print("can use a or b to update dictionary, _my_dict = ", _my_dict)
print("setting a.age to 16")
a.age = 16
_my_dict[a] = 3
print("a is changed so new key, _my_dict = ", _my_dict)
print("_my_dict[a] = ", _my_dict[a])
a.age = 15
print("a change is reversed changed _my_dict[a] = ", _my_dict[a])
print("so in this example we are saying 15 year old bob is treated different to 16 year bob")

# dictionaries work by using hashing/has tables
# the key is converted to a hash code
print("\na quick reminder on how hashing works...")
print("...as fundamental to Python as nearly everything under hood is a dict...")
print("if we have 100000 telephone number records is a linear array")
print("and we want to find the record for a particular number")
print("we can linearly search. if first in array great, if last")
print("then search time will be long")
print("a solution is to apply a function to the number/string whatever, a hashing function")
print("the resulting value, an integer, indexes into a hash table")
print("a hash table has a number or rows, or buckets")
print("the bucket index is usually computed as hash_value % number buckets")
print("each bucket may have a small number of phone records in it")
print("so when i want to do a look-up I hash the number (key) which gives me a bucket")
print("i then go along row (chain) to find record, or pointer to record, associated with my hash value")
print("if there is a collision - two keys generate same hash value")
print("then need to compare actual numbers to find right record")
print("so choice of hash function is important to spread records evenly")
print("over all the buckets and also to avoid collisions")
