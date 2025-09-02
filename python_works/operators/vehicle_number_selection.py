#read vehicle_number Last 4 Digit

#last_digit even
#last_digit > 5

number = int(input("Enter the last four digits of vehicle number:"))

last_digit = number % 10

print(last_digit > 5 and last_digit % 2 == 0)