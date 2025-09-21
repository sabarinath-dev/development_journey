

num_list = list()

for i in range(0, 5):

    num = int(input("Enter the number:"))
    num_list.append(num)

elem = int(input("Enter the element to be counted:"))
freq = num_list.count(elem)
print(num_list)
print(freq)