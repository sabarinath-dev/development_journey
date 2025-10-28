# Define a base class Person
class Person:
    def __init__(self):                                         
        self.name    = ""                                       
        self.age     = 0                                        
        self.place   = ""                                       
        self.mobile  = 0                                        

    def person_data(self):                                      
        self.name    = input("Enter the name        : ")        
        self.age     = int(input("Enter the age         : "))   
        self.place   = input("Enter the place       : ")        
        self.mobile  = int(input("Enter the mobile no  : "))    

    def display_person_details(self):                           
        print("\n--- PERSON DETAILS ---")                       
        print("Name       : ", self.name)                       
        print("Age        : ", self.age)                        
        print("Place      : ", self.place)                      
        print("Mobile No  : ", self.mobile)                     


# Derived class Student from Person
class Student(Person):
    def __init__(self):                                         # Constructor for Student
        Person().__init__()                                      # Call parent constructor
        self.sid      = 0                                       
        self.course   = ""                                      
        self.college  = ""                                      

    def student_data(self):                                     # Method to collect student details
        print("\n--- ENTER STUDENT DETAILS ---")                
        self.person_data()                                      # Call base class method
        self.sid      = int(input("Enter the student ID : "))   
        self.course   = input("Enter the course     : ")        
        self.college  = input("Enter the college    : ")        

    def display_student_details(self):                          # Method to display student details
        print("\n--- STUDENT DETAILS ---")                      
        self.display_person_details()                           # Display base class details
        print("Student ID  : ", self.sid)                       
        print("Course      : ", self.course)                    
        print("College     : ", self.college)                   


# Derived class Doctor from Person
class Doctor(Person):
    def __init__(self):                                         # Constructor for Doctor
        Person().__init__()                                      # Call parent constructor
        self.dept        = ""                                   
        self.spl         = ""                                   
        self.hosp_name   = ""                                   
        self.location    = ""                                   

    def doctor_data(self):                                      # Method to collect doctor details
        print("\n--- ENTER DOCTOR DETAILS ---")                 
        self.person_data()                                      # Call base class method
        self.dept        = input("Enter the department     : ") 
        self.spl         = input("Enter the specialization : ") 
        self.hosp_name   = input("Enter the hospital name  : ") 
        self.location    = input("Enter the location       : ") 

    def display_doctor_details(self):                           # Method to display doctor details
        print("\n--- DOCTOR DETAILS ---")                       
        self.display_person_details()                           # Display base class details
        print("Department     : ", self.dept)                   
        print("Specialization : ", self.spl)                    
        print("Hospital Name  : ", self.hosp_name)               
        print("Location       : ", self.location)               


# Derived class Teacher from Person
class Teacher(Person):
    def __init__(self):                                         # Constructor for Teacher
        Person().__init__()                                      # Call parent constructor
        self.tid        = 0                                     
        self.sub        = ""                                    
        self.qlf        = ""                                    
        self.clg        = ""                                    
        self.location   = ""                                    

    def teacher_data(self):                                     # Method to collect teacher details
        print("\n--- ENTER TEACHER DETAILS ---")                
        self.person_data()                                      # Call base class method
        self.tid        = int(input("Enter the teacher ID : ")) 
        self.sub        = input("Enter the subject     : ")     
        self.qlf        = input("Enter the qualification : ")   
        self.clg        = input("Enter the college     : ")     
        self.location   = input("Enter the location    : ")      

    def display_teacher_details(self):                          # Method to display teacher details
        print("\n--- TEACHER DETAILS ---")                      
        self.display_person_details()                           # Display base class details
        print("Teacher ID   : ", self.tid)                      
        print("Subject      : ", self.sub)                      
        print("Qualification: ", self.qlf)                      
        print("College      : ", self.clg)                      
        print("Location     : ", self.location)                 




obj1 = Student()
obj1.student_data()
obj1.display_student_details()


obj2 = Doctor()
obj2.doctor_data()
obj2.display_doctor_details()

obj3 = Teacher()
obj3.teacher_data()
obj3.display_teacher_details()