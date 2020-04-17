"""for disassembling Python byte code"""
import dis
import traceback
import sys

# see https://docs.python.org/3/library/dis.html
# see https://en.wikipedia.org/wiki/Stack-oriented_programming
print("Python is a stack-orientated language...")
print("..there are 3 stacks: call, data (python code/function evaluation) and block (control structures)")

def my_function(x, y):
    _z = x + y
    print(_z)
    try:
        f = open('my_file.txt', 'r')
    except FileNotFoundError:
        pass
    return _z

print("\ndisassemble an object - module, class, method, function etc...")
dis.dis(my_function)

print("\nshow code information...")
print(dis.code_info(my_function))

print("\nwe can also access code information through the __code__ attribute of a function...")
print(my_function.__code__)
print("literals =", my_function.__code__.co_consts)             # any literals in the code
print("locals =", my_function.__code__.co_varnames)             # local variables
print("non-locals =", my_function.__code__.co_names)            # non-local names referenced

print("\nget Instructions using an iterator...")
my_instructions = dis.get_instructions(my_function)
for instruction in my_instructions:
    print(f"opcode: {instruction.opcode} opname: {instruction.opname} arg: {instruction.arg}")

print("difference between [] and list()....")
print("[] =")
dis.dis("[]")
print("list() =")
dis.dis("list()")
print("you can see why [] is faster...")

my_list = [1, 2, 3]
try:
    print(my_list.womble)
except AttributeError as e:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print("print traceback object...")
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
    print("print traceback object from exception attribute...")
    print("type(e.__traceback__) =", type(e.__traceback__))
    traceback.print_tb(e.__traceback__, limit=1, file=sys.stdout)

def my_function():
    print("print stack...")
    traceback.print_stack()

my_function()

def my_function():
    _my_list = [1, 2, 3]
    try:
        print(_my_list.womble)
    except AttributeError as e:
        print("disassemble the last traceback in my_function()...")
        dis.distb(e.__traceback__)

my_function()

print("\nsee https://github.com/python/cpython/blob/master/Include/opcode.h for opcode header file")

