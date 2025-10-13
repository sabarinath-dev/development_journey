

gender = input("enter gender")

age = int(input("enter age"))

weight_in_kg= int(input("enter weight"))

height_in_cm = int(input("enter height"))

activity_level = 1.2

"""
The basal metabolic rate (BMR)=
10 * weight (kg) + 6.25 * height(cm) - 5 * age(y) + 5 for (man)
10 * weight(kg) + 6.25 * height(cm) - 5 * age(y) - 161 for ​(woman)
"""
if gender == "male":

    BMR = 10*weight_in_kg+6.25*height_in_cm-5*age+5

else:
    
    BMR =10*weight_in_kg+6.25*height_in_cm-5*age-161


calories = BMR * activity_level

print(calories)


