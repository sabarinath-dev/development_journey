



arr=[1,3,4,5,2]

arr.sort() 
#             -1
# [1,2,3,4,5]
#  0 1 2 3 4 
#        c n
#3-2=1 
# difference!=1 c+1 is missing

"""missing least +ve integer"""

for current in range(0,len(arr)-1):

    next=current+1

    current_element = arr[current]

    next_element = arr[next]

    difference = next_element - current_element

    if difference !=1:

        print(current_element+1,"is missing")

        break


if arr[next] == arr[-1]:

    print(arr[-1]+1,"is missing")


# 9:30 starts  list 