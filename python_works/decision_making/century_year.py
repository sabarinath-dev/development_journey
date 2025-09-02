# display century year if last two digits are zero
# if not print non century


year = int(input("Enter the year:"))

if year % 100 == 0:

    print("Century year")
    
else:
    print("Non century year")