
years=[1899,1900,2000,2021,2022,2023,1991,1992]

# century_years_list
# non_century_year_list

century_years=list()

non_century_years=list()

for y in years:

    if y%100==0:

        century_years.append(y)

    else:

        non_century_years.append(y)

print("century years,",century_years)

print("non century years",non_century_years)
