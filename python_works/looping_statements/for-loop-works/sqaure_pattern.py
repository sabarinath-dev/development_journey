# $   $   $   $   $   $
# $                   $
# $                   $
# $                   $
# $                   $
# $   $   $   $   $   $


for row in range(1,7):

    for col in range(1,7):

        if row == 1 or row == 6:

            print("$", end=" ")

        elif col == 1 or col == 6:

            print("$", end=" ")

        else:
            
            print(" ", end=" ")

    print()
