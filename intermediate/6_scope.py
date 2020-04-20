"""LEGB Python scope

Local: variables defined in a function are local to that function
Enclosing: local scope but
Global: variable defined in module level or variable with 'global' keyword
Built-in: preassigned names in python

this is the order in which names are resolved in python
"""
my_global_variable = 1          # an immutable integer of global scope
my_global_list = [1, 2, 3]

MY_GLOBAL_LIST = [1, 2, 3]      # not syntactically required globals are usually in capitals
_MY_GLOBAL_LIST = [1, 2, 3]     # use underscore if we don't want to be export this to another module


def my_function(my_parameter_variable):
    print("incoming local scope parameter value", my_parameter_variable,
          "at id", id(my_parameter_variable), "is bound to global my_global_variable")
    # we can read immutable globals
    print("my_global_variable =", my_global_variable)
    # we can read mutable globals
    print("my_global_list =", my_global_list)
    print("local namespace =", locals())
    # reassign local parameter variable
    my_parameter_variable = 2
    print("my_global_variable after my_parameter_variable binding changed =",
          my_global_variable)
    my_local_variable = 3                           # add new variable to local scope
    print("local namespace =", locals())


def my_bad_global_modifier_function():
    try:
        my_global_variable = 2
    except UnboundLocalError:
        print("python won't allow you to write to a global object from a function directly")


def my_ok_global_modifier_function():                       # not a great thing to do but code correct
    print("python will allow you to write to a global object from a function if you tell it about the global")
    # better to tell interpreter we mean to change
    global my_global_variable
    # ...the global scope variable
    print("my_global_variable =", my_global_variable)
    my_global_variable = 2


print("my_global_variable of value", my_global_variable,
      "at id", id(my_global_variable))
print("global namespace =", globals())
print("note that my_function functions etc are in the global scope as well as my_global*")

my_function(my_global_variable)
print("global namespace =", globals())
print("my_local_variable is not in the global namespace")
try:
    print(my_local_variable)
except NameError:
    print("don't know about a locally scoped variable at module level")

my_bad_global_modifier_function()
my_ok_global_modifier_function()


def my_nested_func():
    my_conflict_name = "'my_nested_func level'"
    my_enclosing_variable = 'bob'

    def my_func_in_func():                                          # locally scoped function
        # name conflicts with enclosing variable name
        my_conflict_name = "'inner my_func_in_func level'"
        # we will use locally scoped version first over the enclosing variant
        print("hello from locally scoped function, my_conflict_name =",
              my_conflict_name, " at id", id(my_conflict_name))
        # not found in local scope, so try enclosing
        print("my_enclosing_variable =", my_enclosing_variable)
        # not found in local, enclosing, so try global
        print("my_global_variable =", my_global_variable)
        print("i can set the enclosing variable using nonlocal")

    def my_func_in_func_modifier():
        # tell interpreter i'm going to modify a non-local
        nonlocal my_enclosing_variable
        my_enclosing_variable = 'sally'

    print("my_nested_func locals =", locals())
    print("my_func_in_func() is a local scope function")
    my_func_in_func()
    print("my_conflict_name in enclosing function =",
          my_conflict_name, " at id", id(my_conflict_name))
    my_func_in_func_modifier()
    # not found in local scope, so try enclosing
    print("modified my_enclosing_variable =", my_enclosing_variable)


my_nested_func()
try:
    my_func_in_func()
except NameError:
    print("don't know about a locally scoped function at module level")

my_list = [1, 2, 3]
# not defined yet so using built-in version
print("max(my_list) =", max(my_list))


def max(a_list):                                # bad thing to do but Python doesn't stop us
    print("using globally scoped version, not built-in")
    return 'whoops'


# interpreter finds max at global scope before built-in scope
print("max(my_list) =", max(my_list))
