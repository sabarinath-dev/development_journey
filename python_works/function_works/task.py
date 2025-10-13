
# min_of_two(n1,n2)
# factorial(num)
# is_prime(num) True or False
# is_armstrong(num) True or False
# is_leap_yar(year) True|False


def min_of_two(n1,n2):

    return n1 if n1<n2 else n2


# print(min_of_two(10,5))
    
def is_odd(num):

    return True if num%2!=0 else False

# print(is_odd(7))


def is_even(num):

    return  True if num%2==0 else False

# print(is_even(12))


def is_positive(num):

    return num>0



def factorial(num):

    result = 1

    for i in range(1,num+1):

         result = result*i

    return result



def is_armstrong_number(number):#151

    number_copy = number#152

    digit_count = len(str(number))# "151" len => 3

    result = 0#0

    while(number!=0):#151 !=0 15!=0 1 !=0

        digit = number %10# 151%10=1 15%10=5 1%10=1
        
        exp= digit**digit_count#1**3 5**3=125 1**3=1
        
        result+=exp#result=127

        number = number//10#0

    return number_copy == result
    
print(is_armstrong_number(151))









