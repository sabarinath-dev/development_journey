

"""

read two numbers

display all common divisors of the two numbers

"""

num1= int(input("Enter first number:"))
num2= int(input("Enter second number:"))

limit = min(num1,num2)

for i in range(1 , limit+1):

    if num1 % i ==0 and num2 % i ==0:
        
        print("The common divisors are:", i)
