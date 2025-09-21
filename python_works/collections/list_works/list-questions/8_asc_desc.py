

num_list = list()

for i in range(0, 5):

    num = int(input("Enter the number:"))
    num_list.append(num)


asc_list = sorted(num_list)

reversed_list = num_list.copy()

desc_list = sorted(num_list, reverse=True)


print("list in ascending order" , asc_list)
print("list in descending order" , desc_list)
