

"""
collection inside collection.

[] =list
()= tuple
{} = set
{key,value} = dictionary

eg:
data =[

        []
        []
        []

]
    =>list of list.
"""


students=[
    {"id": 1, "name": "Sabarinath", "Qualification": "BSc cs", "college": "UIT kollam", "Graduated year": 2025},
    {"id": 2, "name": "Sagar", "Qualification": "BTECH", "college": "UIT kollam", "Graduated year": 2025},
    {"id": 3, "name": "Asif nissar", "Qualification": "BSc cs", "college": "UIT kollam", "Graduated year": 2025},
    {"id": 4, "name": "Mahi", "Qualification": "MCA", "college": "Amarjyothi", "Graduated year": 2025},
    {"id": 5, "name": "Izzath A S", "Qualification": "MBA", "college": "UIT kollam", "Graduated year": 2025}
]

# for st in students:
#     print(st.get("name"))

# for clg in students:
#     print(st.get("college"))

all_st_name = [st.get("name") for st in students]
all_st_college = [st.get("college") for st in students]
all_st_year = [st.get("Graduated year") for st in students]
all_st_qualification = [st.get("Qualification") for st in students]

print(all_st_college)
print(all_st_name)
print(all_st_qualification)
print(all_st_year)

cs_st_name = [st.get("name") for st in students if st.get("Qualification") == "BSc cs"]
print(cs_st_name)

st_year = [st.get("name")for st in students if st.get("Graduated year") == 2025]
print(st_year)