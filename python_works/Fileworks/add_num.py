# create a function smart_sub with two parameters return +number as result after subtraction





def smart_sub(n1,n2):

    return abs(n1-n2)




assert smart_sub(10,2)==8,"test case1 failed with n1>n2"

assert smart_sub(2,10)==8,"test case2 failed with n1<n2"

assert smart_sub(50,40)==10,"test case3 failed"