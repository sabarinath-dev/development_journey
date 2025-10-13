

numbers=[10,20,20,11,11,12,13,13]
# sort()
# [10,11,11,12,13,13,20,20]
#   0  1  2  3  4  5  6  7
#   c, n
numbers.sort()

duplicate_numbers=[]


for current in range(0,len(numbers)-1):

    next = current + 1

    current_element = numbers[current]

    next_element = numbers[next]

    differnce = next_element - current_element

    if differnce == 0 and current_element not in duplicate_numbers:

        duplicate_numbers.append(current_element)

print(duplicate_numbers)


numbers =[1,3,4]

# numbers=[1,3,4]
#          0 1 2
#     

# find least +ve missing number 
 







