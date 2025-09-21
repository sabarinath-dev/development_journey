arr = [1 , 2 ,3 ,4, 5 , 6]

arr.sort()  # Sort the list to ensure numbers are in order

for current in range(0, len(arr) - 1): # Using two pointer

    next = current + 1  # Get the index of the next element

    next_element = arr[next]  # Value of the next element

    current_element = arr[current]  # Value of the current element

    difference = next_element - current_element  # Find the difference between consecutive elements

    if difference != 1:  # If the difference is not 1, a number is missing

        print(current_element + 1, "is missing.")  # Print the missing number

        break  # Exit after finding the first missing number

if arr[next] == arr[-1]:

    print(arr[-1]+1, "is missing")
