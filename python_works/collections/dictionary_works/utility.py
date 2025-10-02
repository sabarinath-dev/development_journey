

"""

class dictionary

dictionary = {"key":value} 

dictionary["key"] = value - to add/update a dictionary

def keys(self): return all keys
def values(self) : return all values
def items()
def get(self,key)
def pop(self,key)
def update(self,key)

"""

phone = {"brand":"Xiaomi" , "model":"Redmi 13 pro plus" ,"connection":"5g" , "price": 25000}

brand = phone["brand"]
model = phone["model"]
price = phone["price"]
connection = phone["connection"]


phone["display"] = "2k Amoled" # adding new key and value
display = phone["display"]

if "connection" in phone: # checking if a specific key value is present in the dictionary
    print("Exist")
else:
    print("Not existing")

print("Brand:" , brand)
print("Phone model is" , model)
print("Connection type is" , connection)
print("Display type:" ,display)
print("Sale value:" , price)