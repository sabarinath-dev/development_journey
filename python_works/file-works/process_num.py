

numbers = [1,2,3,4,5,6,7,8,9,10]

file_path_even = "C:\\Users\\Sabar\\Desktop\\development_journey\\python_works\\file-works\\even_num.txt"

file_path_odd = "C:\\Users\\Sabar\\Desktop\\development_journey\\python_works\\file-works\\odd_num.txt"

fw_even = open(file_path_even , "w")
fw_odd = open(file_path_odd , "w")

for num in numbers:

    if num  % 2 == 0:

        fw_even.write(str(num)+ "\n")
                      
    else:
        fw_odd.write(str(num)+"\n")