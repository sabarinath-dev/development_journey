

"""

P=loan amount
R= monthly interest rate(annual_rate/(12*100))
n=loan tenure in moths (6*12)

"""

loan_amount = int(input("enter loan amount ")) #600000

interest_rate = int(input("enter interest rate "))#9

loan_tenure = int(input("enter tenure "))#6

p = loan_amount

r = interest_rate /(12*100)

n = loan_tenure * 12

# EMI =( P*R*(1+R)^n )/((1+R)^n-1)
EMI = ( p*r*(1+r)**n) / ((1+r)**n-1)

total_payable_amount = EMI * n

total_interest_payable = total_payable_amount - loan_amount 

print("EMI=",round(EMI,2),"Total Payabale Amount",round(total_payable_amount,2),"total interest",round(total_interest_payable,2))

