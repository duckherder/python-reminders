"""underscores are often used for variable names"""

_MY_GLOBAL_VARIABLE = 'please do not import me'     # prevents modules that import this one being polluted by
                                                    # ...this global (to this module) variable


class TotalGenerator:
    def __init__(self):
        # infers that _total is semiprivate, this is simply convention
        self._total = 7
        # considered super-private to prevent accidental access
        self.__mangled_total = 13
        self.__builtin_total__ = 99         # typically reserved for built in types

    def __SuperPrivateMethod(self):
        print("what are doing here!")


my_total = TotalGenerator()
print("my_total._total =", my_total._total)
print("my_total.__builtin_total__ =", my_total.__builtin_total__)

print("my_total.__mangled_total =")         # this is special
try:
    print(my_total.__mangled_total)
except AttributeError:
    print("interpreter won't allow this sort of shenanigans")

print("..but for the persistent and naught programmer we can access through mangled name")
print(my_total._TotalGenerator__mangled_total)

print("same for super-private methods")
try:
    my_total.__SuperPrivateMethod()
except AttributeError:
    print("interpreter won't allow this sort of shenanigans")
print("..but again we can circumvent..")
my_total._TotalGenerator__SuperPrivateMethod()

print("underscores are used by convention to mean don't care")
my_dict = {'bob': 1, 'tim': 2, 'ray': 3}
for key, _ in my_dict.items():                  # don't care about the value just the key (or you can use keys())
    print("key: ", key)

print("underscores can be used to make numbers more readable")
my_number = 93203
print(my_number)
my_number = 93_203
print(my_number)
