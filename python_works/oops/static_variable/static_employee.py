

class Employee:
    company = "TCS"
    def setvalues(self,id,name,gender,designation,salary):
        self.eid = id
        self.name = name
        self.gender = gender
        self.position = designation
        self.salary = salary

    def getvalues(self):
        print("Employee id      :" , self.eid)
        print("Name             :" , self.name)
        print("Gender           :" , self.gender)
        print("Designation      :" , self.position)
        print("Salary           :" , self.salary)
        print("Company          :" , Employee.company)

e1 = Employee()
e1.setvalues(101 , "Aqeel" , "M" , "Python developer" , 75000 )
e1.getvalues() 
print()

e2 = Employee()
e2.setvalues(102 , "Priya Sharma" , "F" , "Frontend Developer" , 68000 )
e2.getvalues() 
print()

e3 = Employee()
e3.setvalues(103 , "Rahul Menon" , "M" , "Data Analyst" , 72000 )
e3.getvalues() 
print()

e4 = Employee()
e4.setvalues(104 , "Anjali Verma" , "F" , "UI/UX Designer" , 64000 )
e4.getvalues() 
print()

e5 = Employee()
e5.setvalues(105 , "Arjun Das" , "M" , "Backend Engineer" , 80000 )
e5.getvalues() 
print()


