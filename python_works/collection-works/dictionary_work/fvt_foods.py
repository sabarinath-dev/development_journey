favt_colors=[]

# data types and operators

favt_colors.append("red")
favt_colors.append("green")
favt_colors.append("black")
favt_colors.append("blue")
favt_colors.append("green")
favt_colors.append("black")
favt_colors.append("gold")
favt_colors.append("black")


print(favt_colors)#['red', 'green',"red" ,'black', 'blue', 'green', 'black', 'gold', 'black']

color_count={}#{"red":1,"green":1}

for c in favt_colors:#c=green

    if c in color_count:

        color_count[c]+=1
    else:
        color_count[c]=1

print(color_count)

