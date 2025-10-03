

word = ["sabari" , "sree" , "latha" , "suresh" ,"sabari" , "latha" ,"sabari" , "sree" , "latha" , "suresh" ,"sabari" , "latha" ,"sabari" , "sree" , "latha" , "suresh" ,"sabari" , "latha" ,"sabari" , "sree" , "latha" , "suresh" ,"sabari" , "latha"]

word_count ={}

# for w in word:
    
#     if w in word_count:

#         word_count[w]+=1

#     else:
#         word_count[w] = 1

# print(word_count)


# print(word.count("sabari"))

word_count={w:word.count(w)for w in word}

print(word_count)