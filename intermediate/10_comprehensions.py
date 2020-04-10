import math

print("allows sequences to be built from other sequences")
print(
    "form is '[ <output-expression> for <variable> in <input-sequence> <optional predicate>")

my_list = [1, 2, 3, 4]
print("adding one to", my_list)
print("[x+1 for x in my_list] =", [x+1 for x in my_list])
print("dividing odd numbers by two from", my_list)
print("[x/2 for x in my_list if x % 2] =", [x/2 for x in my_list if x % 2])
print("not only odd numbers end up in output expression due to predicate which controls items to go in output")

print("can be used to create populated lists:", [x for x in range(8)])
print("or a signal:", [math.sin(2*math.pi*x/16) for x in range(16)])

print("nested list comprehension to generate identity matrix - lists within lists")
# output-expression of first level comprehension is a list, which is generated by a list comprehension
identity_matrix = [[1 if col_index == row_index else 0 for col_index in range(
    4)] for row_index in range(4)]
print(identity_matrix)

print("you can have multiple levels - multiple for loops - in a comprehension")
print([col for row in identity_matrix for col in row])
print("this is equivalent to...")
output = []
for row in identity_matrix:
    for col in row:
        output.append(col)
print(output)

print("you can have if-else statements in the output expression")
print("['odd' if x % 2 else 'even' for x in my_list] =",
      ['odd' if x % 2 else 'even' for x in my_list])
print("useful if you want to keep sequence the same size")


def number_function(x):
    return x**2


def string_function(x):
    return x.capitalize()


my_list = [1, 2, 'bob', 3, 'elephant']
print("you can call functions inside comprehensions for", my_list)
print([number_function(x) if type(x) is int else string_function(x)
       for x in my_list])

my_tuple = (1, 2, 3)
print("you input sequence can be any sequence, such as a tuple or zip output", my_tuple)
print([x for x in my_tuple])

my_dict = {'bob': 1, 'sally': 2, 'susan': 3}
print("or a dictionary", my_dict,
      "and convert it to a list of tuple (key,value) pairs")
print([(key, value) for key, value in my_dict.items()])

print("\ncomprehensions aren't restricted to lists e.g. dictionary comprehension")
print({key.capitalize(): value for key, value in my_dict.items() if value > 1})
