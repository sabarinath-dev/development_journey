

numbers = [10 , 40 ,20 , 10 , 20 , 50 , 12 , 14, 15 , 12] #list

duplicate_list = [] #empty list to add duplicate numbers

for num in numbers: #taking each object on the list

    freq = numbers.count(num)   #adding the count value to freq

    if freq > 1 and num not in duplicate_list:   

        duplicate_list.append(num)

print("numbers:" ,numbers)
print("duplicate numbers:", duplicate_list)