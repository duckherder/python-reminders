print("you can use slicing to access into lists")
my_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_list)

print("use [n] to access a specific item")
print("my_list[2] =", my_list[2])

print("use [-n] to access a specific item from the end backwards")
print("my_list[-1] = ", my_list[-1])

print("use [start:end] to return a slice that includes start but not end")
print("my_list[0:2] =", my_list[0:2])
print("my_list[1:4] =", my_list[1:4])

print("use [start:] to return a slice that includes start and all the way to the last item")
print("my_list[4:] = ", my_list[4:])

print("use [:end] to return a slice that includes everything up to but excluding end")
print("my_list[:4] =", my_list[:4])

print("use [:] for items in the list")
print("my_list[:] =", my_list[:])

print("use a [::step] value to use a different step value when slicing")
# start at index 0 and go up in steps of 2
print("my_list[::2] =", my_list[::2])
# start at index 1 and go up in steps of 2
print("my_list[1::2] =", my_list[1::2])
# start at index 0 and end at index 7 but step backwards
print("my_list[::-1] = ", my_list[::-1])
# start at index 7 and end at index 7
print("my_list[-1::-1] = ", my_list[-1::1])
# start at index 0 and end at but not including index 7
print("my_list[:-1:1] = ", my_list[:-1:1])
# start at index 6 and end at but not including index 2...
print("my_list[-2:2:-1] = ", my_list[-2:2:-1])
# ...but step backwards

print("another way to do above...")
slice_tests = ['my_list[::2]', 'my_list[1::2]', 'my_list[::-1]']
for test in slice_tests:
    print(test, "=", eval(test))
