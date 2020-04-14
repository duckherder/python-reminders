class MyClass:
    def __init__(self, a_value):
        self._my_value = a_value

    def get_value(self):
        return self._my_value

    def set_value(self, a_value):
        if type(a_value) is not int:
            raise TypeError("unsupported property type")
        self._my_value = a_value


print("we can create a normal class and has setters and getters...")
my_instance = MyClass(13)
my_instance.set_value(21)
print("my_instance._my_value =", my_instance._my_value)             # semi-private but accessible
print("my_instance.get_value() =", my_instance.get_value())         # better interface to use setters/getters

print("...but we can create a property that has get and set attributes...")
my_property = property()
print(my_property)
print(dir(my_property))


print("we can create a class with getters and setters properties defined...")
class MyPropertyClass:
    def __init__(self, a_value):
        self._my_value = a_value

    def get_value(self):
        print("getting value")
        return self._my_value

    def set_value(self, a_value):
        print("setting value to", a_value)
        if type(a_value) is not int:
            raise TypeError("unsupported property type")
        self._my_value = a_value

    # a property object is a data descriptor as it implements the __get__ and __set__ methods
    my_value_property = property(get_value, set_value, fdel=None, doc="my lovely horse")


my_instance = MyPropertyClass(7)
print("\nwe can inspect the attributes of the class property")
print("MyPropertyClass.my_value_property.fset =", MyPropertyClass.my_value_property.fset)
print("MyPropertyClass.my_value_property.fget =", MyPropertyClass.my_value_property.fget)
print("MyPropertyClass.my_value_property.fdel =", MyPropertyClass.my_value_property.fdel)
print("MyPropertyClass.my_value_property.__doc__ =", MyPropertyClass.my_value_property.__doc__)
print("\nand then make use of them...")
print("my_instance.my_value_property =", my_instance.my_value_property)     # calls get_value
print("my_instance.my_value_property = 6")
my_instance.my_value_property = 6               # this looks like we are reassigning class variable to object '6'
                                                # ... but in fact calls set_value() because it has __set__ defined
print("my_instance.my_property_value =", my_instance.my_value_property)
print("my_instance.my_property_value =", my_instance.my_value_property)
print("can still use setters/getters directly")
my_instance.set_value(13)
print(my_instance.get_value())
print(my_instance.my_value_property)


print("we can use property decorator...")
class MyPropertyDecoratedClass:
    def __init__(self, a_value):
        self._my_value = a_value

    @property                               # property is a class with getter, setter, deleter decorator functions
    def my_value(self):                     # with __init__ called as property.__init__(self, fget=my_value)
        print("getting value")
        return self._my_value

    @my_value.setter                        # my_value is a property with a setter attribute function
    def my_value(self, a_value):            # ..so effectively (property(my_value)).setter(my_value)
        print("setting value to", a_value)
        if type(a_value) is not int:
            raise TypeError("unsupported property type")
        self._my_value = a_value


my_instance = MyPropertyDecoratedClass(9)
print("my_instance.my_value =", my_instance.my_value)
my_instance.my_value = 4
print("my_instance.my_value =", my_instance.my_value)

my_second_instance = MyPropertyDecoratedClass(33)
print("my_instance.my_value =", my_instance.my_value)
print("my_second_instance.my_value =", my_second_instance.my_value)
