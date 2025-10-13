
"""
based on bmi display health condition  

under weight
normal weight
over weight
obese

BMI = weight_in_kg / height_in_meter ** 2

Display obese bmi >= 30
Display overweight bmi >= 25
Display normal bmi >= 20
Display under weight bmi <20


"""
height_in_cm = int(input("enter height in cm "))

weight_in_kg = int(input("enter weight in kg"))

height_in_meter = height_in_cm/100

BMI = weight_in_kg / (height_in_meter**2)

BMI = round(BMI)

if BMI >= 30:

    print("OBESE")

elif BMI >= 25:

    print("overweight")

elif BMI>= 20:

    print("normal weight")

else:

    print("under weight")


