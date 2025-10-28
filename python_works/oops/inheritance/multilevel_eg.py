

class college():
    def __init__(self):
        self.college_name = ""
        self.location     = ""
        self.Clg_contact  = ""
        self.clg_mail     = ""

    def clg_data(self):
        self.college_name   = input("Enter your college name: ")
        self.location       = input("Enter your location: ")
        self.clg_contact    = input("Enter your clg contact: ")
        self.clg_mail       = input("Enter your clg mail: ")

    def clg_details(self):
        print("College      :" , self.college_name)
        print("Location     :" , self.location)
        print("Contact      :" , self.clg_contact)
        print("Mail         :" , self.clg_mail)

class department(college):
    def __init__(self):
        self.department_id      = ""
        self.department_name    = ""
        self.department_hod     = ""

    def department_data(self):
        self.department_id      = input("Enter your department ID: ")
        self.department_name    = input("Enter your department name: ")
        self.department_hod     = input("Enter your department hod name: ")

    def department_details(self):
        print("Department ID        :" , self.department_id)
        print("Department Name      :" , self.department_name)
        print("Department Hod Name  :" , self.department_hod)

class student(department):
    def __init__(self):
        self.student_id     = ""
        self.student_name   = ""
        self.age            =""
        self.gender         = ""
        self.course         = ""
        self.mobile_no      = ""
        self.email          = ""

    def student_data(self):
        self.student_id     = input("Enter your student ID: ")
        self.student_name   = input("Enter your student name: ")
        self.age            = input("Enter your age: ")
        self.gender         = input("Enter your gender: ")
        self.course         = input("Enter your course: ")
        self.mobile_no      = input("Enter your mobile no: ")
        self.email          = input("Enter your email: ")

    def student_details(self):
        print("Student ID   :" , self.student_id)
        print("Student Name :" , self.student_name)
        print("Age          :" , self.age)
        print("Gender       :" , self.gender)
        print("Course       :" , self.course)
        print("Mobile No    :" , self.mobile_no)
        print("Email        :" , self.email)

obj1 = student()
obj1.student_data()
obj1.department_data()
obj1.clg_data()
obj1.student_details()
obj1.department_details()
obj1.clg_details()