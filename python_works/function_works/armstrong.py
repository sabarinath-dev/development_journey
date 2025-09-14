

num = int(input("Enter the number:"))

def is_armstrong(num):

    temp = num

    digit_count = len(str(num))

    result = 0

    while temp != 0:

        digit = temp % 10
        exp = digit ** digit_count
        result += exp

        temp = temp // 10

    return result == num

if is_armstrong(num):
    print(num, "is armstrong")
else:
    print(num, "is not armstrong")
 
