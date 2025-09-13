

"""
functions are used to perform specific task

can be divided into two steps:
    1) Define the function

        def function_name(parameter1,parameter2,parameter3,,,,,parametern)
           
             function body
            
             return value

eg:     def addition(n1,n2)

            result = n1 + n2

            return result

    2)Call the Function

        function_name(arg)

eg:     addition(100,200)

"""

#create a function cube with one parameter num
#return cube of number

n = int(input("Enter the number:"))

def cube(n):

    result = n ** 3

    return result

print(cube(n))

