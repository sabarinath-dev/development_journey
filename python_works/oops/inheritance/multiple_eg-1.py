

class person():
    def __init__(self):
        self.name   = ""
        self.age    = 0
        self.place  = ""
        self.mobile = 0

    def person_data(self):
        self.name   = input("Enter your name: ")
        self.age    = int(input("Enter your age: "))
        self.place  = input("Enter your place: ")
        self.mobile = int(input("Enter your mobile: "))

    def person_details(self):
        print("\n_____Person Details_____")
        print("Name    :" , self.name)
        print("Age     :" , self.age)
        print("Place   :" , self.place)
        print("Mobile  :" , self.mobile)


class job:
    def __init__(self):
        self.position   = ""
        self.salary     = 0

    def job_data(self):
        self.position   = input("Enter your position: ")
        self.salary     = int(input("Enter your salary: "))

    def job_details(self):
        print("\n_____Job Details_____")
        print("Designation  :" , self.position)
        print("Salary       :" , self.salary)

class employee(person,job):
    def __init__(self):
        self.employee_id    = 0
        self.company        = ""
        self.location       = ""
        self.email          = ""

    def employee_data(self):
        self.employee_id    = int(input("Enter your employee id: "))
        self.company        = input("Enter your company: ")
        self.location       = input("Enter your company location: ")
        self.email          = input("Enter your email: ")

    def employee_details(self):
        print("\n_____Company Details_____")
        print("Employee ID  :" , self.employee_id)
        print("Company      :" , self.company)
        print("Location     :" , self.location)
        print("Email        :" , self.email)

obj1 = person()
obj1.person_data()

obj2 = job()
obj2.job_data()

obj3 = employee()
obj3.employee_data()

obj1.person_details()
obj2.job_details()
obj3.employee_details()

