"""Some examples of how to add comments to Python code."""

# This is a comment
# and also like this

"""You can add comments like this to your code"""

"""You can do
this for multi-line comments 
as well"""

"""
or like this style if you prefer
"""


def print_function(my_string):
    '''You can use triple quoted ones here - these are called docstrings
    and should prescribe the functions effect as a command according to PEP0257'''

    # they should be indented the same as the code below
    if my_string is None:
        # comment with correct indentation
        print("string is None")
        return
    print(my_string)                # you can add them like this as well


def pretty_print_function(my_string) -> bool:
    """Print a user defined string.        -> according to PEP0257 triple double quotes are preferred for docstrings
                                           -> also note that description should end in a period (full stop)
    :param my_string:     String to print
    :return:              True if successful, False otherwise   -> note no blank lines before or after docstring
    """
    if my_string is None:
        print("string is None!")
        return False

    # print the string -> example of redundant commenting - legal but unnecessary
    print(my_string)
    return True


# triple quoted comments in the first the line after a start of a module,
# function, class or method are called docstrings and can be
# printed in code elsewhere. __doc__ is an attribute of the
# function object named pretty_print_function
print(pretty_print_function.__doc__)
