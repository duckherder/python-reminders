a = ('a', 'b', 'c')         # packing a tuple
(aa, bb, cc) = a            # unpacking a tuple

my_unpacked_string_list = [*'hello']
print("my_unpacked_string_list =", my_unpacked_string_list)
my_unpacked_tuple_list = [*('a', 1, 3.4)]
print("my_unpacked_tuple_list =", my_unpacked_tuple_list)
my_unpacked_list_list = [*['a', 1, 3.4]]
print("my_unpacked_list_list =", my_unpacked_list_list)

*my_unpacked_tuple_list, = ('a', 1, 3.4)                    # unpacks to a list
print("my_unpacked_tuple_list =", my_unpacked_tuple_list)

first, second, *rest = 'hello'                              # from PEP 3132
print("first =", first)
print("second =", second)
print("rest =", rest)

first, second, *rest = (1, 'bob', 3, 3.5, 'fred')
print("first =", first)
print("second =", second)
print("rest =", rest)


def my_function(param1, param2=None):
    print("in my_function(param1, param2)")
    print("param1 =", param1)
    print("param2 =", param2)


print("calling my_function by unpacking a tuple with * operator....")
arguments = (1, 'bob')
print("arguments =", arguments)         # will print the tuple
# this expands to print("*arguments =", 1, 'bob') in print function
print("*arguments =", *arguments)
# if pass tuple as argument then single tuple will be passed
my_function(arguments)
# if we didn't unpack we send a single tuple parameter, rather than int, str
my_function(*arguments)

print("calling my_function using parameter names by unpacking a dictionary with ** operator...")
# what we want to send named arguments -> can't do this...
arguments = ('param2 = 1', 'param1 = 2')
# ..we'll just pass two strings
my_function(*arguments)
arguments = {'param2': 1, 'param1': 2}              # keywords must be strings
# use a dictionary and **operator
my_function(**arguments)


def argument_function(*args):
    print("number of arguments =", len(args))
    # always a tuple, even if just passing a single integer
    print("type(args) =", type(args))
    print(args)


print("calling a functions with *args parameter...")
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


def keyword_function(**named_args):
    print("number of named arguments =", len(named_args))
    print("type(named_args) =", type(named_args))
    # we'll get a dictionary instead of a tuple
    print(named_args)


print("calling a functions with **named_args parameter...")
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


print("calling a functions with *args and **kwargs parameters...")
args_and_kwargs(1, 2, [7, 'bob'])
args_and_kwargs(mary=1, donald=2, sally=[7, 'bob'])
args_and_kwargs(1, 2, sally=[7, 'bob'])
