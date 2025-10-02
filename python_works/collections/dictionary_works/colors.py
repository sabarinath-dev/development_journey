

colors =["red" , "blue" , "green" , "yellow" , "red" , "red" , "green"]

color_count = {}

for c in colors:

    if c in color_count:

        color_count[c] +=1

    else:
        color_count[c] = 1

print(color_count)