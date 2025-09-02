

number = int(input("Enter the number:"))

while(number != 0):
    last_digit = number % 10
    print(last_digit)
    number = number // 10