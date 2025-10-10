

# step-1: open file

file_path = "C:\\Users\\Sabar\\Desktop\\development_journey\\python_works\\file-works\\self_intro.txt"

fr = open(file_path, "r")

for line in fr:
    print(line)