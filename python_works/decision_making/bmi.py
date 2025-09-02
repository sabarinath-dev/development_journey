
"""
based on display condition

under weight
normal weight
over weight
obese

BMI = weight_in_kg / height_in_meter ** 2

Display obese bmi >= 30
Display overweight bmi >= 25
Display normal bmi >= 20
Display under bmi < 20

"""

height_in_cm = int(input("Enter the height:"))
weight_in_kg = int(input("Enter the weight: "))

height_in_m = height_in_cm/100

BMI = weight_in_kg / (height_in_m ** 2)

BMI = round(BMI)

if BMI >= 30:

    print(BMI, "Obese")

elif BMI >= 25:

    print(BMI, "overweight")

elif BMI >= 20:

    print(BMI, "normal")

else:
    
    print(BMI, "Under")