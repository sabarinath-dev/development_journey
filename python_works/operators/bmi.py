
# read height,weight
# BMI = weight_in_kg / (height_in_meter^2)

height_in_cm = int(input("enter height in cm ") )

weight_in_kg = int(input("enter weight in kg "))

height_in_meter = height_in_cm/100

bmi = weight_in_kg/(height_in_meter**2)

print(bmi)

