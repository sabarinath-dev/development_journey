

orders = ["tea" , "coffee" , "blackcoffee" , "cappucinno" , "coffee" , "iced tea" , "tea", "blackcoffee"]

# {"tea":2 , "coffee":2 , "blackcoffee":2}

order_count = {}

# iterrate orders

for o in orders:
    # check o exist in order_count

    if o in order_count:
        # o exist in order count
        # update o as current value +1
        order_count[o]+=1

    else:
        # o not exist in order count
        # add o as key and value as 1
        order_count[o] = 1

print(order_count)