print("simple loop of 10, range returns an iterable")
for i in range(10):
    print(i)

print("loop through odd numbers with a conditional break")
for i in range(1, 10, 2):       # range(start, stop, step)
    print(i)
    if i == 5:
        break       # conditional loop break, stop looping

print("loop and print only even numbers using continue")
for i in range(10):
    if i % 2:
        continue    # skip rest and continue looping
    print(i)        # print even numbers

print("while loops are supported")
while True:                             # you can use any conditional to control when to stop
    print("Hello")
    break

print("lists are iterable")
my_list = [1, 2, 3]                     # lists are iterable
for value in my_list:
    print(value)

print("so are strings")
for char in "Hello World":
    print(char)

print("..so are dictionaries but not directly - use items()")
my_dict = {'bob': 1, 'tim': 2, 'ray': 3}
for key, value in my_dict.items():
    print("key: ", key, "  value: ", value)

print("nesting loops is also possible")
counter = 0
for index in my_list:
    for key, value in my_dict.items():
        counter += 1
print("looped %d times!!" % counter)

print("loops can have an else construct for when loop terminates")
for i in range(3):
    print(i)
else:
    print("Done")

print("if we need the index we can use enumerate")
# use enumerate rather than range(len(my_list))
for index, value in enumerate(my_list):
    print("index=", index, "value=", value, "(%d)" % my_list[index])
