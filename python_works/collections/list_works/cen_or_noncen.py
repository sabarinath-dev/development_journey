

# century_years_list
# non_century_years_list


years = [1899 , 1900 , 2000 , 2021 , 2022 , 2023 , 1991 , 1992]

century_years_list = list()
non_century_years_list = list()

for yr in years:

    if yr % 100 == 0:
         
         century_years_list.append(yr)

    else:
         
         non_century_years_list.append(yr)

print("century_years_list:" , century_years_list)
print("non_century_years_list:" , non_century_years_list)