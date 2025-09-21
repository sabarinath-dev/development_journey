

num_list = list()

for i in range(0, 5):

    num = int(input("Enter the number:"))
    num_list.append(num)
reversed_list = num_list[::-1]
print("List=" ,num_list)
print("Reversed List =" , reversed_list)