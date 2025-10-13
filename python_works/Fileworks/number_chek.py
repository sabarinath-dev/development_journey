

# create a function is_positive with 1 parameter num return True if number is +ve else return False


def is_positive(num):

    result=True

    result=num>0

    return result




assert is_positive(5)==True,"test case1 failed with +ve number"

assert is_positive(-5)==False,"test case2 failed with -ve number"



assert is_positive(0) == False,"test case3 failed with 0"



"""

try:
    doubtful code
except:
    handling code
finally:
    cleanup processing
raise custom error
assert debug
"""