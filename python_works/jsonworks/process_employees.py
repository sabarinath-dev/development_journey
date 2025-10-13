
from json import load,loads



file_path="C:\\Users\\Luminar\\Desktop\\development_journey_july_2k25\\python_works\\jsonworks\\employees.json"

fr=open(file_path,"r")


employees=load(fr)

# print(employees)


all_employee_names=[emp.get("name") for emp in employees ]


# print(all_employee_names)


all_departments={emp.get("department") for emp in employees}

# print(all_departments)


# display ell employee names whose salary > 30000


salry_filter=[emp.get("name") for emp in employees if emp.get("salary")>30000]

print(salry_filter)

#display vendor of  TikTok  


for c in c