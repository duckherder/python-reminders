"""Everything in Python is an object."""

print("\nwe might expect the following two variables have different ids or addresses...")
my_first_int = 3
my_second_int = 3
print("my_first_int is at id", id(my_first_int))
print("my_second_int is at id", id(my_second_int))
print("..this is because in Python both variables bind to the same object, namely the object '3'")

my_first_string = 'hello!'
my_second_string = 'hello!'
print("my_first_string is at id", id(my_first_string))
print("my_second_string is at id", id(my_second_string))
print("...same again")

my_first_list = [1, 2, 3]
my_second_list = [1, 2, 3]
print("my_first_list is at id", id(my_first_list))
print("my_second_list is at id", id(my_second_list))
print("..but in this case they have different ids!")

# strings are immutable which means Python can use two different names to bind to the same
# object without any worries of changes being applied to a name affecting the bound object
# and thus silently modifying the value of another variable bound to the same object
print("this is because numbers and strings are immutable in Python, unlike lists which are mutable")
try:
    my_first_string[0] = 'y'
except TypeError:
    print("can't modify a string object - once created it is of fixed size in memory!")
print("but what if i do something like a += 'y'")
print("string is at", id(my_first_string))
# bind another name to this object
my_first_string_original = my_first_string
my_first_string += 'y'                              # add to string
print(my_first_string)                              # result looks as expected
print("resulting string is now at a different address - same name but new object",
      id(my_first_string))
print(f"but the original string '{my_first_string_original}'",
      "still exists at", id(my_first_string_original))

print("\nso what about tuples, they are immutable like strings and integers...")
my_first_tuple = (1, 2, 3)
my_second_tuple = (1, 2, 3)
print("my_first_tuple is at id", id(my_first_tuple))
print("my_second_tuple is at id", id(my_second_tuple))
print("yep, as expected the same ids")

print("if i modify what the variable points at it will change the id")
print("my_second_tuple", my_second_tuple)
my_second_tuple = (1, 2, 4)
print("my_second_tuple", my_second_tuple, "is now at id", id(my_second_tuple))
print("..but i can point it back to the original (1,2,3) tuple object")
my_second_tuple = (1, 2, 3)
print("my_second_tuple", my_second_tuple, "is now at id", id(my_second_tuple))

print("and obviously if my_third_tuple = my_second_tuple")
my_third_tuple = my_second_tuple
print("my_third_tuple", my_third_tuple, "is at same id", id(my_third_tuple))
print("and if my_third_list = my_second_list...")
# this is not a *copy* of values!!
my_third_list = my_second_list
print("my_third_list", my_third_list, "is at same id", id(
    my_third_list), "as my_second_list id", id(my_second_list))
print("...because in this case we are merely binding a new name to the same object, so if I modify 2nd")
print("...we are *not* creating a new object, just a new name - no copying of data is performed")
my_second_list[0] = 777
print("my_second_list", my_second_list)
print("my_third_list", my_third_list)
print("...and vice versa if I modify the 3rd list it will modify the second as well")
my_third_list[1] = -888
print("my_second_list", my_second_list)
print("my_third_list", my_third_list)


def my_function(a_list, an_integer, a_string) -> tuple:
    print("a_list at id", id(a_list))
    # this reference is immutable so can't be changed in function
    print("an_integer at id", id(an_integer))
    # this reference is also immutable
    print("a_string at id", id(a_string))
    print("all parameter ids are the same regardless of mutability - because they are passed by *reference*")
    print("...or like before simply binding a new name to the same object")
    print("a_list is another reference to my_list, which means I can change my_list in this function")
    a_list[0] = 99
    print("but surely i can change an_integer or a_string as well...")
    a_string = "my lovely new string"
    print("no, because we have not modified the string 'hello' but the changed the binding of a_string to a new object")
    print("a_string is now at id", id(a_string))
    _bool_result = an_integer < len(a_list)
    print("_bool_result at id", id(_bool_result))
    _local_list = [2, 3, 4]
    print("_local_list at id", id(_local_list))
    return _bool_result, _local_list


print("\nso what happens with variables when passed and returned from functions...")
my_list = [1, 2, 3]
my_integer = 1
my_string = 'hello'
print("my_list at id", id(my_list))
print("my_integer at id", id(my_integer))
print("my_string at id", id(my_string))
print("calling my_function")
bool_result, returned_list = my_function(my_list, my_integer, my_string)
print("returning from my_function shows new return variables bound to same objects that locals variables were bound")
# local object not destroyed just local binding
print("bool_result at id", id(bool_result))
# global variable binds to object created in function
print("returned_list at id", id(returned_list))
print("my_list has been modified in my_function:", my_list)
print("but my_string is not modified by my_function:", my_string)

print("\neverything is an object including None...")
print("None is an object at id", id(None))
print("None has attributes like any other object")
print(dir(None))
print("and a size of", None.__sizeof__())
print("my_function is an object at id", id(my_function))


class Bob:
    class_variable = [1, 2, 3]              # a mutable list

    def __init__(self, x):
        self.instance_variable = x


bob = Bob(3)
print("\ninstances of class Bob are objects obviously...")
print("id(bob) =", id(bob))
print("..with attributes of course")
print(dir(bob))

print("\nBUT the class Bob is also an object, not so obviously...")
print("id(Bob) =", id(Bob))
print("..with attributes")
print(dir(Bob))
print("note that instance_variable is not an attribute of the class, only the instance")
print("note that class_variable is an attribute of both the class and the instance")

robert = Bob(4)
print("\nrobert's instance variable is a different object to bob's...")
print("id(bob.instance_variable) =", id(bob.instance_variable))
print("id(robert.instance_variable) =", id(robert.instance_variable))
print("..but roberts and bob's mutable class variable is the same as class Bobs")
print("id(Bob.class_variable) =", id(Bob.class_variable))
print("id(bob.class_variable) =", id(bob.class_variable))
print("id(robert.class_variable) =", id(robert.class_variable))

print(
    "i can modify the class variable through the class as Bob.class_variable = ['bob', 'tim']")
Bob.class_variable = ['bob', 'tim']
print("Bob.class_variable =", Bob.class_variable)
print("bob.class_variable =", bob.class_variable)
print("robert.class_variable =", robert.class_variable)

print("but what if i modify the class variable through one of"
      "the instances as robert.class_variable = ['sally', 'susan']")
robert.class_variable = ['sally', 'susan']
print("Bob.class_variable =", Bob.class_variable)
print("bob.class_variable =", bob.class_variable)
# robert's class_variable is a conflicting instance variable
print("robert.class_variable =", robert.class_variable)
# note it is Bobs and bob's id that have changed
print("id(Bob.class_variable) =", id(Bob.class_variable))
print("id(bob.class_variable) =", id(bob.class_variable))
# object modified but at same id
print("id(robert.class_variable) =", id(robert.class_variable))
