


# r1                  *   

# r2              *       *   

# r3          *       *       * 
  
# r4      *       *       *       *  
  
# r5   *       *       *       *       *


for r in range(1,6):

    for space in range(1,6-r):

        print(" ", end=" ")

    for col in range(1,r+1):

        print("* ", end=" ")

    print()