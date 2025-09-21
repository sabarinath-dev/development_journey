


num_list = list()

for i in range(0, 5):

    num = int(input("Enter the number:"))

    num_list.append(num)

elem = int(input("Enter the element to be checked:"))

for num in num_list:

    if elem == num:
        print(num , "is present in the list.")

        break