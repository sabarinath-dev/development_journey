

"""
the basal metabolic rate (BMR)=
10 * weight (KG) + 6.25 * height (cm) - 5 * age + 5 for (MEN)malee
10 * weight (KG) + 6.25 * height (cm) - 5 * age - 161 for (Women)

"""

gender = input("Enter the gender: ")
age = int(input("Enter the age: "))

height_in_cm = int(input("Enter the height: ") )

weight_in_kg = int(input("Enter the weight: "))

activity_level = 1.2

if gender == "male":

   BMR = 10 * weight_in_kg + 6.25 * height_in_cm - 5 * age + 5

else:

   BMR = 10 * weight_in_kg + 6.25 * height_in_cm - 5 * age - 161

calories = BMR * activity_level

print("calories=" , calories)

