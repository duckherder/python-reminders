import os
import datetime

# simple printing
print("hello world!")
# pass multiple parameters, will be separated by a ' '
print("hello", "world!")
# you can change separator
print("hello", "world!", sep='@')
# you can change terminator
print("hello", "world!", end=':end of the line!\n\n')
# you can send objects of different types, no conversion
print("hello my values is", complex(1, 4))
# if use string concatenation need to convert and add space
print("hello my values is " + str(complex(1, 4)))

# get input from the command line
print("get a string from the command line")
my_input_string = input("Enter a string here: ")
print(my_input_string)

# input in Python 2.x would evaluate the input string - try string 'print("bob")'
if len(my_input_string):
    eval(my_input_string)       # this will do what input used to do

print("open a file called 'test.txt'")
file_object = open("test.txt", "w")
print("filename =", file_object.name)
print("open mode =", file_object.mode)
file_object.write("Hello!\n")
file_object.close()
print("file closed:", file_object.closed)

print("all attributes of a file object")
print(dir(file_object))

with open("test.txt", "a") as file_object:            # with is a better to open a file, example of a context..
    # empty line with just new line                   # ..manager for managing resource - no need to call close()
    file_object.write("\n")
    file_object.write("I'm the third line!\n")

print("read entire contents using read()...")
with open("test.txt", "r") as f:
    contents = f.read()
print("contents is of type", type(contents))
print(contents)                     # will be a string with embedded line feeds

print("read line by line using readline()...")
with open("test.txt", "r") as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line.strip())          # strip the line feed character

print("read first 5 characters at a time from every line using readline()...")
with open("test.txt", "r") as f:
    while True:
        line = f.readline(5)
        if not line:
            break
        print(line)

print("read all lines using readlines()...")
with open("test.txt", "r") as f:
    all_lines = f.readlines()
print("all_lines is of type", type(all_lines))
print(all_lines)                    # list of strings with line feeds

print("deleting the file")
os.remove("test.txt")

with open("test.dat", "wb") as file_object:                     # open as binary file for writing
    file_object.write(bytes([0x01, 0x01, 0x02, 0x03, 0x04]))    # write 5 bytes

with open("test.dat", "rb") as f:
    # seek to 0 offset from end of file
    f.seek(0, 2)
    # use tell to see how many bytes
    number_bytes = f.tell()
    print("number of bytes =", number_bytes)
    # go back to start of file
    f.seek(0, 0)
    contents = f.read(number_bytes)                             # read contents
    # binary files so read bytes, not list or string
    print("contents of type", type(contents))
    print("length of contents =", len(contents))
    print(contents)

print("can use os to find file size")
number_bytes = os.path.getsize("test.dat")
print("number of bytes = ", number_bytes)
os.remove("test.dat")

print("you can check if file exists before opening")
print("does test.txt exist?", os.path.exists("test.txt"))

# file may be moved/deleted since testing
print("but better to attempt to open with a try...")
try:
    f = open("test.txt", "r")
except FileNotFoundError:                                       # subclasses IOError
    print("unable to find file for reading!")

print("difference between %r and %s")
time = datetime.datetime.now()
# prints string - uses __str__ object attribute - how a user might want to see it
print("%s" % time)
# prints representation using __repr__ attribute - how programmer might want it
print("%r" % time)
