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


# checking for list membership
print("we can use membership operators to test whether an object is in a list etc..")
if 2 in [1, 2, 3]:
    print("2 is in the list")

my_dict = {'bob': 1, 'tim': 2}
if 'bob' in my_dict:            # replaces has_key() in Python 2
    print("found bob")
if 'sally' not in my_dict.keys():     # more verbose version
    print("no sally")

list_a = [1, 2, 3]
list_b = [1, 2, 3]

if list_a == list_b:                # use comparison operator to compare values
    print("lists have the same values - they are equal")

print("but equality does not imply identical!")
if list_a is not list_b:
    print("..same values but different objects as lists are mutable")

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

x = 4
y = 3
result = 4 >= 3
print(type(result))
print(result)

if x >= y and y < 5:                        # and, or, not operate on bool True and False objects
    print("use of logical and operator")

print("we can use ternary conditonals...")
result = True if x == 4 else False
print(result)
