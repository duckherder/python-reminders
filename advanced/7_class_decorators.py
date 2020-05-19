"""Class decorators are classes that include functions as state."""

print("\ndefining a class decorator...")


class MyClassDecorator:

    def __init__(self, func):
        print("in __init__")
        self.func = func
        self.some_state = 0

    def __call__(self, *args, **kwargs):
        print("in __call__")
        print("do your decorating of args and kwargs here!")
        # update some state
        self.some_state += 1
        self.func(*args, **kwargs)


print("\nlet's define a non-decorated function...")


def my_function():
    print("in my_function")


print("\ndecorate the function using the class constructor...")
decorated_function = MyClassDecorator(my_function)
print("type(decorated_function)=", type(decorated_function))        # decorated function is in fact a class instance
print("now call the decorated function")
decorated_function()                                                # call the instance -> __call__ for "()" operator

print("\ndecorating my_function with the class decorator using @...")


@MyClassDecorator                                                   # with parameters this is effectively...
def my_function():                                                  # ...MyClassDecorator(my_function)
    print("in my_function")


print("call my_function")
my_function()                                                       # again this actually a class instance -> use "()"


print("########################")
print("\nwhat about parameters with a class decorator...")


class MyParameterisedClassDecorator:

    class MyLocalClassDecorator:                                      # you can create local class within class
        def __init__(self, func, a_parameter=False):                  # could have made it an external base class
            print("in MyLocalClassDecorator.__init__")                # so get_state() could be overloaded
            self.func = func
            self.parameter = a_parameter
            self.some_state = 0

        def __call__(self, *args, **kwargs):
            print("in MyLocalClassDecorator.__call__")
            print("do your decorating of args and kwargs here!")
            # update some state
            if self.parameter:
                self.some_state += 1
            return self.func(*args, **kwargs)

        def get_state(self):
            return self.parameter, self.some_state

    def __init__(self, _func=None, *, a_parameter=False):
        print("in MyParameterisedClassDecorator.__init__")
        self.parameter = a_parameter
        self.func = None
        if _func is not None:
            # decorator has been created like this MyParameterisedClassDecorator(my_function)
            print("no parameters have been specified as _func is", _func)
            self.func = MyParameterisedClassDecorator.MyLocalClassDecorator(_func, a_parameter=self.parameter)

    def __call__(self, *args, **kwargs):
        print("in MyParameterisedClassDecorator.__call__")
        if self.func is None:     # has been called like this MyParameterisedClassDecorator(a_parameter=2)(my_function)
            if len(args) != 1 or not callable(args[0]):
                raise ValueError("expecting only a single function to decorate!")
            self.func = MyParameterisedClassDecorator.MyLocalClassDecorator(args[0], a_parameter=self.parameter)
            return self.func
        return self.func(*args, **kwargs)

    def get_state(self):
        # in case where parameters are used my_function will be a MyParameterisedClassDecorator object
        if self.func is None:
            raise ValueError("undecorated function!")
        return self.func.get_state()


print("\ndecorating my_function without parameters...")


@MyParameterisedClassDecorator
def my_function(my_function_parameter):
    print("in my_function:", my_function_parameter)


print("calling my_function")
my_function('non-parameterised class')
print("my_function is an MyParameterisedClassDecorator so can access as such")
print("type(my_function) =", type(my_function))
print("my_function.func.parameter =", my_function.func.parameter)
print("my_function.func.state =", my_function.func.some_state)
print("my_function.get_state() =", my_function.get_state())         # use a method to get state

print("\ndecorating my_function with parameters...")


@MyParameterisedClassDecorator(a_parameter=True)
def my_function(my_function_parameter):
    print("in my_function:", my_function_parameter)


print("calling my_function")
my_function('parameterised class')
my_function('parameterised class')
print("my_function is an MyParameterisedClassDecorator.MyLocalClassDecorator object so can access as such")
print("type(my_function) =", type(my_function))
print("my_function.parameter = ", my_function.parameter)
print("my_function.state = ", my_function.some_state)
print("my_function.get_state() =", my_function.get_state())
