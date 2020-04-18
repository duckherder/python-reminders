my_generator = (x for x in range(5, 10))
my_code_to_execute = "print(next(my_generator))"
print("use eval to evaluate a string as code...")
eval(my_code_to_execute)
eval(my_code_to_execute)

def my_function(name):
    print(f"hello {name} from my_function")

my_code_to_execute = "my_function('bob')"
eval(my_code_to_execute)
eval("my_function('sally')")
try:
    # eval is obviously dangerous as you may not know where the string has originated, such as from input()
    eval('print("hello")', {'__builtins__': None}, {})          # input() does not evaluate in Python 3
except TypeError:
    print("this eval will fail as print() not in globals")
# the globals add locals parameters allow some protection on what may be used by eval
eval(my_code_to_execute, {'__builtins__': None, 'my_function': my_function}, {})    # just allow my_function
my_code_to_execute = "eval('print(" + '"nested hello eval!"' + ")')"
eval(my_code_to_execute)
try:
    eval(my_code_to_execute, {'__builtins__': None, 'my_function': my_function}, {})
except TypeError:
    print("this eval will fail again as eval() not in globals")

print("you can use compile to create a code object that can be evaluated later...")
eval_code_object = compile("my_function('tim')", '', 'eval')
eval(eval_code_object)
try:
    eval_code_object = compile("my_function('tim')\nprint('hello function, from tim!')", '', 'eval')
except SyntaxError:
    print("exception: evaluations must be single expression strings")
print("for multi-expressions strings use exec()")
exec("my_function('tim')\nprint('hello function, from tim!')")
print("..also compatible with compile...")
exec_code_object = compile("my_function('tim')\nprint('hello function, from tim!')", '', 'exec')
exec(exec_code_object)
