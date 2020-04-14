import random

# generators are for creating large lists that don't require large amount of memory like a list see PEP255
print("allow you to declare a function that behaves like an iterator - a lazy iterator")

print("using a generator function and yield...")


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

print("the generator object is an iterator so we can call next() on a generator object...")
print(next(generator_fn))
print(next(generator_fn))
print(next(generator_fn))

print("using a generator expression or comprehension...")
generator_comprehension = (random.randint(0, 100) for x in range(0, 10))
for i in generator_comprehension:
    print(i)

my_string = 'hello'
# generator expression or generator comprehension
hex_generator = ("{:02x}".format(ord(c)) for c in my_string)
print(type(hex_generator))
# join expects an iterable e.g. a list or a generator expression
print(":".join(hex_generator))

# from https://realpython.com/introduction-to-python-generators/
nums_squared_lc = [num**2 for num in range(5)]
nums_squared_gc = (num**2 for num in range(5))
print(nums_squared_lc)
print(nums_squared_gc)

print("these do the same thing but have a different memory footprint")
# this creates a whole list through comprehension and then iterates
for i in [num**2 for num in range(5)]:
    print(i)
for i in (num**2 for num in range(5)):          # this iterates data as it goes
    print(i)

print("max() also takes an iterable as a parameter so we can pass generator to max =",
      max(num**2 for num in range(5)))

print("what if i return a value from a generator?...")


def single_shot():
    yield 'fire!'
    return True


my_single_shot = single_shot()
print(next(my_single_shot))
try:
    print(next(my_single_shot))
except StopIteration as e:              # StopIteration exception is raised
    print("StopIteration exception: generator finished and returned value:", e)

print("will a generator comprehension raise an exception?...")
single_shot_comprehension = (random.randint(0, 100) for x in range(0, 1))
print(next(single_shot_comprehension))
try:
    print(next(single_shot_comprehension))
except StopIteration as e:              # StopIteration exception is raised again
    # ...but no return value to print
    print("StopIteration exception: generator finished and returned value:", e)

print("what attributes does a generator different from a standard function")


def single_shot_fn():
    fired = True
    return fired


print("difference in attributes between a generator function and standard function:",
      (set(dir(single_shot)) - set(dir(single_shot_fn))))
print("difference in attributes between a generator object and standard function:",
      (set(dir(my_single_shot)) - set(dir(single_shot_fn))))
print("difference in attributes between a generators from function or comprehension:",
      (set(dir(my_single_shot)) - set(dir(single_shot_comprehension))))

print("you can have multiple yields...")


def triple_shot():
    yield 'first yield!'
    yield 'second yield!'
    yield 'third yield!'


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
    print("how to use send() to create a coroutine...")
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


print("call throw on generator object...")
my_throw_yield = test_yield()
value = next(my_throw_yield)
try:
    if value == 1:
        my_throw_yield.throw(ValueError(
            "whoops don't like looks of this from generator"))
except StopIteration:
    print("caught stop iteration - thrown by throw() function")

print("call close on generator object...")
my_close_yield = test_yield()
value = next(my_close_yield)
if value == 1:
    my_close_yield.close()
try:
    # should be 2 if hadn't closed the generator
    value = next(my_close_yield)
except StopIteration:
    print("caught stop iteration - thrown by next() function")
