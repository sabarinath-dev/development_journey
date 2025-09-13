"""

read number
set digit_count = 0
set sum = 0

loop:

    extract digit

    increment digit_count by 1

    floor number

loop:

    extract digit

    find exponent of digit with digit count

    add exponent with sum

    floor

display sum

"""



number = int(input("Enter a number:"))

original = number

digit_count = 0
sum = 0

while (number != 0):

    last_digit = number % 10
    digit_count = digit_count + 1
    number = number // 10

while (original != 0):
    last_digit = original % 10
    sum = sum + (last_digit ** digit_count)
    original = original // 10

print("Sum of digits:", sum)