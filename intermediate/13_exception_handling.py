"""Exception handling in Python."""

import builtins
import inspect
import pprint

print("\nwhat if we do a simple divide by zero...")
try:
    z = 1 / 0
except ZeroDivisionError:
    print("divide by zero!")

try:
    z = 1 / 0
except ZeroDivisionError as e:
    print(e)

print("\nwhat if we do a bad index into a list...")
my_list = [1, 2, 3]
try:
    print(my_list[8])
except IndexError as e:
    print(e)

print("\nwhat are the builtin exception types?...")
pprint.pprint([x for x in dir(builtins) if inspect.isclass(
    eval(x)) and issubclass(eval(x), BaseException)])

print("catch all builtin exceptions")
try:
    z = 1 / 0
except BaseException:
    print("catching all builtin exceptions subclassed from BaseException!")

print("\nwe can use an 'else' condition for what to do if try succeeds...")
try:
    f = open("bob.txt", "r")           # try something - an action
except FileNotFoundError:
    # do something as a consequence of failure, such as rollback an action
    print("failed to open file")
else:
    print("should not be seeing this message")

try:
    print("do something that doesn't raise an exception")
except FileNotFoundError:
    # do something as a consequence of failure, such as rollback an action
    print("failed to open file")
else:
    print("no exception so do something else as a consequence")


print("\nwe can use 'finally' condition for what to do regardless of try succeeding...")
try:
    print("try an open non-existent file")
    f = open("bob.txt", "r")
except FileNotFoundError:
    print("failed to open file")
finally:
    # will execute regardless of
    print("and finally do this whatever...")

try:
    print("do something that doesn't raise an exception")
except BaseException:
    print("whoops exception")
finally:
    # will execute regardless of
    print("and finally do this whatever...")

print("\nnested try-excepts...")
try:
    try:
        z = 1 / 0
    except ZeroDivisionError:
        print("divide by zero exception")
        raise                                               # re-raise last exception
except BaseException as e:
    print("base exception", e)


def my_function(x):
    if type(x) is not int:
        raise TypeError("expected an integer!")
    if x < 0:
        raise ValueError("type ok but value not supported")
    return


print("\nworking function with no exceptions raised...")
try:
    my_function(1)
except (TypeError, ValueError) as e:
    print("exception caught:", e)

print("raising exceptions...")
try:
    my_function([1])
except (TypeError, ValueError) as e:            # to catch multiple exceptions use a tuple
    print("exception caught:", e)

try:
    my_function(-1)
except (TypeError, ValueError) as e:
    print("exception caught:", e)

print("\nhow do i write my own exception handler?...")


class MyExceptionHandler(Exception):
    def __init__(self, message, my_error_list):
        super().__init__(message)
        self.my_error_list = my_error_list


try:
    stuff_going_right_now = ['up', 1, 4.5]
    raise MyExceptionHandler("this is bad!!", stuff_going_right_now)
except MyExceptionHandler as e:
    print(e)
    print(e.my_error_list)
