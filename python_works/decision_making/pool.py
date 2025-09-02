

mark1 = int(input("enter mark 1:"))
mark2 = int(input("enter mark 2:"))
mark3 = int(input("enter mark 3:"))

total = mark1 + mark2 + mark3

if mark1 <= 50 and mark2 <=50 and mark3 <=50:

    if total >= 140:
        print("excellence pool:" , total)

    elif total >= 130:
        print("progress pool.", total)

    elif total >= 120:
        print("foundation pool.", total)

    else:
        print("dead pool.", total)

else:
    print("not eligible for any pool")
