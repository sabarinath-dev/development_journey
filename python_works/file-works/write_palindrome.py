

words = ["hello" , "hai" , "madam" , "neveroddoreven", "cricket", "steponnopets"]

file_path = "C:\\Users\\Sabar\\Desktop\\development_journey\\python_works\\file-works\\palindrome.txt"

fw=open(file_path,"w")\

for w in words:
    if w == w[::-1]:

        fw.write(w + "\n")