"""Generators allow you to declare a function that behaves like an iterator - a lazy iterator."""

import random

# generators are for creating large lists that don't require large amount of memory like a list see PEP255
print("\nusing a generator function and yield...")    # generators behave like iterators but are implemented differently


# you could make generator create an infinite list
def random_number_sequence(limit):
    num = limit
    while num > 0:
        # use of 'yield' is what makes it a generator object rather than a standard object
        # state of generator function object saved here and number returned
        yield random.randint(0, 100)
        # start again from here when next() is called
        num -= 1


for i in random_number_sequence(10):
    print(i)

# the generator function is just a function
print("type(random_number_sequence) =", type(random_number_sequence))
# could be set to 100000000 without allocating equivalent memory
generator_fn = random_number_sequence(10)
print("..but object created when generator function is called is of type(generator_fn) =", type(generator_fn))

print("\nthe generator object is an iterator so we can call next() on a generator object...")
print(next(generator_fn))
print(next(generator_fn))
print(next(generator_fn))

print("\nusing a generator expression or comprehension...")
generator_comprehension = (random.randint(0, 100) for x in range(0, 10))
print("some random numbers")
for i in generator_comprehension:
    print(i)

my_string = 'hello'
print("converting the string '", my_string, "' to hexideximal")
hex_generator = ("{:02x}".format(ord(c)) for c in my_string)
print(type(hex_generator))
# join expects an iterable e.g. a list or a generator expression
print(":".join(hex_generator))

# from https://realpython.com/introduction-to-python-generators/
print("\ncomparing a list comprehension with a generator comprehension...")
nums_squared_lc = [num**2 for num in range(5)]
nums_squared_gc = (num**2 for num in range(5))
print("[num**2 for num in range(5)] =", nums_squared_lc)
print("(num**2 for num in range(5)) =", nums_squared_gc)

print("these do the same thing but have a different memory footprint")
# this creates a whole list through comprehension and then iterates
for i in [num**2 for num in range(5)]:
    print(i)
for i in (num**2 for num in range(5)):          # this iterates data as it goes
    print(i)

print("\nmax() also takes an iterable as a parameter so we can pass generator to max...")
print(max(num**2 for num in range(5)))


def single_shot():
    yield 'fire!'
    return True             # returning value from generator function


print("\nwhat if i return a value from a generator?...")
my_single_shot = single_shot()
print(next(my_single_shot))
try:
    print(next(my_single_shot))
except StopIteration as e:              # StopIteration exception is raised
    print("StopIteration exception: generator finished and returned value:", e)

print("\nwill a generator comprehension raise an exception?...")
single_shot_comprehension = (random.randint(0, 100) for x in range(0, 1))
print(next(single_shot_comprehension))
try:
    print(next(single_shot_comprehension))
except StopIteration as e:              # StopIteration exception is raised again
    # ...but no return value to print
    print("StopIteration exception: generator finished and returned value:", e)


def single_shot_fn():
    fired = True
    return fired


print("\nwhat attributes does a generator different from a standard function...")
print("difference in attributes between a generator function and standard function:",
      (set(dir(single_shot)) - set(dir(single_shot_fn))))
print("difference in attributes between a generator object and standard function:",
      (set(dir(my_single_shot)) - set(dir(single_shot_fn))))
print("difference in attributes between a generators from function or comprehension:",
      (set(dir(my_single_shot)) - set(dir(single_shot_comprehension))))


def triple_shot():
    yield 'first yield!'
    yield 'second yield!'
    yield 'third yield!'


print("\nyou can have multiple yields...")
my_triple_generator = triple_shot()
print(next(my_triple_generator))
print(next(my_triple_generator))
print(next(my_triple_generator))


def send_to_yield():
    # yield as expression and not statement
    ret = (yield 1)
    print("after first yield, ret=", ret)
    ret = (yield 2)
    print("after second yield, ret=", ret)
    yield                                           # yield None


try:
    print("\nhow to use send() to create a coroutine...")
    my_send_to_yield = send_to_yield()
    print("calling next(my_send_to_yield)")
    print("value returned from next =", next(my_send_to_yield)
          )                     # return first yielded value
    print("sending 'hello yield' to the generator")
    print("value returned from send =", my_send_to_yield.send(
        'hello yield'))       # send returns next yield value
    print("calling next(my_send_to_yield)")
    # returns last yield (None)
    print("value returned =", next(my_send_to_yield))
except StopIteration:
    print("generator complete!")


def test_yield():
    try:
        yield 1
        yield 2
        yield 3
    except ValueError:
        print("caught value error exception in generator!")


print("\ncall throw on generator object...")
my_throw_yield = test_yield()
value = next(my_throw_yield)
try:
    if value == 1:
        my_throw_yield.throw(ValueError("whoops don't like looks of this from generator"))
except StopIteration:
    print("caught stop iteration - thrown by throw() function")

print("\ncall close on generator object...")
my_close_yield = test_yield()
value = next(my_close_yield)
if value == 1:
    my_close_yield.close()
try:
    # should be 2 if hadn't closed the generator
    value = next(my_close_yield)
except StopIteration:
    print("caught stop iteration - thrown by next() function")


print("'\nyield from' allows for delegation to sub-generators...")
# see https://docs.python.org/3/whatsnew/3.3.html#pep-380

print("simple example")
my_sub_generator = ['bob', 'sally', 'donald']       # a list can be considered a sub-generator


def my_generator():
    yield from my_sub_generator                     # this could be any generator function or comprehension
    yield from range(3)
    yield from (x for x in my_sub_generator)
    yield (x for x in my_sub_generator)             # if I just yield, it will yield a generator object instead


for x in my_generator():
    print(x)


print("\ncan be useful for recursive traversal of tree...")
my_nested_list = [[[1, 2, 3], 'bob', 'john'], ['sally', 'susan', 'amelia']]


def traverse_nested_lists(a_node):
    if type(a_node) is not list:
        print("yielding a node")
        yield a_node
    else:
        print("recurse nested list")
        for node in a_node:
            yield from traverse_nested_lists(node)


for x in traverse_nested_lists(my_nested_list):
    print(x)
