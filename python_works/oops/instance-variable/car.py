# car 5 obj

class car:
    def setvalues(self,brand,model,year,color,fuel_type,transmission,body_type):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.fuel = fuel_type
        self.transmission = transmission
        self.body = body_type

    def getvalues(self):
        print(" Brand        : " ,self.brand)
        print(" Model        : " ,self.model)
        print(" Year         : " ,self.year)
        print(" Color        : " ,self.color)
        print(" Fuel         : " ,self.fuel)
        print(" Transmission : " ,self.transmission)
        print(" Body Type    : " ,self.body)



c1 = car()
c1.setvalues("Toyota" , "Corolla Altis" , 2020 , "White" , "Petrol" , "Automatic" , "Sedan")
c1.getvalues()
print()

c2 = car()
c2.setvalues("Hyundai" , "Creta" , 2023 , "Red" , "Petrol" , "Automatic" , "Sedan")
c2.getvalues()
print()

c3 = car()
c3.setvalues("volkswagen" , "Vento" , 2019 , "Silver" , "Petrol" , "Automatic" , "Sedan")
c3.getvalues()
print()

c4 = car()
c4.setvalues("Tata" , "Nexon EV" , 2022 , "Blue" , "Electric" , "Automatic" , "SUV")
c4.getvalues()
print()

c5 = car()
c5.setvalues("Maruti Suzuki" , "Baleno" , 2021 , "Grey " ,"Petrol" , "Manual" , "Hatch")
c5.getvalues()



