"""Demonstration of some basic features."""
# various methods for importing modules from other packages
from math import factorial
import datetime
import numpy as np
import sys

print("time is ", datetime.datetime.now())
# we can use factorial rather than math.factorial()
print("5! = ", factorial(5))
array = np.array([1, 2, 3])     # use simpler/shorter module name
print(array)

if np.size(array) > 0:
    print("array is not empty!")

print("case sensitive so my_var and MY_VAR are different variables")
my_var = 3
MY_VAR = 4
print("my_var at", id(my_var), "with value", my_var)
print("MY_VAR at", id(MY_VAR), "with value", MY_VAR)


def my_function(bob, susan):
    # indentation is key in Python
    try:
        if bob is None:
            if susan is None:
                print("anybody there?")
                return True    # the return is also conditional on bob and susan both None
            return False    # bob is None but susan isn't
        return False    # bob is not None, who cares about susan
    except ValueError:
        print("whoops")
        pass                # does nothing
    return False


# use line continuation after the operator
if None is not None and\
   None is None:
    print("how odd")

# you can use line continuations like this
my_variable = 1 + 4 +\
    6 + 10
print(my_variable)

# line continuation not required for example in lists or dictionaries
my_colors = ['red',
             'green']
print(my_colors)

my_dictionary = {
    'a': 10,
    'b': 23
}
print(my_dictionary)

# multiple assignment
a, b, c = 1, 2, 3
print(a, b, c)
d = e = f = 4
print(d)

# getting help on some function, module etc..
print(help(dir))

if __name__ == '__main__':      # typical entry point for python program from interpreter, not another module
    print("in main!")           # you would expect to call some function here and pass the return value to
    sys.exit()                  # ..sys.exit. Note a None value is equivalent to passing 0 (ok)
