"""context managers allow for clean allocation and de-allocation of resources resources regardless"""

try:
    with open('15_context_manager.py', 'r') as f:
        raise ValueError("raising some random exception")
except ValueError:
    print("file will be closed by with statement regardless of exception...")


class MyContextManager:
    def __init__(self, swallow_exception=False):
        print("creating context manager")
        self.resource_handle = 99
        self.swallow_exception = swallow_exception

    def __enter__(self):
        print("creating context manager resources")
        return self.resource_handle

    def __exit__(self, exc_type, exc_val, exc_tb):      # don't re-raise exceptions here
        print(f"freeing up context manager resources for handle {self.resource_handle}")
        print("exc_type =", exc_type)       # will all be None if no exception
        print("exc_val =", exc_val)
        print("exc_tb =", exc_tb)
        return self.swallow_exception if exc_tb is not None else False

print("we can create our own context manager...")
my_context_manager = MyContextManager()

try:
    with my_context_manager as handle:
        print("in 'with' block")
except ValueError:
    pass


print("if exception raised in our own context manager...")
try:
    with my_context_manager as handle:
        print("in 'with' block, raising exception")
        raise ValueError("raising some random exception")
except ValueError:
    print("exception: handle resources freed regardless of exception")


print("if exception raised in our own context manager we can swallow it if we wish...")
my_context_manager = MyContextManager(swallow_exception=True)
try:
    with my_context_manager as handle:
        print("in 'with' block, raising exception")
        raise ValueError("raising some random exception")
except ValueError:
    print("exception: should not be here!")
print("no exception raised!")
