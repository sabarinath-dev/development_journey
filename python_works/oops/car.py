# car 5 obj

class car:

    def car_atrributes(self,brand,model,year,color,fuel_type,transmission,body_type):
        print(" Brand        : " ,brand)
        print(" Model        : " ,model)
        print(" Year         : " ,year)
        print(" Color        : " ,color)
        print(" Fuel         : " ,fuel_type)
        print(" Transmission : " ,transmission)
        print(" Body Type    : " ,body_type)



c1 = car()
c1.car_atrributes("Toyota" , "Corolla Altis" , 2020 , "White" , "Petrol" , "Automatic" , "Sedan")
print()

c2 = car()
c2.car_atrributes("Hyundai" , "Creta" , 2023 , "Red" , "Petrol" , "Automatic" , "Sedan")
print()

c3 = car()
c3.car_atrributes("volkswagen" , "Vento" , 2019 , "Silver" , "Petrol" , "Automatic" , "Sedan")
print()

c4 = car()
c4.car_atrributes("Tata" , "Nexon EV" , 2022 , "Blue" , "Electric" , "Automatic" , "SUV")
print()

c5 = car()
c5.car_atrributes("Maruti Suzuki" , "Baleno" , 2021 , "Grey " ,"Petrol" , "Manual" , "Hatch")




