

class Employee:
    def __init__(self, name ,place , company , salary):
        self.name = name
        self.place = place
        self.company = company
        self.salary = salary
    def getvalues(self):
        print("Employee Name    :" , self.name)
        print("Employee Place   :" , self.place)
        print("Employee Company :" , self.company)
        print("Employee Salary  :" , self.salary)

e1 = Employee("Sabarinath" , "Kochi" , "TCS" , "30000")
e1.getvalues()