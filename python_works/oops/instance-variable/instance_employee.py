

class employee:

    def setvalues(self,id,name,gender,designation,salary,company):
        self.eid = id
        self.name = name
        self.gender = gender
        self.position = designation
        self.salary = salary
        self.company = company

    def getvalues(self):
        print("Employee id      :" , self.eid)
        print("Name             :" , self.name)
        print("Gender           :" , self.gender)
        print("Designation      :" , self.position)
        print("Salary           :" , self.salary)
        print("Company          :" , self.company) 

e1 = employee()
e1.setvalues(101 , "Aqeel" , "M" , "Python developer" , 75000 )
e1.getvalues() 
print()

e2 = employee()
e2.setvalues(102 , "Priya Sharma" , "F" , "Frontend Developer" , 68000 )
e2.getvalues() 
print()

e3 = employee()
e3.setvalues(103 , "Rahul Menon" , "M" , "Data Analyst" , 72000 )
e3.getvalues() 
print()

e4 = employee()
e4.setvalues(104 , "Anjali Verma" , "F" , "UI/UX Designer" , 64000 )
e4.getvalues() 
print()

e5 = employee()
e5.setvalues(105 , "Arjun Das" , "M" , "Backend Engineer" , 80000 )
e5.getvalues() 
print()


