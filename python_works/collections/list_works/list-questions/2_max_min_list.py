

num_list = list()

for i in range(0, 5):

    num = int(input("Enter the number:"))
    num_list.append(num)
maximum = max(num_list)
minimum = min(num_list)
print("The list =" , num_list)
print("The maximum number in the list=" , maximum)
print("The minimum number in the list=" , minimum)