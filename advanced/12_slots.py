"""__slots__ attribute is capable of reducing memory overheads associated with __dict__."""

from pympler import asizeof


class MyClassWithoutSlots(object):
    def __init__(self, x):
        self.x = x
        self.y = 'hello' + str(x)
        self.z = x * 113.8


class MyClassWithSlots(object):
    # instead of class variables being stored in __dict__ known variables can be stored in __slots__
    __slots__ = ['x', 'y', 'z']

    def __init__(self, x):
        self.x = x
        self.y = 'hello' + str(x)
        self.z = x * 113.8


my_instance_without_slots = MyClassWithoutSlots(1)
my_instance_without_slots.dynamic_value = 1
my_instance_with_slots = MyClassWithSlots(1)
try:
    my_instance_with_slots.dynamic_value = 1
except AttributeError:
    print("with __slots__ defined we can not add new dynamic variables after creation")

my_instance_without_slots = MyClassWithoutSlots(1)
my_instance_with_slots = MyClassWithSlots(1)
print(dir(my_instance_without_slots))
print(dir(my_instance_with_slots))
print(my_instance_without_slots.__dict__)
print(my_instance_with_slots.__slots__)

my_instance_list_without_slots = [MyClassWithoutSlots(x) for x in range(1000)]
my_instance_list_with_slots = [MyClassWithSlots(x) for x in range(1000)]

# storing variables in __slots__ rather than __dict__ can save significant amount of RAM
print("memory required for 1000 object without slots =", asizeof.asizeof(my_instance_list_without_slots))
print("memory required for 1000 object with slots =", asizeof.asizeof(my_instance_list_with_slots))
