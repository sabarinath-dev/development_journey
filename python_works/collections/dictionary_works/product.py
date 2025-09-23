


"""
create a dictionary of product with code,title,brand,category,price
add key stock with value 50 if stock not exist.
"""

product = {"code":123 , "title":"Potronics keyboard" , "brand":"Potronics" , "category":"PC accessories" , "price":1420 , "offer":1000}

if "stock"  not in product:

    product["stock"] = 50

else:

    print("Stock already exist.")

if "offer" in product:

    product["offer"]+=99

else:

    product["offer"] = 1099

print(product)