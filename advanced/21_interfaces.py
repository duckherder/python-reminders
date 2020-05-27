"""Implementing interfaces in Python."""

import abc          # abc = abstract base class

print("\nclass are objects and type and class can mostly be used to mean the same in Python but there are diffs...")
print("difference in attributes between object and type (metaclass = an object)", set(dir(type)) - set(dir(object)))


class MySimpleInterface:
    """Simple interface but with no enforcement, simply using standard subclassing."""

    def print_message(self, message: str) -> None:
        """Print message method with no implementation."""
        pass

    def my_other_interface_function(self):
        """There is no requirement with simple subclassing to fully implement this interface. Will work without it."""
        pass        # is this an interface in the true sense of the word?


class MyConcreteClass(MySimpleInterface):           # does not fully implement the interface

    def print_message(self, message: str) -> None:
        print("MyConcreteClass message:", message)


class MyOtherConcreteClass(MySimpleInterface):      # fully implements the interface

    def print_message(self, message: str) -> None:
        print("MyOtherConcreteClass message:", message)

    def my_other_interface_function(self):
        print("MyOtherConcreteClass message in my_other_interface_function!")


def some_function(my_interface: MySimpleInterface) -> None:
    print("in some_function")
    print("my_interface =", my_interface)
    my_interface.print_message("some random message!")
    # even though we have not fully implemented the interface we can however call my_other_interface
    my_interface.my_other_interface_function()


my_concrete_class = MyConcreteClass()
my_other_concrete_class = MyOtherConcreteClass()

print("\nwe can pass interfaces to functions to use...")
some_function(my_concrete_class)
some_function(my_other_concrete_class)

print("\nwe could override using a metaclass to enforce type checking...")   # From https://realpython/python-interface


class SimpleMeta(type):                                 # metaclass describes how a class should work

    def __instancecheck__(self, instance):
        print("overridding instance type check in SimpleMeta")
        return self.__subclasscheck__(type(instance))

    def __subclasscheck__(self, subclass):
        print("overridding subclass check in SimpleMeta")
        print("self =", self)
        print("subclass =", subclass)
        # see if subclass actually implements the interface
        return hasattr(subclass, 'print_message') and callable(subclass.print_message) and \
            hasattr(subclass, 'my_other_interface_function') and callable(subclass.my_other_interface_function)


class MySimpleInterface(metaclass=SimpleMeta):      # this is a virtual base class of MyFullImplementedConcreteClass...
                                                    # ...below as it implements the interface defined in metaclass
    """__subclasscheck__ implicitly makes print_message and my_other_interface available"""
    pass    # if you define them the point we hasattr and callable as above will work - which we don't want


class MyConcreteClass:

    def print_message(self, message: str) -> None:
        print("MyConcreteClass message:", message)


class MyFullImplementedConcreteClass:           # note implicit super-classing....
                                                # ....not MyFullImplementedConcreteClass(MySimpleInterface)...
                                                # ...which is also perfectly fine to do so appears in MRO

    def print_message(self, message: str) -> None:
        print("MyOtherConcreteClass message:", message)

    def my_other_interface_function(self):
        print("MyFullImplementedConcreteClass: in my_other_interface_function!")


print("using a metaclass we can see if a class is really of type MySimpleInterface")
print("issubclass(MyConcreteClass, MySimpleInterface) =", issubclass(MyConcreteClass, MySimpleInterface))
print("issubclass(MyFullImplementedConcreteClass, MySimpleInterface) =",
      issubclass(MyFullImplementedConcreteClass, MySimpleInterface))


def some_function(my_interface: MySimpleInterface) -> None:
    print("in some_function")
    print("my_interface =", my_interface)
    print("calling my_other_interface_function")
    my_interface.my_other_interface_function()


print("create instances")
my_full_concrete_class = MyFullImplementedConcreteClass()
my_concrete_class = MyConcreteClass()
print("isinstance(my_full_concrete_class, MySimpleInterface) =", isinstance(my_full_concrete_class, MySimpleInterface))
print("isinstance(my_concrete_class, MySimpleInterface) =", isinstance(my_concrete_class, MySimpleInterface))
print("now if we try and use interface improperly we will get an exception")
some_function(my_full_concrete_class)
try:
    some_function(my_concrete_class)
except AttributeError:
    print("Exception: Attribute error - my_other_interface is not implemented")


print("virtual base class and metaclass do not appear in the MRO if implicit inheritance used")
print("MyConcreteClass.__mro__ =", MyConcreteClass.__mro__)
print("MyFullImplementedConcreteClass.__mro__ =", MyFullImplementedConcreteClass.__mro__)

print("\nalternatively you can use the abstract base class abc to be more formal...")


class MySimpleABCInterface(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        print("overridding subclass hook in MySimpleABCInterface")
        print("self =", cls)
        print("subclass =", subclass)
        # see if subclass actually implements the interface
        return (hasattr(subclass, 'print_message') and callable(subclass.print_message) and
                hasattr(subclass, 'my_other_interface_function') and callable(subclass.my_other_interface_function) or
                NotImplemented)

    @abc.abstractmethod
    def print_message(self, message: str) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def my_other_interface_function(self):
        raise NotImplementedError


class MyABCClass(MySimpleABCInterface):
    def print_message(self, message: str) -> None:
        print("MyABCClass message:", message)

    def my_other_interface_function(self):
        print("MyABCClass: in my_other_interface_function!")


class NotMyABCClass(MySimpleABCInterface):                 # fails to implement all abstract methods
    def print_message(self, message: str) -> None:
        print("NotMyABCClass message:", message)


print("instantiating a MyABCClass object")
my_abc_class = MyABCClass()
print("instantiating a NotMyABCClass object")
try:
    my_not_abc_class = NotMyABCClass()
except TypeError:
    print("trying to instantiate an object that does not implement interface will throw a TypeError exception")

print("issubclass(MyABCClass, MySimpleABCInterface) =", issubclass(MyABCClass, MySimpleABCInterface))
# note the following will return True to say it is because you have defined methods in interface
print("issubclass(NotMyABCClass, MySimpleABCInterface) =", issubclass(NotMyABCClass, MySimpleABCInterface))
