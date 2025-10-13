"""
functions are used to perform a specific task

1)function defnition
2)function calling


syntax
    def function_name(p1,p2,p3,,,pn):
    
        functionbody

        retrun value

function_calling

function_name(arg1,arg2,arg2,,,argn)
"""


# create a function greeting that will display Goodmorning


def greeting():

    print("good morning")

greeting()




# create a function say_hello with one parameter user_name 
#function display hello user_name


def say_hello(user_name):

    print("hello",user_name)

say_hello("vipin")


# create a funtion add_numbers with two parameter n1,n2
# function should return sum of n1,n2

def add_numbers(n1,n2):

    result= n1+n2

    return result


# output=add_numbers(100,200)

# print(output)

print(add_numbers(100,200))


# create a function cube with one parameter num
# return cubre of number

def cube(num):

    result = num**3

    return result

print(cube(4))

print(cube(5))


# create a function max_of_two with two parameter n1,n2 return largest number 



def max_of_two(n1,n2):

    if n1>n2:

        return n1
    else:

        return n2
    

print(max_of_two(100,20))


def is_prime(number):#17 ,1,17 2,,,,,,,,16

    flag=True

    for i in range(2,number):

        if number%i ==0:

            flag=False

            break
    
    return flag



def prime_upto_limit(limit):

    for number in range(1,limit+1):

        result = is_prime(number)

        if result == True:

            print(number)

prime_upto_limit(50) 


#