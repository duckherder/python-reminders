def my_empty_function():
    """This describes the action the function takes"""
    pass    # needs something else syntax error


print("start with an empty function")
print(my_empty_function.__doc__)
my_empty_function()

print("a function is an object, so it has attributes")
print(dir(my_empty_function()))


def my_simple_function():
    """This describes the action the function takes"""
    return "hello"


print("you can return any object from a function")
print(my_simple_function())


def my_parameterised_function(name, value):
    print("My name is", name, "and I have value =",
          value, "of type", type(value))


print("you can pass any old object to a function as a parameter")
my_parameterised_function('bob', 10)
# Python is dynamically typed
my_parameterised_function('tim', [1, 2, 3])
my_parameterised_function('sam', (1, 2, 3))


def execute_my_function(func):
    print(func())


print("you can pass a function object as a parameter")
execute_my_function(my_simple_function)

print("you can use keywords when calling a function and you can change order")
my_parameterised_function(name='tim', value=[1, 2, 3])
# named values must come after unnamed positional ones
my_parameterised_function(value=[1, 2, 3], name='tim')

print("you can set default values to parameters such that they do need to be specified")


def my_default_function(name, value=None):
    if value is None:
        print("value is None!")


my_default_function('bob')
my_default_function('bob', 'sally')


# as of Python 3.5 you can provide hints to how the
def my_type_hinted_function(name: str) -> bool:
    return True                                         # function should be used


print(my_type_hinted_function('bob'))


def my_type_hinted_function2(name: str) -> bool:
    # however Python is not a statically typed language, so
    return "bob"


    # no errors will be generated - it is a hint only
print(my_type_hinted_function2(1))


def my_local_variable_function(x):
    # local scope only -> only available in function
    _my_local_variable = x
    x += 1
    return x


MY_GLOBAL_VARIABLE = 10
print(my_local_variable_function(MY_GLOBAL_VARIABLE))
print(MY_GLOBAL_VARIABLE)
try:
    print(_my_local_variable)
except NameError:
    print("local variable does not exist here - exception raised!")
