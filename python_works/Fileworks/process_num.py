"""
read number from numbers.txt

find max_number
find min_number
find sum

write all these to another file called result.txt



"""

file_input_path="C:\\Users\\Luminar\\Desktop\\development_journey_july_2k25\\python_works\\Fileworks\\numbers.txt"

file_write_path="C:\\Users\\Luminar\\Desktop\\development_journey_july_2k25\\python_works\\Fileworks\\result.txt"

numbers=[]

max_number=0

min_number=0

total=0

try:

    fw=open(file_write_path,"w")
    fr=open(file_input_path,"r")

    for line in fr:

        num=int(line.rstrip("\n"))#"100"

        numbers.append(num)

    max_number=max(numbers)

    min_number=min(numbers)

    total=sum(numbers)

    fw.write("maxnumber="+str(max_number)+"\n")

    fw.write("min number ="+str(min_number)+"\n")

    fw.write("total="+str(total)+"\n")


except FileNotFoundError as fe:

    print(fe)



finally:

    fr.close()

    fw.close()

# 
# python core => object oriented programming
# mysql
# django