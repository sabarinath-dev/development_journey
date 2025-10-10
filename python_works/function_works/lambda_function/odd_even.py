

# create a lambda function with one parameter n return true if n is even else return false

n = int(input("Enter the number needed to be checked:"))
is_even = lambda n: True if n % 2 == 0 else False
print(is_even(n))