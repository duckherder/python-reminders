"""Objects can be an iterable, an iterator or both. According to PEP234

1. An object can be iterated over with "for" if it implements
   __iter__() or __getitem__().

2. An object can function as an iterator if it implements next()."""

import random

print("all(): returns True if all elements of an iterable list are True...")
print(all([True, True, True, True]))
print(all([True, True, False, True]))

print("any(): returns True if all elements of an iterable tuple are True...")
print(any((False, False, False, True)))
print(any((False, False, False, False)))

print("min/max(): return min/max of an iterable...")
print(max(["bob", "tim", "andy"]))
print(min([1, 2, -3]))

print("use next function to read lines from file...")
with open('7_iterators.py', 'r') as f:        # f is a file handle but also an iterator...
    try:                                      # .. it has a __next__ attribute
        while True:
            current = next(f)
            print(current.strip())
    except StopIteration:
        print('EOF!')

my_list = [1, 5, 3, 'bob', 2]

print("common way to use an iterator is in a for loop...")
for an_item in my_list:
    print(an_item)

print("or if you get given an iterator using iter() - a list is iterable but is not an iterator itself...")
# list have an __iter__ attribute to return an iterator but no __next__
my_iter = iter(my_list)
for an_item in my_iter:
    print(an_item)

# note this is how a for loop is implemented
print("you can use iter() and next()...")
my_iter = iter(my_list)
while True:
    try:
        # next() will throw StopIteration if nothing left in iterable
        print(next(my_iter))
    except StopIteration:
        print("end of list!")
        break

my_iter = iter(my_list)
print("or the __next__() attribute of the iterator...")
while True:
    try:
        # next() will throw StopIteration if nothing left in iterable
        print(my_iter.__next__())
    except StopIteration:
        print("end of list!")
        break


print("we can create an iterable class by implementing the __getitem__ attribute...")

class GetItemClass:
    def __init__(self):
        """a doc string is a valid statement so don't need a pass"""

    def __getitem__(self, item):        # item can be an integer or a slice object
        print("in GetItemClass.__getitem__")
        if type(item) is int:
            return 2**item
        elif type(item) is slice:
            return [2**x for x in range(item.start, item.stop, item.step)]


my_getitem_instance = GetItemClass()
print("my_getitem_instance[0] =", my_getitem_instance[0])
print("my_getitem_instance[1] =", my_getitem_instance[1])
print("my_getitem_instance[2] =", my_getitem_instance[2])
print("GetItemClass is iterable as it implements __getitem__")
for my_value in my_getitem_instance:
    print("my_value =", my_value)
    if my_value > 32:          # because GetItemClass is an infinite iterator - it will never finish we need to break
        break
print("we can also use slicing with GetItemClass as it supports __getitem__")
for my_value in my_getitem_instance[4:12:2]:
    print("my_value =", my_value)

my_getitem_iterator = iter(my_getitem_instance)
print("interestingly iter() will return an iterator even though __iter__ is not defined")
print("my_getitem_iterator =", my_getitem_iterator)                 # iter() has returned a base class Iterator object
print("dir(my_getitem_iterator) =", dir(my_getitem_iterator))
print("next also works on this iterator by calling __getitem__ with increasing item values")
print("next(my_getitem_iterator) =", next(my_getitem_iterator))
print("next(my_getitem_iterator) =", next(my_getitem_iterator))
print("next(my_getitem_iterator) =", next(my_getitem_iterator))

print("we can create an iterable class by implementing __iter__ and __next__ attributes...")


class IterableClass:
    """class is iterable but also an iterator"""        # note this is not always true - sometimes an iterable
    def __init__(self, limit):                          # will return a separate iterator instance e.g. a list
        self.limit = limit

    def __iter__(self):                 # called when you use iter() on an instance of IterableClass
        # need to reset each time iter() is called else only works once
        self.value = 1
        return self                     # returns itself as the iterator

    def __next__(self):                 # as Iterable class is also an iterator we need to implement __next__
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


print("you can pass a function and a sentinel - value that raises the exception if returned from function...")
sentinel_based_iterator = iter(my_random_number_generator, 5)
while True:
    try:
        print(next(sentinel_based_iterator))
    except StopIteration:
        print("jackpot! random number of 5!")
        break

for random_value in iter(my_random_number_generator, 5):
    print(random_value)

print("you can use zip to create an iterable of tuples that aggregate from a number of iterables...")
my_list_a = ['bob', 'simon', 'john', 'dave']
my_list_b = [1, 2, 3]
my_list_c = [3.1, 3.4, 1.4, 8.3]

# will terminate on shortest of the iterables
for zipped_tuple in zip(my_list_a, my_list_b, my_list_c):
    # gets the nth item from each iterable in the zip list and puts them in a tuple
    print(zipped_tuple)


print("we can create an iterable class that returns a separate iterator object...")


class StudentIteratorClass:
    def __init__(self, student_iterable):
        print("StudentIteratorClass.__init__")
        self.student_iterable = student_iterable
        self.index = 0

    def __next__(self):                                     # as an iterator we need to implement __next__
        print("StudentIteratorClass.__next__")
        if self.index < len(self.student_iterable.students):
            _next_val = self.student_iterable.students[self.index]
            self.index += 1
            return _next_val
        else:
            raise StopIteration


class StudentIterableClass:
    def __init__(self):
        print("StudentIterableClass.__init__")
        self.students = ['bob', 'sally', 'jake']

    def __iter__(self):
        print("StudentIterableClass.__iter__")
        return StudentIteratorClass(self)


my_instance = StudentIterableClass()
my_instance_iterator = iter(my_instance)
print("type(my_instance_iterator) =", type(my_instance_iterator))
for student in my_instance:
    print("student =", student)
