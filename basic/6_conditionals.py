"""How to use conditional statements in Python."""

print("\nPython has a boolean type...")
print("bool(): convert to a boolean")
print("integer 0 means", bool(0))
print("integer 17 means", bool(17))
print("integer -17 means", bool(-17))


def my_function(x):
    # standard if, elif, else structure for controlling control paths
    if x == 3:                          # there is no switch statement in Python
        print("interesting value")
    elif x == 4:
        print("that even it out")
    else:
        print("something else")


print("\nwe can use membership operators to test whether an object is in a list etc..")
if 2 in [1, 2, 3]:
    print("2 is in the list")

my_dict = {'bob': 1, 'tim': 2}
if 'bob' in my_dict:            # replaces has_key() in Python 2
    print("found bob")
if 'sally' not in my_dict.keys():     # more verbose version
    print("no sally")

list_a = [1, 2, 3]
list_b = [1, 2, 3]

print("\nuse comparison operator '==' to test for same value...")
print("list_a =", list_a)
print("list_b =", list_b)
if list_a == list_b:
    print("lists a and b have the same values - they are equal")

print("but equality does not imply identical!")
if list_a is not list_b:
    print("..same values but lists a and b are different objects as lists are mutable")

x = None                    # set to empty state
if x is None:               # should use 'is' instead of '=='  -> saying x is the same object as None
    print("x is None")      # None has no value to compare against

x = True
if x == True:
    print("x has the value True")
    print(x)

if x is True:       # preferred
    print("x is the same object as True")
    print(id(x))
    print(id(True))

print("\noperators like '>=' generate booleans...")
x = 4
y = 3
result = 4 >= 3
print(type(result))
print(result)

print("\nand, or, not can operate on bool True and False objects...")
if x >= y and not y > 5:                        #
    print("condition met!")

print("\nwe can use ternary conditional statements like 'result = True if x == 4 else False'...")
result = True if x == 4 else False
print(result)
