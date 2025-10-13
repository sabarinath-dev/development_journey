

# last_week_attendance store organize "P","O","A","H"

monday="A"
tuesday="A"

# sunday
# sat

attendance=["H","A","P","O","O","A","H"]
#            0   1   2   3   4   5   6


attendance[4]="P"

print(attendance)


holiday_count=0

offline_count = 0

online_count = 0

absent_count = 0
# offline_count
#online_count
# absent_count

for at in attendance:

    if at=="H":

        holiday_count+=1

    elif at=="P":

        offline_count+=1

    elif at=="O":

        online_count+=1

    elif at == "A":

        absent_count+=1

print("holiday count",holiday_count)

print("offline count",offline_count)

print("online count",online_count)

print("absent count",absent_count)



# bms,dst,ptm,wkn
orders=["bms","bms","bms","ptm","ptm","ptm","wkn","wkn","wkn","bms","ptm"]

# highest
# lowest
# total_tiket_sold

"""
numbers=[10,11,14,3,8,19,20,21,22,23,56]

q1)display all even numbers
q2)display all odd numbers
q3)display_sum of all even numbers
q4)display largest number
q5)display smallest number

"""