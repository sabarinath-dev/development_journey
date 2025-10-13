
# read vehicle_number last 4 digit

# 1919
# last_digit even
# last_digit > 5

vehicle_number = int(input("enter number"))


last_digit = vehicle_number % 10 #last_digit = 9

print(last_digit > 5 and last_digit%2==0)



