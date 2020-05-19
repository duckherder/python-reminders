"""Use of different types of supported numbers in Python."""

import math

print("\nbasic numbers types are int, float and complex...")
a = 8
b = 10.0
c = 3+4j
d = complex(3, 4)

print("\nuse type() to tell you what Python believes the type to be...")
print(type(a))
print(type(b))
print(type(c))
print(d)

print("\nuse isinstance() built in function to see if it is the type we believe it is or should be...")
print("is 5 an integer", isinstance(5, int))
print("is 'hello' a float", isinstance("hello", float))

# like anything in Python everything is an object and has attributes and an address
# ..even an integer value
print("\nall objects, even number objects such as '0', have attributes and an 'address'")
print("attributes = ", dir(0))
print("address = ", id(0))


def factorial(n):
    """Compute factorial of n, n!"""
    if n <= 1:
        return 1
    return n * factorial(n-1)


# In Python 3 there is only the integer class and that
# does not have a size limit. There are is no 'long' type any more or L literal.
# See how the object size increases automatically dependent on value.
# Note that the size is the object size not the size of the representation
print("\nvalues of n! factorial with increasing n...")
for i in range(1, 100):
    result = factorial(i)
    print("%d! = %d of type %s (object size=%d, bit length=%d)" %
          (i, result, type(result), result.__sizeof__(), result.bit_length()))

# where does the size change?
# use brackets so parser doesn't confuse integer...
print("value of 0 object size = %d" % (0).__sizeof__())
# ...for float when reading left to right
print("value of 1 object size = %d" % (1).__sizeof__())
print("value of 2^30-1 object size = %d" % (pow(2, 30) - 1).__sizeof__())
print("value of 2^30 object size = %d" % (pow(2, 30)).__sizeof__())
print("value of 2^60-1 object size = %d" % (pow(2, 60) - 1).__sizeof__())
print("value of 2^60 object size = %d" % (pow(2, 60)).__sizeof__())

print("\ndivisions in Python 3 result in a float even if numerator and denominator are both int objects...")
a = a / 2
print(type(a))

print("you can cast back to a integer")
a = int(a)
print(type(a))

print("\ncasting a float to an integer is towards 0...")
a = int(1.999999)
print("int(1.999999) = %d" % a)
a = int(0.999999)
print("int(0.999999) = %d" % a)
a = int(-0.999999)
print("int(-0.999999) = %d" % a)
a = int(-1.999999)
print("int(-1.999999) = %d" % a)

# various mathematical functions are built into Python, or available from math package
print("\nsome useful math functions...")
print("abs(-1) = %d" % abs(-1))
print("math.ceil(1.5) = %d" % math.ceil(1.5))       # round up
print("math.floor(1.5)= %d" % math.floor(1.5))      # round down
print("round(1.6) = %d" % round(1.6))               # rounding to nearest
print("round(1.4) = %d" % round(1.4))
print("math.pi = %f" % math.pi)
print("divmod(17, 3) =", divmod(17, 3))             # returns quotient and remainder
# convert to a binary string
print("bin(10) =", bin(10))
print("bin(31) =", bin(31))
print("oct(8) =", oct(8))                          # convert to octal string
print("sum([1, 2, 3]) =", sum([1, 2, 3]))          # sum a list of numbers
print("pow(2, 4) =", pow(2, 4))                    # power function
print("2**4 =", 2**4)
