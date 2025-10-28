

class Student:
    def __init__(self):
        self.name   = ""
        self.age    = 0
        self.course = ""
        self.place  = ""
        self.mobile = 0

    def student_data(self):
        self.name   = input("Enter your name: ")
        self.age    = int(input("Enter your age: "))
        self.course = input("Enter your course: ")
        self.place  = input("Enter your place: ")
        self.mobile = int(input("Enter your mobile: "))

    def student_detailis(self):
        print("\n_____STUDENT DETAILS_____")
        print("Name     :" , self.name)
        print("Age      :" , self.age)
        print("Course   :" , self.course)
        print("Place    :" , self.place)
        print("Mobile   :" , self.mobile)

class Sports:
    def __init__(self):
        self.sports = ""
        self.score  = ""

    def sport_data(self):
        print("\n_____Please Enter Sport_Details_____")
        self.sports = input("Enter your sports: ")
        self.score  = int(input("Enter your score: "))

    def sport_detailis(self):
        print("\n_____SPORTS DETAILS_____")
        print("Sports Name  :" , self.sports)
        print("Sports Score :" , self.score)

class Result(Student,Sports):
    def __init__(self):
        Student.__init__(self)
        Sports.__init__(self)
        self.total = 0

    def calculate_total(self):
        self.total = self.age + self.score

    def display_result(self ):
        obj.student_detailis()
        obj.sport_detailis()
        print("\n_____RESULT_____")
        print("Total :" , self.total)

obj = Result()
obj.student_data()
obj.sport_data()

obj.calculate_total()
obj.display_result()
