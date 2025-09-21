

num_list = list()

for i in range(0, 5):

    num = int(input("Enter the number:"))
    num_list.append(num)

num_list.sort()

print("The list = " , num_list)

print("The second largest number is" , num_list[1])