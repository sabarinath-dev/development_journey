
#pattern


#         col-1    col-2     col-3     col-4
# row 1     <         >         <         >
# row 1     <         >         <         >
# row 1     <         >         <         >





for row in range(1,4):

    for col in range(1,5):

        if col % 2 == 0:

            print(">",end=" ")

        else:
            print("<",end=" ")

    print()