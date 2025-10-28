class student:
    def __init__(self):
        self.student_id     = 0
        self.student_name   = ""
        self.age            = 0
        self.course         = ""
        self.place          = ""
        self.contact        = 0

    def student_data(self):
        self.student_id     = int(input("Enter student ID: "))
        self.student_name   = input("Enter student name: ")
        self.age            = int(input("Enter age: "))
        self.course         = input("Enter course: ")
        self.place          = input("Enter place: ")
        self.contact        = int(input("Enter contact number: "))

    def student_details(self):
        print("\n----- Student Details -----")
        print("Student ID: "    , self.student_id)
        print("Student name: "  , self.student_name)
        print("Age: "           , self.age)
        print("Course: "        , self.course)
        print("Place: "         , self.place)
        print("Contact: "       , self.contact)


class marks(student):
    def __init__(self):
        self.physics    = 0
        self.chemistry  = 0
        self.maths      = 0
        self.english    = 0
        self.computer   = 0

    def marks_data(self):
        print("\n----- Enter Marks -----")
        self.physics    = int(input("Enter physics marks: "))
        self.chemistry  = int(input("Enter chemistry marks: "))
        self.maths      = int(input("Enter maths marks: "))
        self.english    = int(input("Enter english marks: "))
        self.computer   = int(input("Enter computer marks: "))


class result(marks):
    def __init__(self):
        self.total_marks        = 0
        self.mark_percentage    = 0

    def calculate_result(self):
        self.total_marks        = ( self.physics + self.chemistry + self.maths + self.english + self.computer)
        self.mark_percentage    = (self.total_marks / 500) * 100

    def result_data(self):
        print("\n----- Result -----")
        print("Total marks: " , self.total_marks)
        print("Percentage: "  , self.mark_percentage ,"%")


student1 = result()
student1.student_data()
student1.marks_data()
student1.calculate_result()
student1.student_details()
student1.result_data()
