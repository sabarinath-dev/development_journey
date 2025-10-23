

class person():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.gender = ""
        self.place = ""

    def person_data(self):
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")
        self.gender = input("Enter your gender: ")
        self.place = input("Enter your place: ")

    def person_details(self):

        print("NAME     :" , self.name)
        print("AGE      :" , self.age)
        print("GENDER   :" , self.gender)
        print("PLACE    :" , self.place)

class employee(person):
    def __init__(self):
        self.company = ""
        self.salary = 0
        self.contact = 0

    def employee_data(self):
        self.company = input("Enter your company: ")
        self.salary = input("Enter your salary: ")
        self.contact = input("Enter your contact: ")

    def employee_details(self):
        print("COMPANY   :" , self.company)
        print("SALARY    :" , self.salary)
        print("CONTACT   :" , self.contact)

obj = employee()
obj.person_data()
obj.employee_data()
obj.person_details()
obj.employee_details()


