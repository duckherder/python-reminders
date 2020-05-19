"""Packing and unpacking and variable length function arguments."""

a = ('a', 'b', 'c')         # packing a tuple
(aa, bb, cc) = a            # unpacking a tuple

print("\nunpacking...")
my_unpacked_string_list = [*'hello']
print("my_unpacked_string_list = [*'hello'] =", my_unpacked_string_list)
my_unpacked_tuple_list = [*('a', 1, 3.4)]
print("my_unpacked_tuple_list = [*('a', 1, 3.4)] =", my_unpacked_tuple_list)
my_unpacked_list_list = [*['a', 1, 3.4]]
print("my_unpacked_list_list = [*['a', 1, 3.4]] =", my_unpacked_list_list)

*my_unpacked_tuple_list, = ('a', 1, 3.4)                    # unpacks to a list
print("my_unpacked_tuple_list =", my_unpacked_tuple_list)

my_string = 'hello'
first, second, *rest = my_string                            # from PEP 3132
print("my_string =", my_string)
print("first =", first)
print("second =", second)
print("rest =", rest)

my_tuple = (1, 'bob', 3, 3.5, 'fred')
first, second, *rest = my_tuple
print("my_tuple =", my_tuple)
print("first =", first)
print("second =", second)
print("rest =", rest)


def my_function(param1, param2=None):
    print("in my_function(param1, param2)")
    print("param1 =", param1)
    print("param2 =", param2)


print("\ncalling my_function by unpacking a tuple with * operator....")
arguments = (1, 'bob')
print("arguments =", arguments)         # will print the tuple
# this expands to print("*arguments =", 1, 'bob') in print function
print("*arguments =", *arguments)
print("pass tuple as argument then single tuple will be passed")
my_function(arguments)
print("if we unpack we won't send a single tuple parameter, rather an int, str")
my_function(*arguments)

print("\ncalling my_function using parameter names by unpacking a dictionary with ** operator...")
# what we want to send named arguments -> can't do this...
arguments = ('param2 = 1', 'param1 = 2')
print("arguments =", arguments, "(this won't work)")
# ..we'll just pass two strings
my_function(*arguments)
arguments = {'param2': 1, 'param1': 2}              # keywords must be strings
print("arguments =", arguments)
print("use a dictionary and **operator")
my_function(**arguments)


def argument_function(*args):
    print("number of arguments =", len(args))
    # always a tuple, even if just passing a single integer
    print("type(args) =", type(args))
    print(args)


print("\ncalling a function with *args parameter...")
argument_function("bob", "sue", "dave")
# argument_function will get a tuple containing a list
argument_function([3.4, 1, 'temp'])
argument_function(1)
# will unpack arguments, then pack into args, then unpacked
argument_function(*arguments)
try:
    argument_function(bob=1, daisy=2)
except TypeError:
    print("argument_function has no support for named parameters")


def keyword_function(**named_args):                             # normally this would be called kwargs by convention
    print("number of named arguments =", len(named_args))
    print("type(named_args) =", type(named_args))
    # we'll get a dictionary instead of a tuple
    print(named_args)


print("\ncalling a function with **named_args parameter...")
keyword_function(bob=1, daisy=2)
keyword_arguments = {'daisy': 2, 'bob': 1}
try:
    # not named so not supported
    keyword_function(keyword_arguments)
except TypeError:
    print("keyword_function has no support for unnamed parameters")
keyword_function(**keyword_arguments)               # ..but we can do this


# kwargs is the more usual variable name
def args_and_kwargs(*args, **kwargs):
    print("in function args_and_kwargs")
    print("number of arguments =", len(args))
    # always a tuple, even if just passing a single integer
    print("type(args) =", type(args))
    print(args)
    print("number of named arguments =", len(kwargs))
    print("type(named_args) =", type(kwargs))
    # we'll get a dictionary instead of a tuple
    print(kwargs)


print("\ncalling a function with *args and **kwargs parameters...")
args_and_kwargs(1, 2, [7, 'bob'])
args_and_kwargs(mary=1, donald=2, sally=[7, 'bob'])
args_and_kwargs(1, 2, sally=[7, 'bob'])

print("\nnote that the dictionary unpacking can also be used to merge dictionaries...")
a = {'bob': 1, 'tom': 3, 'rodney': 5}
b = {'sally': 5, 'susan': 7, 'amelia': 0}
merged_dictionary = {**a, **b}
print("a = ", a)
print("b = ", b)
print("merged_dictionary = ", merged_dictionary)
