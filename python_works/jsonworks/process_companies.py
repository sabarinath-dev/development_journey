
from json import load

file_path="C:\\Users\\Luminar\\Desktop\\development_journey_july_2k25\\python_works\\jsonworks\\companies.json"

fr=open(file_path,"r")

companies=load(fr)

all_company_names=[c.get("name") for c in companies]

# print(all_company_names)

# produce a new dictionry from companies where key as compnay name and value as employees_count



emp_count={c.get("name"):c.get("employees") for c in companies}

print(emp_count)


# produce a new dictionary from companies where key as company name and value as count of products


product_count={c.get("name"):len(c.get("products")) for c in companies}

print(product_count)


for c in companies:

    if "TikTok" in c.get("products"): # if c.get("products")=="TikTok"

        print(c.get("name"))


product_vendor=[c.get("name") for c in companies if "TikTok" in c.get("products")]


# json.py > load ,load
