

"""
EMI = P*R(1+R)^N / ((1+R)^N-1)

P = Loan Amount
R = Monthly Interest Rate (Annual Rate/12*100)
N = loan tenure (6*12)

"""

loan_amount = int(input("Enter the Loan Amount: "))

interest_rate = float(input("Enter the Annual Interest Rate: "))

loan_tenure = int(input("Enter the Loan Tenure (in years): "))

p = loan_amount
r = interest_rate / (12 * 100)
n = loan_tenure * 12

EMI = (p * r * (1+r)**n) / ((1+r)**n-1)

total_payment = EMI * n

total_interest = total_payment - p

print("EMI=",round(EMI,2), "Total Payment=", round(total_payment,2), "Total Interest=", round(total_interest,2))

