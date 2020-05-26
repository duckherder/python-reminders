"""Not intended to be a full and complete list just some examples of the more interesting changes."""

import time
import ipaddress                        # New module in Python 3.3
import statistics                       # New module in Python 3.4
import tracemalloc                      # New module in Python 3.4
from functools import reduce            # No longer a builtin function
from contextlib import suppress         # New feature in Python 3.4

# See https://docs.python.org/3/whatsnew/

print("print now a function...")
print("hello world!")                                           # Python 2: print "hello world!"

print("input() now longer evaluates input so input now same as raw_input (deprecated)...")
my_string = input()                                             # PEP 3111 in Python 3.0
print(my_string)

print("new .isascii() attribute for strings...")
my_char = 'c'
print("my_char.isascii() =", my_char.isascii())                 # New in Python 3.7

print("there are no longs any more in Python 3...")
print("type(65536*65536) =", type(65536*65536))                 # Python 2: <type 'long'>
print("ints can be of any size", 65536**32)

print("integer division now result in a float...")
print("type(7/2) =", type(7/2))

print("strings are unicode by default, no u prefix required...")
my_string = "\u018e"


class Bob:                      # no need to use Bob(object) to use new-style class in Python 3
    def __init__(self):
        pass


print("classes are new-style only and type of class can be used to mean the same...")
bob = Bob()
print("instance bob.__class__ =", bob.__class__)
print("type(bob) =", type(bob))     # this would return built-in type 'instance' in Python 2

print("classes are instances of object but also the metaclass 'type'...")
print("type(Bob) =", type(Bob))         # type metaclass is an instance of itself
print("type(type) =", type(type))       # type() is an instance of itself, type returns a new instance of type metaclass
print("Bob.__bases__ =", Bob.__bases__)
print("Bob.__mro__ = ", Bob.__mro__)    # new style allows for method resolution order to be seen

print("range() now returns an iterable range object instead of a list...")
range_object = range(1000)                                                 # better memory footprint
print("type(range_object) =", range_object)
print("...so no more need for xrange")

print("items() and not iteritems()...")                         # PEP 3106
my_dict = {'bob': 1, 'sally': 2}
for k, v in my_dict.items():                                    # Python 2: my_dict.iteritems()...
    print(k, v)                                                 # ...items() is a generator

print("no has_key() dictionary attribute any more...")
try:
    print(my_dict.has_key('bob'))
except AttributeError:
    print("no attribute has_key() any more")
print('bob' in my_dict)

try:
    print("except ValueError, e is no longer supported...")
except ValueError as e:    # rather than "except ValueError, e" which is no longer supported
    pass

with suppress(AttributeError):
    print("use suppress when you wish to pass on certain exceptions...")
    print(my_dict.womble)


print("'with' statement is now a builtin rather than __future__ feature...")
try:
    with open('random.txt', 'r',) as f:
        print("hello!")
except FileNotFoundError:
    pass

try:
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = cmp(a, b)
except NameError:
    print("cmp no longer supported in Python 3...")


# you can implement it yourself if you so wish
def my_cmp(a_value, b_value):
    return (a_value > b_value) - (a_value < b_value)


a = [1, 4, 3]
b = [1, 2, 2]
print("my_cmp(a, b) =", my_cmp(a, b))

# create an immutable bytes object
print("bytes() constructor is different....")
# Python 2: key = ''.join(chr(x) for x in [0x13, ....]) -> str
key = bytes([0x13, 0x00, 0x00, 0x00, 0x08, 0x00])
print(key)

print("iterable unpacking...")                                  # PEP 3132 in Python 3.0
first, second, *rest = ['first', 'second', 'bob', 'sally', 'brian']
print("first =", first)
print("second =", second)
print("rest =", rest)

print("nonlocal keyword...")                                    # PEP 3104


def my_nested_func():
    my_enclosing_variable = 'bob'

    def my_func_in_func_modifier():
        nonlocal my_enclosing_variable
        my_enclosing_variable = 'sally'

    my_func_in_func_modifier()
    print("modified my_enclosing_variable =", my_enclosing_variable)


def my_keyword_only_function(*, keyword_param_1, keyword_param_2):
    print(keyword_param_1, keyword_param_2)


try:
    my_keyword_only_function(3, 'bob')                          # PEP 3102 in Python 3.0
except TypeError:
    print("keyword only arguments...")
    my_keyword_only_function(keyword_param_1=3, keyword_param_2='bob')

print("function hinting...")


def my_type_hinted_function2(name: str) -> bool:                # PEP 3107/484
    return "bob"


try:
    f = open('does_not_exist.txt', 'r')
except FileNotFoundError:
    print("new exception FileNotFoundError...")


class BaseClass:
    def __init__(self):
        print("BaseClass __init__")


class DerivedClass(BaseClass):
    def __init__(self):
        super().__init__()                                      # PEP 3135: no parameter required for super()
        print("DerivedClass __init__")


print("super() requires no parameters...")
my_instance = DerivedClass()

print("next() is now a builtin function...")
my_list_iter = iter([1, 2, 3])                                  # PEP 3114 in Python 3.0
print("next(my_list_iter) =", next(my_list_iter))               # Python 2: my_list_iter.next(), now __next__()

print("f strings...")
my_variable = 'bob'
my_f_string = f"hello {my_variable.capitalize()}"               # PEP 498 in Python 3.6
print(my_f_string)

print("statistics module...")                                   # PEP 450 in Python 3.4
my_list = [3.2, 5.6, 2.1]
print("statistics.mean(my_list) =", statistics.mean(my_list))
print("statistics.stdev(my_list) =", statistics.stdev(my_list))

print("ipaddress module...")                                    # New in Python 3.3
address = ipaddress.ip_address('239.255.255.250')
print("type(address) =", type(address))
print("address.is_multicast =", address.is_multicast)
address = ipaddress.ip_address('2001:db8::')
print("type(address) =", type(address))

print("tracemalloc module...")                                  # PEP 454 in Python 3.4
tracemalloc.start()
trace_malloc_vector = [z for z in range(1000)]
memory_snapshot = tracemalloc.take_snapshot()
stats = memory_snapshot.statistics('lineno')
for stat in stats[:10]:
    print(stat)

print("new time functions for measuring relative time...")
start_time = time.perf_counter()                                # PEP 418 in Python 3.3
print("elapsed time from time.perf_counter() =", time.perf_counter() - start_time)
start_time = time.process_time()
print("elapsed time from time.process_time() =", time.process_time() - start_time)

print("reduce() is no longer builtin function - part of functools...")


def my_reducer(x, y): return x if x < y else y


print(reduce(my_reducer, [5, 3, -1, 4]))
print("@= and @ are new operators introduced in Python 3.5 performing matrix multiplication...")
A = [[1,2], [3,4]]
B = [[10,100], [10, 100]]
try:
    print(A @ B)                                                # PEP 465 in Python 3.5
except TypeError:
    print("but no supported for any built in types...")

print("there are plenty more so see https://docs.python.org/3/whatsnew/ ...")
