

# sample input

# num1 = 12
# num1 = 24
# 1,2,3,4,6,12
# Common divisors

num1 = int (input ("Enter the first number:"))
num2 = int (input ("Enter the second number:"))

i = 1

minimum = min(num1,num2)

while(i<=minimum):
    if num1 % i == 0 and num2 % i== 0:
        print("The common divisors are:", i)

    i += 1

    