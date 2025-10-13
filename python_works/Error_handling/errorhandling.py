
"""
Error handling

(try,except,finally)=>block,
raise,assert=>key words


1)syntax error
2)logical error
3)runtime error handle

try:
    doubtful code

except:
    handling code
"""


num1=int(input("enter numebr1"))#10

num2=int(input("enter numebr1"))#0

try:
    div_result=num1//num2#10//0// error stop

    print(div_result)

   

except:
    print("error occured")

print("write div result into a file")

print("program completed.......")




# enter atm
# select service as wirtdraw
# enter pin
# enter amount 5000
#process trasaction=> bank => rollback 
# collect cash