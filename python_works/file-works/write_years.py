
"""
write all years from 1890 to 2025 into years.txt

"""

file_path = "C:\\Users\\Sabar\\Desktop\\development_journey\\python_works\\file-works\\years.txt"

fw = open(file_path , "w")

for y in range(1890 , 2026):
    fw.write(str(y) + "\n")