import types
import inspect

class MyNonDataDescriptor:
    def __init__(self):
        print("MyNonDataDescriptor initialisation")

    def __get__(self, obj, type=None):                          # self is MyNonDataDescriptor instance
        print("__get__ called in MyNonDataDescriptor")          # and obj is the object we're attached to
        print("__get__ obj=", obj, "type=", type)               # ...sou'll get a MyClass obj in this case
        return 19


class MyDataDescriptor:
    def __init__(self):
        print("MyDataDescriptor initialisation")
        self.some_value = 'some_value'

    def __get__(self, obj, type=None):
        """implements the __get__ method of the descriptor protocol"""
        print("__get__ called in MyDataDescriptor")
        return self.some_value

    def __set__(self, obj, value):
        """implements the __set__ method of the descriptor protocol"""
        print("__set__ called in MyDataDescriptor")
        self.some_value = value


class MyReadOnlyDescriptor:
    def __init__(self):
        print("MyReadOnlyDescriptor initialisation")

    def __get__(self, obj, type=None):
        print("__get__ called in MyReadOnlyDescriptor")
        return 19

    def __set__(self, obj, value):
        print("__set__ called in MyReadOnlyDescriptor")
        raise AttributeError("this value is read only!")



class MyClass:
    # once instantiated as part of MyClass it can considered a descriptor
    # as can be accessed using the dot (.) operator which these descriptors override and have precedence
    print("descriptor objects live in the class and not the instance")
    my_descriptor = MyNonDataDescriptor()
    my_data_descriptor = MyDataDescriptor()
    my_ro_descriptor = MyReadOnlyDescriptor()

    def __init__(self):
        pass


my_instance = MyClass()
print("\nUsing the non-data descriptor...")
print("type(my_instance.my_descriptor) =", type(my_instance.my_descriptor))
print("my_instance.my_descriptor at", id(my_instance.my_descriptor))
print("my_instance.my_descriptor =", my_instance.my_descriptor)
my_instance.my_descriptor = 'my new value'                                      # no __set__ method so...
print("type(my_instance.my_descriptor) =", type(my_instance.my_descriptor))     # no longer a descriptor, just a string
print("my_instance.my_descriptor at", id(my_instance.my_descriptor))            # __get__ no longer called
print("my_instance.my_descriptor =", my_instance.my_descriptor)

print("\nUsing the data descriptor...")
print("type(my_instance.my_data_descriptor) =", type(my_instance.my_data_descriptor))
print("my_instance.my_data_descriptor at", id(my_instance.my_data_descriptor))
print("my_instance.my_data_descriptor =", my_instance.my_data_descriptor)
my_instance.my_data_descriptor = 'ive changed this value'
print("type(my_instance.my_data_descriptor) =", type(my_instance.my_data_descriptor))   # remains MyDataDescriptor
print("my_instance.my_data_descriptor at", id(my_instance.my_data_descriptor))          # __get__ still called
print("my_instance.my_data_descriptor =", my_instance.my_data_descriptor)

print("\nUsing the read-only descriptor...")
print("type(my_instance.my_ro_descriptor) =", type(my_instance.my_ro_descriptor))
print("my_instance.my_ro_descriptor at", id(my_instance.my_ro_descriptor))
print("my_instance.my_ro_descriptor =", my_instance.my_ro_descriptor)
try:
    my_instance.my_ro_descriptor = 'ive changed this value'                     # recommended way to implement
except AttributeError as e:                                                     # read-only attribute
    print("exception handler:", e)
print("type(my_instance.my_ro_descriptor) =", type(my_instance.my_ro_descriptor))
print("my_instance.my_ro_descriptor at", id(my_instance.my_ro_descriptor))
print("my_instance.my_ro_descriptor =", my_instance.my_ro_descriptor)


class MySelf:
    def __init__(self):
        print("MySelf initialisation")
        print("type(self) =", type(self))
        print("id(self) =", id(self))
        print(self)                                     # what is self?, self is a MySelf object
        self.some_attribute = 'some instance attribute'

    def do_something(funky_chicken, some_parameter):    # you don't need to call it 'self' - it's just the
        print("in do_something function")               # ...accepted name to use for first parameter in bound method
        print("type(funky_chicken) =", type(funky_chicken))
        print("id(funky_chicken) =", id(funky_chicken))
        print("funky_chicken.some_attribute =", funky_chicken.some_attribute)
        print("type(some_parameter) =", type(some_parameter))
        print("id(some_parameter) =", id(some_parameter))
        if some_parameter is funky_chicken:
            print("hey we've passed self twice!")
        else:
            print(some_parameter)


