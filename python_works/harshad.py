

num = int(input("Enter the number: "))  #user input number
sum = 0 #empty variable
for i in str(num):  #converting the number into string for easy digitd separation
    sum = sum + int(i)  #adding each i(digits) of str(num) into sum variable as int variable
if num % sum == 0:  #if the num is divisble by sum its a harshad no.
    print("The number is harshad.")
else:
    print("The number is not harshad.")