

# read number from user
#set sum as zero


#loop while number != 0
    #get last digit from number
    #find the cube of the last digit
    #add last digit cube to sum
    #remove last digit from number


number = int(input("Enter a number:"))
sum = 0

while(number != 0):

    last_digit = number % 10
    digit_cube = last_digit ** 3
    sum = sum + digit_cube
    number = number // 10

print("Sum of cube of digits:", sum)