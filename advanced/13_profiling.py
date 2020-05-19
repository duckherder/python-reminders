"""Profiling CPU and memory with Python."""

import time
import timeit
import statistics       # in standard library since Python 3.4/PEP450
import sys
from pympler import asizeof
import tracemalloc
from memory_profiler import profile
import objgraph
from guppy import hpy

print("########## timing code ############")

def is_prime_fn1(x):
    for i in range(2, x-1):
        if x % i == 0:
            return False
    return True


def is_prime_fn2(x):
    for i in range(2, int(x**.5)+1):
        if x % i == 0:
            return False
    return True


is_prime_lambda = lambda x: all(x % i != 0 for i in range(2, int(x**.5)+1))


def get_primes(y, func):
    _primes = []
    for val in range(y):
        if func(val):
            _primes.append(val)
    return _primes


print("\nwe can use time.time() to time code...")
start_time = time.time()
print(get_primes(1000, is_prime_fn1))
print(get_primes(1000, is_prime_fn2))
print(get_primes(1000, is_prime_lambda))
end_time = time.time()
print(f"elapsed time = {end_time - start_time} seconds")

print("\nwe can use time.perf_counter() for system wide elapsed time...")
start_time = time.perf_counter()            # time.clock() deprecated in Python 3.8
get_primes(10000, is_prime_fn1)
print(f"is_prime_fn1 elapsed time = {time.perf_counter()- start_time} seconds")

start_time = time.perf_counter()
get_primes(10000, is_prime_fn2)
print(f"is_prime_fn2 elapsed time = {time.perf_counter()- start_time} seconds")

start_time = time.perf_counter()
get_primes(10000, is_prime_lambda)
print(f"is_prime_lambda elapsed time = {time.perf_counter()- start_time} seconds")

print("\nwe can use time.process_time() if only want time for this process, excluding any sleeps...")
start_time = time.process_time()
get_primes(10000, is_prime_lambda)
print(f"is_prime_lambda elapsed time = {time.process_time()- start_time} seconds")

print("\nwe can use time.process_time_ns() for nanoseconds counting...")
start_time = time.perf_counter_ns()
print("hello!")
print(f"print elapsed time = {time.perf_counter_ns()- start_time}ns")

print("\nwe can use timeit.timeit if you prefer...")
print(timeit.timeit("get_primes(10000, is_prime_fn1)", globals=globals(), number=5))
print(timeit.timeit("get_primes(10000, is_prime_fn2)", globals=globals(), number=5))
print(timeit.timeit("get_primes(10000, is_prime_lambda)", globals=globals(), number=5))


def time_primes(number_tests=1):
    def my_time_prime_decorator(func):
        def time_prime_execution(*args, **kwargs):
            _tests = []
            for t in range(1, number_tests):
                _start_time = time.process_time()
                func(*args, **kwargs)
                _end_time = time.process_time()
                _tests.append(_end_time - _start_time)
            print("number of tests executed =", number_tests)
            print("mean execution time =", statistics.mean(_tests))
            print("standard deviation execution time =", statistics.stdev(_tests))
        return time_prime_execution
    return my_time_prime_decorator


@time_primes(number_tests=10)
def get_primes(y, func):
    _primes = []
    for val in range(y):
        if func(val):
            _primes.append(val)
    return _primes


print("\nwe can use a decorator if we so wish...")
get_primes(10000, is_prime_fn1)
get_primes(10000, is_prime_fn2)
get_primes(10000, is_prime_lambda)

print("\nfor large lists of data it is often much faster to create a dictionary than perform linear search...")
my_big_data_list = [(7263, 'bob'), (221333, 'sally'), (212892, 'simon')]
for x in my_big_data_list:
    if x[0] == 221333:
        print("found them!")
my_big_data_list_dict = {x[0]: x for x in my_big_data_list}         # use a dictionary comprehension
print(my_big_data_list_dict)
print(my_big_data_list_dict[221333])

print("########## memory usage ############")

print("\nmemory usage...")
my_number_list = [1, 2, 3, 4]
print("some objects have the __sizeof__ attribute")
print("my_list =", my_number_list)
print(dir(my_number_list))
print("type(my_list.__sizeof__) =", type(my_number_list.__sizeof__))
print("len(my_list) =", len(my_number_list))                               # just number of elements
print("my_list.__sizeof__() =", my_number_list.__sizeof__())               # raw object size
print("sys.getsizeof(1) =", sys.getsizeof(1))
print("sys.getsizeof(my_number_list) =", sys.getsizeof(my_number_list))    # __sizeof__ + garbage collector overhead
print("len(my_number_list) * (1).__sizeof__() =", len(my_number_list) * (1).__sizeof__())
print("total size of elements greater than list object size!")

my_string_list = ['hello world', 'my name is Bob', 'quick brown fox', 'phillip the cat']
print("my_string_list =", my_string_list)
print("len(my_string_list) =", len(my_string_list))                         # just number of elements
print("my_string_list.__sizeof__() =", my_string_list.__sizeof__())         # raw object size
print("sys.getsizeof(my_string_list) =", sys.getsizeof(my_string_list))     # __sizeof__ + garbage collector overhead
print("string list the same size as integer list")

print("sys.getsizeof(my_number_list) + sys.getsizeof(1) + ... =",
      sys.getsizeof(my_number_list) +
      sys.getsizeof(1) +
      sys.getsizeof(2) +
      sys.getsizeof(3) +
      sys.getsizeof(4))
print("sys.getsizeof(my_string_list) + sys.getsizeof('hello world') + ... =",
      sys.getsizeof(my_string_list) +
      sys.getsizeof('hello world') +
      sys.getsizeof('my name is Bob') +
      sys.getsizeof('quick brown fox') +
      sys.getsizeof('phillip the cat'))
print("asizeof.asizeof(my_number_list) =", asizeof.asizeof(my_number_list))
print("asizeof.asizeof(my_string_list) =", asizeof.asizeof(my_string_list))

print("\nusing tracemalloc...")
tracemalloc.start()
trace_malloc_vector = [z for z in range(1000)]
memory_snapshot = tracemalloc.take_snapshot()
stats = memory_snapshot.statistics('lineno')
for stat in stats[:10]:
    print(stat)

print("\nusing guppy...")
h = hpy()
h.setrelheap()
my_number_heaped_list = ['red', 'brown', 'green', 'blue']
print(my_number_heaped_list)
result = h.heap()
print(result)


print("\nusing memory_profiler...")
@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a


my_func()

print("\nusing objgraph...")
objgraph.show_most_common_types()
objgraph.show_growth(limit=3)
my_new_number_list = [1, 2, 3, 4]
my_new_string_list = ['hello world', 'my name is Bob', 'quick brown fox', 'phillip the cat']
objgraph.show_growth()
