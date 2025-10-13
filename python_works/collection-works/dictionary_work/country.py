"""
create a dictionary country with keys code,alpha_code,name,capital,population
 create a dictionary product code,title,category,price,brand
"""

country = {
    "code":1234,
    "alphacode":"ind",
    "name":"india",
    "capital":"delhi",
    "population":34567890,
    "gdp":8,
    "altspelling":"india"
}






# add key if key not exist else update key
# update gdp as current gdp+1 if gdp exist else add gdp as 9

# update offer as current offer+300 if offer exist else add offer as 250

if "gdp" in country:

    country["gdp"]+=1# update

else:

    country["gdp"]=9#adding


print(country)






# pop=country["population"]

# print(pop)
# # add key stock with value 50 if stock not exist

# if "language" not in country:

#     country["language"]="hindi"

# print(country)