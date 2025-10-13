
"""
read number
set digit_count as 0
set sum as 0

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



number = int(input("enter number"))

digit_count = len(str(number))

original = number

sum =0

while(number !=0):

    digit = number% 10

    exponent = digit ** digit_count

    sum = sum + exponent

    number = number // 10



if original == sum :

    print(original,"is armstrong")

else:

    print(original ,"is not armstrong")


# sum of digit
# largest odd number
# cube sum of digit
# armstromg number

# hackerrank

# for  => if range is known
# while => if range is unknown

# 10 -100  => even numbers

# num  != 0 

# number = 5 (1*2*3*4*5

# for 