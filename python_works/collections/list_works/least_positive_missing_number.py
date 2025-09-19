
#find least positive missing number.


numbers = [1 ,2, 3 ,4 , 6] #list

for num in range(0,len(numbers)): #taking each num in numbers

    least = num+1   #1+1 = 2

    if least not in numbers:    #if 2 is not in numbers its the least missing number

        print("The least missing number:",least)