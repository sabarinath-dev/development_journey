

# read a year = 2000
""""
display century year if last two digit of year is 00 
else display non century year

"""

year = int(input("enter year"))


if year % 100 ==0 :

    print("century year")

else:

    print("non century year")


    