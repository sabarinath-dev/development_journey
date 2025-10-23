
class person:
    def __init__(self):
        self.name = ""
        self.age = ""
        self.place = ""

    def person_data(self):
        print(("Enter the following details..."))
        self.name = input("Enter your name      : ")
        self.age = input("Enter your age        : ")
        self.place = input("Enter your place    : ")
        print()

    def person_details(self):
        print("---Your details---")
        print("Name  : " , self.name)
        print("Age   : " , self.age)
        print("Place : " , self.place)

p1 = person()
p1.person_data()
p1.person_details()