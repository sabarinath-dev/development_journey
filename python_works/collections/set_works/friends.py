

all_users={"sachin", "dravid", "kohli", "laxman", "ganguly", "yuvi", "dhoni", "zaheer"}

sachin_friends={"dravid", "kohli", "laxman", "ganguly"}

yuvi_friends={"laxman", "ganguly", "dhoni", "zaheer"}

# display suggestion for sachin

suggestions = all_users.difference(sachin_friends)

suggestions.remove("sachin")

mutual_frnds = sachin_friends.intersection(yuvi_friends) #common frnds

print(suggestions)
print(mutual_frnds)