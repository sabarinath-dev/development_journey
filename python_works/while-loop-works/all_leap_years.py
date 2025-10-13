
start_year = int(input("enter start year"))

end_year = int(input("enter end year"))


while(start_year <= end_year):

    if start_year%100==0 and start_year %400==0 or start_year%100!=0 and start_year%4==0:

        print(start_year)

    start_year+=1