

arr =[2,3,4,5,6,7,12,1,13,14,15]

# generate a new list even_numbers andd odd_numbers from this list

odd_list=list() #[]

even_list=list()

for num in arr:

    if num %2==0:

        even_list.append(num)

    else:

        odd_list.append(num)

print("odd list",odd_list)
print("even list",even_list)

