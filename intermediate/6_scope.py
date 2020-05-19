"""LEGB Python scope

Local: variables defined in a function are local to that function
Enclosing: local scope but
Global: variable defined in module level or variable with 'global' keyword
Built-in: preassigned names in Python

this is the order in which names are resolved in Python
"""
my_global_variable = 1          # an immutable integer of global scope
my_global_list = [1, 2, 3]

MY_GLOBAL_LIST = [1, 2, 3]      # not syntactically required but globals are usually in capitals
_MY_GLOBAL_LIST = [1, 2, 3]     # use underscore if we don't want this to be exported to another module


def my_function(my_parameter_variable):
    print("function parameter my_parameter_variable with value", my_parameter_variable,
          "at id", id(my_parameter_variable), "is bound to same object as global my_global_variable")
    # we can read immutable globals
    print("my_global_variable =", my_global_variable)
    # we can read mutable globals
    print("my_global_list =", my_global_list)
    print("local namespace =", locals())
    # reassign local parameter variable
    my_parameter_variable = 2
    print("my_global_variable remains same after my_parameter_variable binding changed =",
          my_global_variable)
    print("add new local scoped variable my_local_variable")
    my_local_variable = 3
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


print("\nglobal variables...")
print("my_global_variable of value", my_global_variable,
      "at id", id(my_global_variable))
print("global namespace =", globals())

print("\nfunctions such as my_function() are in the global scope as well as variables such my_global_list...")
print("calling my_function with my_global_variable as a parameter with id =", id(my_global_variable))
my_function(my_global_variable)
print("returned from my_function")
print("global namespace =", globals())
print("my_local_variable is not in the global namespace")
try:
    print(my_local_variable)
except NameError:
    print("don't know about a locally scoped variable at module level")

print("\nmodifying a global variable from a function...")
my_bad_global_modifier_function()
my_ok_global_modifier_function()


def my_nested_func():
    my_conflict_name = "'my_nested_func level'"
    my_enclosing_variable = 'bob'

    def my_func_in_func():                                          # locally scoped function
        # name conflicts with enclosing variable name
        my_conflict_name = "'inner my_func_in_func level'"
        # we will use locally scoped version first over the enclosing variant
        print("in my_func_in_func locally scoped function, set my_conflict_name =",
              my_conflict_name, " at id", id(my_conflict_name))
        # not found in local scope, so try enclosing
        print("my_enclosing_variable =", my_enclosing_variable)
        # not found in local, enclosing, so try global
        print("my_global_variable =", my_global_variable)

    def my_func_in_func_modifier():
        # tell interpreter i'm going to modify a non-local (not global)
        nonlocal my_enclosing_variable
        print("using nonlocal in my_func_in_func_modifier() to modify my_enclosing_variable")
        my_enclosing_variable = 'sally'

    print("my_nested_func locals =", locals())
    print("calling my_func_in_func() which is a locally scoped function")
    my_func_in_func()
    print("returned from my_func_in_func()")
    print("in enclosing function my_conflict_name =",
          my_conflict_name, "at id", id(my_conflict_name))
    print("calling my_func_in_func_modifier()")
    my_func_in_func_modifier()
    print("my_enclosing_variable has been modified:", my_enclosing_variable)


print("\nnested functions...")
print("calling my_nested_func()")
my_nested_func()
print("returned from my_nested_func(), try to call my_func_in_func() directly")
try:
    my_func_in_func()
except NameError:
    print("don't know about a locally scoped function at module level")

print("\nfunction overloading of built-ins is possible...")
my_list = [1, 2, 3]
print("not defined yet so using built-in version")
print("max(my_list) =", max(my_list))


def max(a_list):                                # bad thing to do but Python doesn't stop us
    print("using globally scoped version, not built-in")
    return 'whoops'


print("interpreter finds max at global scope before built-in scope as defined by LEGB")
print("max(my_list) =", max(my_list))
