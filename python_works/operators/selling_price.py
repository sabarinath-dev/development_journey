"""
A shop owner purchases a product at Rs. x 
and adds a profit margin of y%. 
What will be the selling price?

"""

purchase_price = int(input("enter purchase price"))

profit_margin = int(input("enter % profit "))

profit = profit_margin/100*purchase_price

selling_price = purchase_price + profit

print(selling_price)

