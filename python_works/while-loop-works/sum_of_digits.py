

# read number from user
#set sum as zero


#loop while number != 0
    #get last digit from number
    #add last digit to sum
    #remove last digit from number

number = int(input("Enter a number:"))
sum = 0

while(number != 0):
    
    last_digit = number % 10
    sum = sum + last_digit
    number = number // 10

print("Sum of digits:", sum)