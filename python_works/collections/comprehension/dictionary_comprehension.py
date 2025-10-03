

"""

dictionary_comprehension => easy way to create dictionary iterable

syntax :

variable_name ={key: value iteration condition}

"""

arr = [10,20,30,40,50]
#       0  1  2  3  4

# op ={10:10**0, 20:20**1}

# {10:100 , 20:400}

dict_square ={num:num**2 for num in arr}
print(dict_square)

dict_cube = {num:num**3 for num in arr}
print(dict_cube)

for index,value in enumerate(arr):
    print(index,value)


dict_index = {value:value**index for index,value in enumerate(arr)}
print(dict_index)