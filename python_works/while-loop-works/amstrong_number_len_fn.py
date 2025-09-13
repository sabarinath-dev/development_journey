"""

read number
set digit_count = 0
set sum = 0

use len() function to find digit_count

loop:

    extract digit

    find exponent of digit with digit count

    add exponent with sum

    floor

display sum

"""

number = int(input("Enter a number:"))

digit_count = len(str(number))

original = number
sum = 0

while(number != 0):

    last_digit = number % 10

    sum = sum + ( last_digit ** digit_count)

    number = number // 10

if (original == sum):
    print(original, "is an Armstrong number")
else:
    print(original, "is not an Armstrong number")