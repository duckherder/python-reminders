"""decorators are higher order functions that accept functions and return another function that executes the original"""
import datetime
import functools

def check_value(func):
    """checking value parameter decorator - function that returns a function."""
    def do_checking(name, value):
        print("decorate: we can do anything we like here, even changing the function parameters or anything")
        if value is None or value == 0:         # decorate original function
            value = 4
        return func(name, value)
    # return function that calls original function parameter
    return do_checking


def fix_name(func):
    """ensure string is correct capitalised."""
    def do_changes(name, value):
        print("decorate: we can fix strings through capitalization")
        name = name.capitalize()
        return func(name, value)
    return do_changes


def negate_value(func):
    """negate value decorator."""
    def do_negation(name, value):
        print("decorate: we can change return values by negating value")
        return -value
    return do_negation


def my_function(name, value):
    """this is our function we want to decorate."""
    print("name:", name, "value:", value)
    return


print("we can stack these functions so one will call the other...")
my_fixed_name_function = fix_name(my_function)                  # a way to create a decorated version of function
my_value_checked_and_fixed_name_function = check_value(my_fixed_name_function)
# original my_function has been decorated
my_value_checked_and_fixed_name_function("hello world!", None)


# this decorator is called first
@check_value
@fix_name
@negate_value                               # you can see this as series of function calls with a function as parameter
def my_decorated_function(name, value):     # ...check_value(fix_name(negate_value(my_decorated_function)))
    """my original function."""
    print("name:", name, "value:", value)
    return value


print("we can use the @symbol to simplify decoration of a function")
print("my_decorated_function.__name__ =", my_decorated_function.__name__)       # not what we expected
ret_value = my_decorated_function("hello world!", 0)
print("ret_value from my_decorated_function =", ret_value)      # check value decorator used before negate_value


def my_general_capitalize_decorator(func):
    def capitalise_func(*args, **kwargs):
        args = tuple([x.capitalize() if isinstance(x, str) else x for x in args])
        kwargs = {k: v.capitalize() if isinstance(v, str) else v for k, v in kwargs.items()}
        func(*args, **kwargs)
    return capitalise_func


@my_general_capitalize_decorator
def my_function(name, age, surname, middle_name):
    print("name:", name, middle_name, surname, f"({age})")


@my_general_capitalize_decorator
def my_other_function(place, time):
    print("meet me at", place, "at", time)


print("we can use args and kwargs to make decorators suitable for different functions and parameters...")
my_function('bob', 34, 'smith', middle_name='reginald')
my_other_function('underneath the arches', datetime.datetime.now())


class SomeRandomClass:
    def __init__(self):
        pass

    @my_general_capitalize_decorator
    def a_method(self, name, age, surname, middle_name):
        print("class name:", name, middle_name, surname, f"({age})")


print("or class methods...")
my_instance = SomeRandomClass()
my_instance.a_method('bob', 34, 'smith', middle_name='reginald')

print("or even a lambda...")
my_general_capitalize_decorator(lambda x, y: print(x, y))('hello', 'bobby')


def my_decorator(func):
    @functools.wraps(func)              # note, you need to send func parameter in this case, wraps accepts
    def do_decoration():                # ...func as a parameter
        print("hello from decorator!")
        func()
    return do_decoration


@my_decorator
def my_function():
    """my_function doc string"""
    print("hello from function!")


print("wraps() decorator from functools can be used to preserve original name and docstring...")
my_function()
print("my_function.__name__ =", my_function.__name__)
print("my_function.__doc__ =", my_function.__doc__)

print("#################################")


def my_simple_decorator(func):
    print("calling function", func.__name__)        # this will be printed when function is decorated not..
    return func                                     # ..when the function is called


@my_simple_decorator                                # note that my_simple_decorator is applied here
def my_function():
    return 'hello from my_function'


print("decorators can be very simple for debugging or registering...")
print(my_function())

print("#################################")


def my_param_decorator(a_string, an_integer):       # functool.wraps() takes a function object as a parameter
    print("my_param_decorator")
    def my_parameterised_decorator(func):
        print("my_parameterised_decorator")
        def do_decoration(*args, **kwargs):
            print("do_decoration:", a_string)
            print(f"..executing {an_integer} times")
            for i in range(an_integer):
                func(*args, **kwargs)
        return do_decoration
    return my_parameterised_decorator


@my_param_decorator('decorator parameter', 2)       # my_param_decorator and my_parameterised_decorator called here
def my_function():
    print("in my_function")


print("we can pass parameters to a decorator using an extra function wrapper...")
my_function()                                       # do_decoration is done here

print("#################################")


# thanks to https://realpython.com/primer-on-python-decorators/
def my_param_decorator(_func=None, *, a_string=None, an_integer=1):     # * means all parameters after are keyword only
    print("my_param_decorator")
    def my_parameterised_decorator(func):
        print("my_parameterised_decorator")
        def do_decoration(*args, **kwargs):
            do_decoration.number_decorations += 1       # decorator state update
            print("do_decoration:", a_string)
            print(f"..executing {an_integer} times")
            for i in range(an_integer):
                func(*args, **kwargs)
        do_decoration.number_decorations = 0            # we can add attributes as usual for state
        return do_decoration

    if _func is None:
        print("_func is None so parameters were specified")
        print("a_string =", a_string, "an_integer =", an_integer)
        return my_parameterised_decorator               # return my_parameterised_decorator function as object
    else:
        print("_func is", _func)
        print("...so no parameters were specified, calling my_parameterised_decorator...!")
        _decorator_func = my_parameterised_decorator(_func)
        print("called my_parameterised_decorator to get decorator function")
        return _decorator_func                          # call function and returns the resulting function object
                                                        # ...do_decoration


@my_param_decorator         # so this is effectively my_param_decorator(my_function) so _func = my_function
def my_function():
    print("in my_function")


print("calling function with non-parameterised decorator...")
my_function()
# my_function is actually the decorated function do_decoration so we can access its attributes
print("number of decorations:", my_function.number_decorations)

print("#################################")


@my_param_decorator(an_integer=2)       # have parameters so _func = None so this is effectively...
def my_function():                      # ...my_param_decorator(an_integer=2)(my_function)
    print("in my_function")


print("calling function with parameterised decorator...")
my_function()
my_function()
print("number of decorations:", my_function.number_decorations)

print("#################################")