print("\nwhat is self?...")
my_instance = MySelf()
my_instance.do_something('hello')
my_instance.do_something(my_instance)


class MyClass:
    my_class_variable = 1                   # not a descriptor, will appear in MyClass.__dict__
    def __init__(self):
        self.my_instance_variable = 2       # will appear in my_instance.__dict__


print("\nwhat is __dict__ attribute and the look up chain?...")
# dict's are used if __get__ method fails on any matching named data descriptors in class
# e.g. if I call print(my_instance.my_class_variable) interpreter will see if my_class_variable is a data descriptor
# that exposes the __get__ interface; if that fails then it will try my_instance.__dict__['my_class_variable'] and
# after that the lookup chain will look for a non-data descriptors with a __get__ method, followed by
# type(my_instance).__dict__['my_class_variable'] (or MyClass.__dict__['my_class_variable']) and failing
# all that will start progressing up parent classes
my_instance = MyClass()
print(my_instance.__dict__)
print(MyClass.__dict__)
print(type(my_instance).__dict__)


def my_dynamic_method(self, x):
    print("self.my_instance_variable + x =", self.my_instance_variable + x)


print("\ndynamically adding a method to an object instance...")
# monkey patch = modification/addition of attributes at run-time
my_instance.my_method = types.MethodType(my_dynamic_method, my_instance)
my_instance.my_method(5)            # method only available to this instance
del my_instance.my_method

class MyFunctionDescriptor:
    def __init__(self):
        pass

    def __get__(self, obj, type=None):
        return obj.do_something

    def __set__(self, obj, value):
        print("__set__ called in MyReadOnlyDescriptor")
        raise AttributeError("this value is read only!")


class MyDynamicFunctionDescriptor:
    def __init__(self):
        pass

    def __get__(self, obj, type=None):
        return types.MethodType(my_dynamic_method, obj)     # similar to how instance methods are called

    def __set__(self, obj, value):
        print("__set__ called in MyReadOnlyDescriptor")
        raise AttributeError("this value is read only!")


class MySelf:
    def __init__(self):
        print("MySelf initialisation")
        print("type(self) =", type(self))
        print("id(self) =", id(self))
        print(self)                                     # what is self?, self is a MySelf object
        self.some_attribute = 'some instance attribute'
        self.my_instance_variable = 2

    def do_something(funky_chicken, some_parameter):    # you don't need to call it 'self' - it's just the
        print("in do_something function")               # ...accepted name to use for first parameter in bound method
        print("type(funky_chicken) =", type(funky_chicken))
        print("id(funky_chicken) =", id(funky_chicken))
        print("funky_chicken.some_attribute =", funky_chicken.some_attribute)
        print("type(some_parameter) =", type(some_parameter))
        print("id(some_parameter) =", id(some_parameter))
        if some_parameter is funky_chicken:
            print("hey we've passed self twice!")
        else:
            print(some_parameter)

    my_do_something = MyFunctionDescriptor()
    my_dynamic_something = MyDynamicFunctionDescriptor()


print("use descriptor object to call instance method...")
my_instance = MySelf()
my_instance.my_do_something('how odd')
my_instance.my_dynamic_something(19)


class MyInstanceDescriptor:
    def __set_name__(self, owner, name):                # available since Python 3.6
        print("MyInstanceDescriptor __set_name__")
        print("owner =", owner)
        print("name =", name)
        self.name = name

    def __get__(self, obj, type=None):
        print("MyInstanceDescriptor __get__")
        return obj.__dict__.get(self.name) or 0

    def __set__(self, obj, value):
        print("MyInstanceDescriptor __set__")
        obj.__dict__[self.name] = value                 # store value in object instance dictionary


class MyClass:
    print("create instance descriptor in MyClass")
    my_instance_descriptor = MyInstanceDescriptor()
    def __init__(self):
        pass


print("to get descriptors to work with instances, not just classes...")
my_instance1 = MyClass()
my_instance2 = MyClass()

print("MyClass.__dict__ =", MyClass.__dict__)
print("my_instance1.__dict__ =", my_instance1.__dict__)
print("my_instance2.__dict__ =", my_instance2.__dict__)
# MyClass.my_instance_descriptor = 3                        # this overwrites the descriptor with the 3 object..
my_instance1.my_instance_descriptor = 9                     # ...rather than call __set__ with obj = class object
my_instance2.my_instance_descriptor = 14
print("MyClass.__dict__ =", MyClass.__dict__)
print("my_instance1.__dict__ =", my_instance1.__dict__)
print("my_instance2.__dict__ =", my_instance2.__dict__)
