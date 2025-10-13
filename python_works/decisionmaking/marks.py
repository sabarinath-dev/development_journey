

# read 3 marks mark1,mark2 and mark3 each out of 50
# find total = mark1+mark2+mark3
# display exlence pool if total > 140
# dispaly progress pool if total > 130
# dispaly foundation pool if total > 120
# display dead pool if total < 120


mark1 = int(input("enter mark1"))

mark2 = int(input("enter mark2"))

mark3 = int(input("enter mark3"))

total = mark1 + mark2 + mark3 # 137

if total>=140:

    print("exellence pool")

elif total>=130:

    print("progress pool")

elif total>=120:

    print("Foundation Pool")

else:

    print("dead pool")


    

