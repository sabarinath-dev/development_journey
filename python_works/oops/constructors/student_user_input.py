
class student:
    def __init__(self):
        self.id         = ""
        self.name       = ""
        self.age        = ""
        self.place      = ""
        self.course     = ""
        self.college    = ""
        self.mobile     = ""

    def student_data(self):
        print("...Enter the student details...")
        self.sid        = input("Enter Student ID : ")
        self.name       = input("Enter Student Name : ")
        self.age        = input("Enter Student Age : ")
        self.place      = input("Enter Student Place : ")
        self.course     = input("Enter Student Course : ")
        self.college    = input("Enter Student College : ")
        self.mobile     = input("Enter Student Mobile : ")
        print()

    def student_details(self):
        print("_____Student Details_____")
        print("Student id       :" , self.sid)
        print("Student Name     :" , self.name)
        print("Student Age      :" , self.age)
        print("Student Place    :" , self.place)
        print("Student Course   :" , self.course)
        print("Student College  :" , self.college)
        print("Student Mobile   :" , self.mobile)

s1 = student()
s1.student_data()
s1.student_details()