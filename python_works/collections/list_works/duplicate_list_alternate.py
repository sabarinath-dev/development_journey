

numbers = [10 , 40 ,20 , 10 , 20 , 50 , 12 , 14, 15 , 12] #list

numbers.sort()


duplicates = list() #empty list


for c in range(0,len(numbers)-1):

    n = c + 1

    current_element = numbers[c]

    next_element = numbers[n]

    difference = next_element - current_element

    if difference == 0 and current_element not in duplicates:

        duplicates.append(current_element)

print("duplicate values:" , duplicates)
    