

arr = [3,4,5,6,7,8,9,10]

#create a new list that contains the cubes of all numbers.

cubes = [num**3 for num in arr]
print(cubes)

#create two new list if contain only even and odd numbers.

even = [num for num in arr if num % 2 == 0]
print(even)

odd = [num for num in arr if num % 2 != 0]
print(odd)