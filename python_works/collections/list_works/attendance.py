

attendance = [ "H" , "O" , "A" , "P"  , "P" , "H" , "H"]


h_count = 0
o_count = 0
p_count = 0
a_count = 0

for at in attendance:

    if at == "H" :

        h_count += 1


    elif at == "O":

        o_count += 1
    
    
    elif at == "A":

        a_count += 1
    
    
    elif at == "P":

        p_count += 1

print("Holiday =" , h_count)
print("online =" , o_count)
print("offline =" , p_count)
print("Absent =" , a_count)


# for at in attendance:

#     if at == "H" :

#         print("Holiday")

#     elif at == "O":

#         print("Online")
    
#     elif at == "A":

#         print("Absent")
    
#     elif at == "P":

#         print("Offline")