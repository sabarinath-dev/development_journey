

"""

Read all years from years.txt and display leap years.


"""

fw_path_leap = "C:\\Users\\Sabar\\Desktop\\development_journey\\python_works\\file-works\\years.txt"\

fw = open(fw_path_leap,"r")

for y in fw:

    year = int(y.rstrip("\n"))

    if year % 100 == 0 and year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        print(year)
