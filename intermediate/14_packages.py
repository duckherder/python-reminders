import my_package as bernard                        # import package and rename
# import module from locally defined my_package
from my_package import fab
import my_package.roger                             # ...is an alternative
# import class from fab module in my_package and rename
from my_package.fab import MyFabClass as Tina
# import all public APIs and variables
from my_package.public_function import *
from datetime import *                              # generally not recommended as you may import name conflicts
                                                    # ...with other modules or reduce readability in code
bernard.fab.my_fab_function('bernard?')

print("use fab module directly to access classes, functions and module variables...")
instance = fab.MyFabClass(1)
fab.my_fab_function('hello')
print(fab.MY_FAB_GLOBAL_VARIABLE)

print("use imported classes names...")
tina = Tina(3)

print("we can use dir() on this import module")
print(dir(fab))
print("fab __name__ =", fab.__name__)

bernard.hello_roger()
try:
    print(bernard.ROGER_GLOBAL_VARIABLE)
except AttributeError:
    print("don't know about this variable")

print("but i do know about this one:", bernard.ROGER_GLOBAL_PUBLIC_VARIABLE)
print("..and i can get at the other one like this:",
      my_package.roger.ROGER_GLOBAL_VARIABLE)

my_public_function()            # function imported from public_function module
try:
    my_private_function()
except NameError:
    print("can access this function as not imported as not in modules __all__ list")

print("but if we know about it we can access it...")
my_package.public_function.my_private_function()
