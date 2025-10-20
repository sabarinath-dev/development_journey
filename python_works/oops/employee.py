
class employee:

    def employeefunction(self,employee_id,name,gender,designation,department,employee_status,salary):
        print(" Employee ID     : " , employee_id)
        print(" Name            : " ,name)
        print(" Gender          : " ,gender)
        print(" Designation     : " ,designation)
        print(" Department      : " ,department)
        print(" Active          : " ,employee_status)
        print(" Salary          : " ,salary)

em1 = employee()
em1.employeefunction("EMP001" , "Arjun Mehta" , "Male" , "Software Engineer ", "IT" , "Active" , 75000)
print()

em2 = employee()
em2.employeefunction("EMP002" , "Priya Sharma" , "Female" , "HR", "Human Resources" , "Active" , 58000)
print()

em3 = employee()
em3.employeefunction("EMP003" , "Rahul Nair" , "Male" , "Sales Manager", "Sales" , "On Leave" , 75000)
print()

