


num_list = list()
sum = 0

for i in range(0, 5):

    num = int(input("Enter the number:"))
    num_list.append(num)

for num in num_list:

    sum += num

total_count = len(num_list)
average = sum // total_count

print("The list is" , num_list)
print("The sum of the list is" , sum)
print("Average" , average)