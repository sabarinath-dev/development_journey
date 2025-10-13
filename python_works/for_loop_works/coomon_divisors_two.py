"""
read two number num1,num2

display common divisors of num1 and num2

num1=12
num2=24
o/p =>1,2,3,4,6,12,
"""


num1=int(input("enter number1"))

num2=int(input("enter number2"))

limit = min(num1,num2)


for i in range(1,limit+1):

    if num1%i ==0 and num2%i ==0:

        print(i)


"""
nested loop

"""



# a person have to visit 5 floor with 7 step in each floor

for fl in range(1,6):#fl=1

    for st in range(1,8):#st=1

        print("floor",fl,"step",st)


# fl=1 st=1
# fl=1 st=2
