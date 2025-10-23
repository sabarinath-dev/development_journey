

class employee:

    def __init__(self):
        self.eid        = ""
        self.name       = ""
        self.gender     = ""
        self.position   = ""
        self.salary     = ""
        self.company    = ""

    def employee_data(self):
        print("Enter the Following Details....")
        self.eid      = input("Enter Employee ID      : ")
        self.name     = input("Enter Employee Name    : ")
        self.gender   = input("Enter Employee Gender  : ")
        self.position = input("Enter Employee Position: ")
        self.salary   = input("Enter Employee Salary  : ")
        self.company  = input("Enter Employee Company : ")
        print()

    def employee_details(self):
        print("_____Employee Details_____")
        print("Employee id      :" , self.eid)
        print("Name             :" , self.name)
        print("Gender           :" , self.gender)
        print("Designation      :" , self.position)
        print("Salary           :" , self.salary)
        print("Company          :" , self.company)

e1 = employee()
e1.employee_data()
e1.employee_details()





