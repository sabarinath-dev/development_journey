
#read number

#loop:
    #extract digit
    #check if digit is odd if yes exit from loop
    #floor number

number = int(input("Enter a number: "))

while(number != 0):

    last_digit = number % 10

    if(last_digit % 2 != 0):

        print("Largest odd number is:", last_digit)
        break
    
    number = number // 10