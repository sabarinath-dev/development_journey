

words = ["sabari" , "sree" , "latha" , "suresh" ,"sabari" , "latha" ,"sabari" , "sree" , "latha" , "suresh" ,"sabari" , "latha" ,"sabari" , "sree" , "latha" , "suresh" ,"sabari" , "latha","sabari" , "sree" , "latha" , "suresh" ,"sabari" , "latha"]

# create a new words with converting all words into upper case.

# upper_words = [w.upper() for w in words]
# print(upper_words)

# create a new dictionary from words , set word as key and value as length of that word.

dict_words = {w:len(w) for w in words}
print(dict_words)