
colors = ["red" , "green" , "blue" , "orange" , "yellow"]

file_path = "C:\\Users\\Sabar\\Desktop\\development_journey\\python_works\\file-works\\colors.txt"

fw = open(file_path , "w")

for c in colors:
    fw.write(c + "\n")