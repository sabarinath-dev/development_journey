

"""
read number
set is_prime as True

loop 2 to number-1
    set is_prime as False if i is divisor of number and break


"""


number = int(input("enter number"))

is_prime = True

for i in range(2,number):

    if number %i==0:

        is_prime=False
        
        break

print(is_prime)



# read a number number =12
# display all divisors of 12 (1,2,3,4,6,12)

