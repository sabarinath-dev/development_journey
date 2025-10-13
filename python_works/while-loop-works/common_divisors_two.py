

num1 = int(input("enter number1"))#6


num2 = int(input("enter number2"))#12

# 1,,,,,,6,,,,,,,,24


i = 1

minimum = min(num1,num2)


while(i<=minimum):

    if num1%i==0 and num2%i==0:

        print(i)

    i+=1

    