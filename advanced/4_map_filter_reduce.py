"""Higher order functions that take a function and an iterable and do something with it."""

from functools import reduce                # built-in function in Python 2

print("\nuse map() to apply a function to an iterable...")
print("e.g. result = map(lambda x : x * 2, [1, 2, 3])")
result = map(lambda x: x * 2, [1, 2, 3])
# returns a map object iterator (generator)
print("map() returns an object of type", type(result))
for i in result:
    print(i)

print("\nvery similar to using a list comprehension...")
print("result = [(lambda x : x * 2)(y) for y in [1, 2, 3]]")
result = [(lambda x: x * 2)(y) for y in [1, 2, 3]]
print(type(result))
print(result)

print("\nbut in fact more like a generator...")
result = ((lambda x: x * 2)(y) for y in [1, 2, 3])
print(type(result))
for i in result:
    print(i)


def my_func(my_string, my_number=0):
    my_string = my_string.capitalize() + ':' + str(my_number)
    print("in my_func, my_string =", my_string)
    return my_string                                # need to return a value


print("\nyou can pass a lambda or any function...")
result = map(my_func, ['bob', 'tom', 'sheila'])
for i in result:
    # you can see interleaving of generator (my_func calls on next())
    print(i)
    # ..function evaluation as we go/need the data

print("\nwhat about multiple arguments to my_func...")
result = map(my_func, ['bob', 'tom', 'sheila'], [1, 2, 3])
for i in result:
    print(i)


def my_filter_function(my_integer):
    return True if my_integer % 2 else False


print("\nuse filter() to filter out items in an iterable - function or lambda must return True or False...")
result = filter(my_filter_function, [3, 4, 34, 2, 1, 1, 33, 4, 5, 6, 7])
print(type(result))
print(list(result))         # you can convert an iterable to a list

result = filter(lambda x: True if x % 2 else False,
                [3, 4, 34, 2, 1, 1, 33, 4, 5, 6, 7])
print(type(result))
print(list(result))

print("\nto use a function with multiple parameters use a lambda or a closure...")
result = filter(lambda x: True if x[0] > x[1]
                else False, [(4, 3), (7, 5), (2, 34)])
print(type(result))
print(list(result))


# function takes 2 values and reduces it to 1
def my_reduce_function(a, b):
    return a if a > b else b


print("\nuse reduce() to reduce an iterable to a single object based on a reduction function and sliding window")
print("sliding windows passes elements 0 and 1 to my_reduce_function() and then the result and element 2....")
# verbose way of performing max()
result = reduce(my_reduce_function, [1, 6, 3, 4, -1])
# ...again could use a lambda
print(type(result))
print(result)
