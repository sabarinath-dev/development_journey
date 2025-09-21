



num_list = list()

no_duplicate_list = []

for i in range(0, 5):

    num = int(input("Enter the number:"))

    num_list.append(num)

for num in num_list:

    if num not in no_duplicate_list:
        
        no_duplicate_list.append(num)

print(no_duplicate_list)