print("an attribute is a name associated with an object in the form object.attribute")
print("objects have attributes, including even modules...")
print("module name:", __name__)
# get a list of all attribute names as a list of strings
print(dir())
# double underscore usually means it is a built in method or variable


def my_function():
    """my doc string"""
    pass


print("functions have attributes...")
print("function name:", my_function.__name__)
print("module doc string:", my_function.__doc__)
print(dir(my_function))

print("we can use getattr() built in function if object has __getattribute__ attribute")
print("the __name__ attribute is of type",
      type(getattr(my_function, '__name__')))
print(getattr(my_function, '__name__'))

print("we can create new object attributes even if it makes no sense")
setattr(my_function, 'other_value', 9)
my_function.womble = 'great uncle bulgaria'         # or directly
print(dir(my_function))
print(my_function.other_value)
print(my_function.womble)
print("use hasattr() for womble:", hasattr(my_function, 'womble'))
print("use hasattr() for disco:", hasattr(my_function, 'disco'))

print("we can delete an attribute")
delattr(my_function, 'womble')
del my_function.other_value                         # or directly
print(dir(my_function))

print("even numbers have attributes...")
print(dir(0.5))                     # numbers don't have a name attribute
print("we can see 0.5 has an attribute is_integer")
print("is_integer of type", type(0.5.is_integer))
print("its a function so lets call it, result is", 0.5.is_integer())
print("try 1.0, result is", 1.0.is_integer())

try:
    setattr(0.5, 'other_value', 9)
except AttributeError:
    print("although __setattr__ is a named attribute of 0.5 python won't allow it, booo!!")
