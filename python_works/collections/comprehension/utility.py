

"""

list comprehension : easy way to create a list from iterable.

set comprehension : easy way to create a set from iterable.

"""

"""
list comprehrnsion

syntax:

list = [return value iteration condition]

"""

arr = [10,11,12,13,14,50]

# create a new list from this arr which contains the square of each number.

# square = []

# for num in arr:

#     square.append(num**2)

# print(square)

squares = [num**2 for num in arr]
print(squares)

cubes = [num**3 for num in arr]
print(cubes)

num_25 = [num for num in arr if num > 25]
print(num_25)

add = [num + 5 for num in arr]

print(add)