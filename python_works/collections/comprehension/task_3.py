

arr = [10,11,12,13,14,15]

# output as {10:even,11:odd,12,even}

dict_arr = {num:"odd" if num % 2 == 0 else "even" for num in arr}

print(dict_arr)