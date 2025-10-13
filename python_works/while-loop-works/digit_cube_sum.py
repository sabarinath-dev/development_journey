

# read number
# set sum as 0

# loop:
    #extract digit 
    #find digit cube
    #add digit_cube with sum
    # floor number

# display sum

number = int(input("enter number"))

sum = 0

while(number !=0):

    digit = number % 10

    cube = digit ** 3

    sum = sum + cube

    number = number // 10

print(sum)


# 1634