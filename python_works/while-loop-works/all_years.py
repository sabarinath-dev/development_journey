

"""
read two year start_year and end_year display all years from start_year to end_year

"""

start_year = int(input("enter year to start"))


end_year = int(input("enter year to end"))


while(start_year<= end_year):

    if start_year %100==0:

        print(start_year)
    
    start_year+=1

