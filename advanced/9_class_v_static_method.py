class MyClass:
    class_value = 5
    # this will be called when the class MyClass is instantiated as an object
    print("this is called when class object, not instance, is created", class_value)
    print("MyClass.class_value =", class_value)

    def __init__(self, new_class_value=5, new_instance_value=10):
        MyClass.class_value = new_class_value       # we need to reference the class object to change it
        self.instance_value = new_instance_value

    def set_value(self, new_value):
        """this is a BOUND method - it is bound to the instance object and receives self as the first argument"""
        # self.instance_value = new_value   <- this is obvious, it changes the instance_value object in the instance
        # MyClass.class_value = new_value  <- we know this will change all but what about...
        self.class_value = new_value    # <- this may not do what you think

    @classmethod
    def set_class_method_value(cls, new_value):     # difference is I get a class reference as a parameter
        """this is a BOUND method - it is bound to the class object and receives cls as the first argument"""
        cls.class_value = new_value

    @staticmethod
    def set_static_method_value(new_value):         # get neither self or cls reference
        """this method is not bound to the instance - no self. non-static unbound methods were removed in Python 3"""
        # we can't access the instance (self) or via a cls parameter but we could the class direct if we so wished
        # in reality this would be some related helper functionality to the method that doesn't change the class
        MyClass.class_value = new_value

    # this is however not allowed for some reason even though it is a class method
    # set_static_method_value(5)


print("\n")
print(f"MyClass is a class but is also an object {MyClass} at {id(MyClass)}")
print(f"we can access of class values at {id(MyClass.class_value)} directly")
print("MyClass.class_value =", MyClass.class_value)
print("\n")

my_instance = MyClass()
print(f"my_instance is an instance of the class and an object at {id(my_instance)}")
print(f"we can access of class values of the instance at the same address {id(my_instance.class_value)}")
print("my_instance.class_value =", my_instance.class_value)
print("\n")

print("...as such if we change the class value e.g. MyClass.class_value = 6, it changes in both class and instance...")
MyClass.class_value = 6
print("MyClass.class_value =", MyClass.class_value)
print("my_instance.class_value =", my_instance.class_value)
print("\n")

print("if we create a new instance with new class value it will effect all objects...")
print("new_instance = MyClass(new_class_value=8, new_instance_value=11)")
new_instance = MyClass(new_class_value=8, new_instance_value=11)
print("MyClass.class_value =", MyClass.class_value)
print("my_instance.class_value =", my_instance.class_value)
print("new_instance.class_value =", new_instance.class_value)
print("\n")

print("no MyClass.self.instance_value but we see my_instance.instance and new_instance.instance are different...")
print(f"my_instance.instance_value at {id(my_instance.instance_value)} of value {my_instance.instance_value}")
print(f"new_instance.instance_value at {id(new_instance.instance_value)} of value {new_instance.instance_value}")
print("\n")

print("what if i set the class value using the standard set_value() method...")
print("new_instance.set_value(15)")
new_instance.set_value(15)
print("MyClass.class_value =", MyClass.class_value)
print("my_instance.class_value =", my_instance.class_value)
print("new_instance.class_value =", new_instance.class_value)
print("\n")

print("perhaps not as expected now we have a naming conflict as we managed to create a new object...")
print(f"MyClass.class_value at {id(MyClass.class_value)} of {MyClass.class_value}")
print(f"new_instance.class_value at {id(new_instance.class_value)} of value {new_instance.class_value}")
print("the instance version of class_value (in new_instance only) is different to the class version of class_value")
print("\n")

print("using a class method would have been the way...")
print("MyClass.set_class_method_value(16)")
MyClass.set_class_method_value(16)
print("MyClass.class_value =", MyClass.class_value)
print("my_instance.class_value =", my_instance.class_value)
print("\n")

print("we can also use a static method but not really what it is for...")
print("MyClass.set_static_method_value(17)")
MyClass.set_static_method_value(17)
print("MyClass.class_value =", MyClass.class_value)
print("my_instance.class_value =", my_instance.class_value)
print("\n")

print("we can see how the various methods for the class MyClass are bound...")
print("MyClass.set_value is bound as %s" % MyClass.set_value)
print("MyClass.set_class_method_value is bound as %s" % MyClass.set_class_method_value)
print("MyClass.set_static_method_value is bound as %s" % MyClass.set_static_method_value)
print("\n")

print("we can see how the various methods for the instance my_instance are bound...")
print("my_instance.set_value is bound as %s" % my_instance.set_value)
print("my_instance.set_class_method_value is bound as %s" % my_instance.set_class_method_value)
print("my_instance.set_static_method_value is bound as %s" % my_instance.set_static_method_value)
print("\n")
