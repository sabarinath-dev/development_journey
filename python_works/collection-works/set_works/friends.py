

all_users={"sachin","dravid","kohli","laxman","ganguly","yuvi","dhoni","zaheer"}


sachin_friends={"dravid","kohli","laxman","ganguly"}


yuvi_friends={"laxman","ganguly","dhoni","zaheer"}


mutual_friends=sachin_friends.intersection(yuvi_friends)
print(mutual_friends)
# mutual friends

# display suggestion for sachin

suggestions=all_users.difference(sachin_friends)

suggestions.remove("sachin")





st1={10,20,30,40}

st2={100,10,200,20,300}

symmetric_diff=st1.symmetric_difference(st2)

print(symmetric_diff)

# a union b - a inter b

# 30,40,100,200,300 (10,)

# set ,{10,20,30} ,



