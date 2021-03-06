"""How to define and use functions in Python."""


def my_empty_function():
    """This describes the action the function takes."""
    pass    # doc string acts a statement so this not necessary


print("\nstart with an empty function...")
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


print("\nyou can pass any old object to a function as a parameter...")
my_parameterised_function('bob', 10)
# Python is dynamically typed
my_parameterised_function('tim', [1, 2, 3])
my_parameterised_function('sam', (1, 2, 3))


def execute_my_function(func):
    print(func())


print("you can even pass a function object as a parameter")
execute_my_function(my_simple_function)

print("\nyou can use keywords when calling a function and you can change order...")
my_parameterised_function(name='tim', value=[1, 2, 3])
# named values must come after unnamed positional ones
my_parameterised_function(value=[1, 2, 3], name='tim')


def my_default_function(name, value=None):
    if value is None:
        print("value is None!")


print("\nyou can set default values to parameters such that they do need to be specified...")
my_default_function('bob')
my_default_function('bob', 'sally')


# as of Python 3.5 you can provide hints to how the function should be used
def my_type_hinted_function(name: str) -> bool:
    return True


print("\nusing hints...")
print(my_type_hinted_function('bob'))


def my_type_hinted_function2(name: str) -> bool:
    # however Python is not a statically typed language, so
    return "bob"


print("no errors will be generated - it is a hint only")
print(my_type_hinted_function2(1))


def my_local_variable_function(x):
    # local scope only -> only available in function
    _my_local_variable = x
    x += 1
    return x


print("\nyou can not access locally scoped variables in function from outside...")
MY_GLOBAL_VARIABLE = 10
print(my_local_variable_function(MY_GLOBAL_VARIABLE))
print("MY_GLOBAL_VARIABLE =", MY_GLOBAL_VARIABLE)
try:
    print("_my_local_variable =", _my_local_variable)
except NameError:
    print("local variable _my_local_variable does not exist here - NameError exception raised!")


print("\nchecking to see if an object is callable...")
print("callable(my_local_variable_function) =",
      callable(my_local_variable_function))
print("callable([1, 2, 3]) =", callable([1, 2, 3]))


def my_function(number, a_list=[]):         # default values are evaluated when functions are created
    a_list.append(number)                   # ..and not when function called, so care is required with
    print(a_list)                           # mutable objects like lists


print("\ncareful: default values are evaluated when functions are created...")
my_function(1)
my_function(2)                              # not what you might have expected
print("use a_list=None and create list in my_function if a_list is None")
