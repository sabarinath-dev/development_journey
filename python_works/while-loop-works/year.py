
start_year = int(input("Enter the start year: "))
end_year = int(input("Enter the end year: "))

while(start_year <= end_year):

    if(start_year % 100 == 0):
         print("year",start_year)

    start_year += 1