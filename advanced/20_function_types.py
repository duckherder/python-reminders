"""More on different types of functions in Python 3."""


class Bob(object):
    def __init__(self):
        pass

    def __add__(self):
        pass

    def a_method(self, x):
        pass

    @staticmethod
    def a_static_method(self):
        pass

    @classmethod
    def a_class_method(cls):
        pass


# see https://stackoverflow.com/questions/10401935/python-method-wrapper-type
print("\n")
print("Bob.__init__ =", Bob.__init__)                   # function
print("Bob.__add__ =", Bob.__add__)                     # function
print("Bob.__getattribute__ =", Bob.__getattribute__)   # slot wrapper -> wraps C-implemented function
print("Bob.__ne__ =", Bob.__ne__)                       # slot wrapper -> wraps C-implemented function
print("Bob.a_method =", Bob.a_method)                   # function
print("Bob.a_static_method =", Bob.a_static_method)     # function
print("Bob.a_class_method =", Bob.a_class_method)       # bound method (bound to class)

my_instance = Bob()
print("\n")
print("my_instance.__init__ =", my_instance.__init__)   # bound method (bound to my_instance)
print("my_instance.__add__ =", my_instance.__add__)     # bound method
print("my_instance.__getattribute__ =", my_instance.__getattribute__)   # method-wrapper
print("my_instance.__ne__ =", my_instance.__ne__)       # method-wrapper -> wraps C-implemented function as bound method
print("my_instance.a_method =", my_instance.a_method)   # bound method
print("my_instance.a_static_method =", my_instance.a_static_method) # function
print("my_instance.a_class_method =", my_instance.a_class_method)   # bound method (bound to class)


def a_function():
    pass


print("\n")
print("a_function =", a_function)                       # function
print("str.capitalize =", str.capitalize)               # method
print("list.append =", list.append)                     # method
print("(0).__ne__ =", (0).__ne__)                       # method-wrapper
my_list = [1,2,3]
print("my_list.append =", my_list.append)               # built-in method (bound to my_list)
my_iterator = iter(my_list)
print("my_iterator.__next__ =", my_iterator.__next__)   # method-wrapper
print("issubclass =", issubclass)                       # built-in function
