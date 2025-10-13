

# logical operators (and,or,not)


# print(True and False) # False  

# print(False or True)#True

# print(not False) # True



number = int(input("enter number"))

# display True if number is completly / by 4 and 8 else False



print(number%4==0 and number%8==0) #True


# read a number display True if last digit of number is > 5 and number / by 2

number = int(input("enter number"))

last_digit = number % 10

print(last_digit > 5 and number%2==0)
