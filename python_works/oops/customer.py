

class customer:

    def customerfunction(self,customer_id,name,email,phone_no,address,pincode):

        print("Customer ID  :" , customer_id)
        print("Name         :" ,name)
        print("Email ID     :" ,email)
        print("Contact No   :" ,phone_no)
        print("Address      :" ,address)
        print("Pincode      :" ,pincode)

c1 = customer()
c1.customerfunction("CUST001", "Neha Verma", "neha.verma@gmail.com", 9876543210, "24 Park Street, Kolkata", 700016)
print()

c2 = customer()
c2.customerfunction("CUST002", "Rohan Iyer", "rohan.iyer@yahoo.com", 9123456789, "112 MG Road, Bengaluru", 560001)
print()

c3 = customer()
c3.customerfunction("CUST003", "Kavya Menon", "kavya.menon@hotmail.com", 9812345678, "45 Anna Nagar, Chennai", 600040)
print()

