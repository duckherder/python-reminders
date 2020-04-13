# quotation types: python supports single, double and triple quotations
my_string_single = 'Hello world'
my_string_double = "Hello again world"
my_multi_line_string = '''This is a string
over two lines'''

print("we can see that these are of type 'str'")
print(type(my_string_single))

# quotes within quotes
my_nested_string = "my nested 'string'"
print("we can nest quotes within quotes")
print(my_nested_string)

my_nested_string = 'my nested "string"'
print(my_nested_string)

# concatenation
print("you can " + "concatenate" + " strings like this")
print('you can ' + "mix" + ' quotes but not recommended')

# repetition with the * operator
bob = "again.." * 5
print(bob)

# escape characters
print("this is a \n string with the '\\n' escape character")
print('this works for single\n quoted strings as well')

# strings have methods and you can apply method direct to literals
print("capitalise this sentence with a method.".capitalize())
print("concatenate using ".join("the join method"))

# formatting
my_integer = 10
# variable string parameters to print, no space required
print("integer value is", my_integer)
# using string formatting
print("integer value is %d" % my_integer)
print("integer value is {0}".format(my_integer))        # using format method
print("integer value in hex 0x{bob:X}".format(bob=my_integer))
big_number = 100000000
print("big number in thousands {0:,}".format(big_number))

# remember that formatting is a property of strings and not print
formatted_string = "with formatted string the integer value is %d" % my_integer
print(formatted_string)


def print_hex(my_string):
    """Print a string in hexidecimal."""
    print(":".join("{:02x}".format(ord(c)) for c in my_string))


# raw strings using the r prefix
raw_string = r"\n"
normal_string = "\n"
print("compare ASCII hex of a raw string with the new line string versus normal string with ASCII line feed")
print_hex(raw_string)
print_hex(normal_string)

# unicode and UTF-8
my_string = 'A unicode # string'
# in Python 3 all strings are unicode by default, so no need for u prefix
my_ustring = 'A unicode \u018e string'
# strings are actually of same length as unicode code point only counts as one character
print("my_string length = %d" % len(my_string))
print("my_ustring length = %d" % len(my_ustring))

# isascii new in Python 3.7
print("is my_string ascii: %r" % my_string.isascii())
print("is my_ustring ascii: %r" % my_ustring.isascii())

# this string is ASCII so UTF-8 mapping is one to one
utf8_encoded = my_string.encode('utf-8')
print("converting to UTF converts a string into a series of bytes, hence the b prefix when printing")
print(utf8_encoded)
print(type(utf8_encoded))

# see https://en.wikipedia.org/wiki/UTF-8 for how utf-8 encoding works for
# non-ASCII characters such as Unicode code points > 128
print("converting Unicode code points to UTF-8")
utf8_encoded = my_ustring.encode('utf-8')
# here you see the large Unicode value 0x018e being encoded as 2 bytes \xc6\x8e
print(utf8_encoded)

print("decoding the UTF-8 bytes back to a Unicode string")
recovered_ustring = utf8_encoded.decode('utf-8')
print(recovered_ustring)
print(type(recovered_ustring))

# character conversions
ord_value = ord('a')
print(ord_value)
print(type(ord_value))
ord_value = ord('\u018e')
print(ord_value)
print(type(ord_value))

# and back again using chr
print(chr(ord_value))

# f-strings
print("f-strings are available in Python 3")
my_integer = 10
my_list = ['bob', 'dave']
my_fstring = f"integer = {my_integer} and my_list is {my_list}"     # uses the f-prefix
print("my_fstring:", my_fstring)
print("you can call functions in f-strings...")
my_fstring = f"integer**2 = {my_integer**2} and max(my_list) is {max(my_list)}"     # uses the f-prefix
print("my_fstring:", my_fstring)
print("use same formatting as with format...")
print(f"integer = 0x{my_integer:02X}")
