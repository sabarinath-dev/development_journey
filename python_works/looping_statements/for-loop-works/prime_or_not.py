

# check the number is prime or not

"""

if n is a prime number then it can only be divided by 1 and itself.

otherwise the number is not prime and it is a composite number.

"""

n = int(input("Enter the number:"))

for i in range(2 , n):

    if(n % i == 0):

        print(n , "is not a prime number ! , Because it is divisible by 1, " , i , "and", n)

        break

    else:

        print(n , "is a prime number.")

        break