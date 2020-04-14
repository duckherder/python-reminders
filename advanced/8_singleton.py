import functools

# from https://realpython.com/primer-on-python-decorators/#creating-singletons
def singleton(cls):
    """make a class a singleton class (only one instance)"""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):     # this is the decoration which checks for previous existence
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
            print("in decoration: no instance exists, so let's create one!")
        else:
            print("in decoration: instance already exists!")
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton            # return instance of class, rather than function with other decorators

@singleton
class MySingleton:
    def __init__(self, parameter):
        self.parameter = parameter

    def do_some_stuff(self):
        print("parameter =", self.parameter)


print("create a MySingleton...")
my_singleton = MySingleton('my_parameter_string')       # MySingleton is really wrapper_singleton(MySingleton)
print("singleton at", id(my_singleton))
print("type(my_singleton) =", type(my_singleton))       # ..which returns a MySingleton instance
my_singleton.do_some_stuff()

print("create a another MySingleton...")
my_singleton_copy = MySingleton('my_other_parameter_string')       # this is wrapper_singleton(MySingleton)
print("singleton at", id(my_singleton_copy))
my_singleton.do_some_stuff()        # not what you might expect -> my_other_parameter_string ignored
