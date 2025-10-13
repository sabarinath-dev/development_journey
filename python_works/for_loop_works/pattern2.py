#pgm2
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3


for row in range(1,4):

    for col in range(1,5):

        print(row,end=" ")

    print()


#   1 2 3 4
#1  < > < >
#2  < > < >
#3  < > < >


for row in range(1,4):

    for col in range(1,5):

        if col %2==0:

            print(">",end=" ")
        else:

            print("<",end=" ")

    print()


for row in range(1,6):

    for col in range(1,5):

        print(col*"*",end=" ")
    
    print()

# pattern3

# * ** *** ****
# * ** *** ****
# * ** *** ****
# * ** *** ****
# * ** *** ****


# pattern4
#    c1    c2   c3    c4

#    1,1   1,2  1,3   1,4 

#r1  $$   $$$  $$$$  $$$$$
#r2  $$$  $$$$  $$$$$ $$$$$$
#r3  $$$$ $$$$$ $$$$$$ $$$$$$$


for row in range(1,4):

    for col in range(1,5):

        print((row+col)*"$",end=" ")
    
    print()