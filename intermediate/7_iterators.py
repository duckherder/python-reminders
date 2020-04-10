import random

print("all(): returns True if all elements of an iterable list are True")
print(all([True, True, True, True]))
print(all([True, True, False, True]))

print("any(): returns True if all elements of an iterable tuple are True")
print(any((False, False, False, True)))
print(any((False, False, False, False)))

print("min/max(): return min/max of an iterable")
print(max(["bob", "tim", "andy"]))
print(min([1, 2, -3]))

print("use next function to read lines from file")
with open('7_iterators.py', 'r') as f:        # f is a file handle but also an iterator
    try:
        while True:
            current = next(f)
            print(current.strip())
    except StopIteration:
        print('EOF!')

my_list = [1, 5, 3, 'bob', 2]

print("common way to use an iterator is in a for loop")
for item in my_list:
    print(item)

print("or if you get given an iterator")
my_iter = iter(my_list)
for item in my_iter:
    print(item)

my_iter = iter(my_list)
# note this is how a for loop is implemented
print("you can use iter() and next()")
while True:
    try:
        # next() will throw StopIteration if nothing left in iterable
        print(next(my_iter))
    except StopIteration:
        print("end of list!")
        break

my_iter = iter(my_list)
print("or the __next__() attribute of the iterator")
while True:
    try:
        # next() will throw StopIteration if nothing left in iterable
        print(my_iter.__next__())
    except StopIteration:
        print("end of list!")
        break

print("we can create an iterable class by implementing __iter__ and __next__ attributes")


class IterableClass:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):                 # called when you use iter() on an instance of IterableClass
        # need to reset each time iter() is called else only works once
        self.value = 1
        return self                     # makes the iterator iterable

    def __next__(self):
        if self.value < self.limit:
            self.value *= 2
            return self.value
        else:
            raise StopIteration         # iteration will cease when this is raised


bob = IterableClass(256)
for value in bob:
    print(value)


def my_random_number_generator():
    return random.randint(1, 10)


print("you can pass a function and a sentinel - value that raises the exception if returned from function")
sentinel_based_iterator = iter(my_random_number_generator, 5)
while True:
    try:
        print(next(sentinel_based_iterator))
    except StopIteration:
        print("jackpot! random number of 5!")
        break

for random_value in iter(my_random_number_generator, 5):
    print(random_value)

print("you can use zip to create an iterable of tuples that aggregate from a number of iterables")
my_list_a = ['bob', 'simon', 'john', 'dave']
my_list_b = [1, 2, 3]
my_list_c = [3.1, 3.4, 1.4, 8.3]

# will terminate on shortest of the iterables
for zipped_tuple in zip(my_list_a, my_list_b, my_list_c):
    # gets the nth item from each iterable in the zip list and puts them in a tuple
    print(zipped_tuple)
