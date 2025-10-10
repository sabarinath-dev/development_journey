

# create a lambda function with 2 paramtere n1,n2 and return maximum number

n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))

maximum = lambda n1,n2: n1 if n1 > n2 else n2 # return n1 if n1 > n2 else return n2
print(maximum(n1,n2))