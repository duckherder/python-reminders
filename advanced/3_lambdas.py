"""Anonymous functions."""

import math

print("\nform 'lambda <bound variable, or argument>: <body including free variables>'...")
print("(lambda x: x)(n) =", (lambda x: x)("identical"))

print("\nyou can name your lambda e.g. times_two = lambda x: x * 2 ...")
times_two = lambda x: x * 2
print("type(times_two) =", type(times_two))
print("times_two(2) =", times_two(2))

print("\nwhat about multiple parameters to your lambda...")
print("(lambda x, y: x + y)(2, 8) =", (lambda x, y: x + y)(2, 8))       # immediately invoked function expression...
add_numbers = lambda x, y: x + y                                        # ...pronounced 'iffy'
print("add_numbers(5, 7) =", add_numbers(5, 7))


def my_func_function(a_list, func):              # higher order function - accepts or returns a function object
    return [func(x) for x in a_list]


print("\nyou can pass lambda functions to other (higher order) functions...")
print(my_func_function([1, 2, 3], lambda x: x * x))
print(my_func_function([1, 2, 3], lambda x: x + 1))
print(my_func_function([1, 2, 3], lambda x: math.sin(x)))


def my_returned_function(scale):
    return lambda x :  x * scale


print("\nyou can return lambda functions from other functions...")
print("my_returned_function(30)(3) =", my_returned_function(30)(3))
