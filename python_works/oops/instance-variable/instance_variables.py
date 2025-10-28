

class student:
    def setvalues(self , student_id, name, age, gender, department, course, year, email):
        self.sid = student_id
        self.name = name
        self.age = age
        self.gender = gender
        self.dep = department
        self.course = course
        self.year = year
        self.email = email

    def getvalues(self):
        print("Student id        :", self.sid)
        print("Name              :", self.name)
        print("Age               :", self.age)
        print("Gender            :", self.gender)
        print("Department        :", self.dep)
        print("Course            :", self.course)
        print("Year              :", self.year)
        print("Email             :", self.email)

s1 = student()
s1.setvalues(101 , "Sabarinath S" , 21 , "M" , "BSc" , "Computer Science" , "2022-25" , "Sabarinath1617@gmail.com")
s1.getvalues()
