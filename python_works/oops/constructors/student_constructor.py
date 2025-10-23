
class student:
    def __init__(self, id , name , age , place , course , college , Contact_no):
        self.sid         = id
        self.name       = name
        self.age        = age
        self.place      = place
        self.course     = course
        self.college    = college
        self.mobile     = Contact_no

    def display(self):
        print("Student ID   :",self.sid)
        print("Name         :",self.name)
        print("Age          :",self.age)
        print("Place        :",self.place)
        print("Course       :",self.course)
        print("College      :",self.college)
        print("Contact No   :",self.mobile)

s1 = student(101 , "Sabarinath" , 21 , "Cochin" , "Bsc CS" , "UIT Kollam" , 8089844630)
s1.display()