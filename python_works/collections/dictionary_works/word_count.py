

words = ["hai" , "hello" , "morning" , "hello" , "hai" , "hai" , "good"]

words_count = {}

for w in words:

    if w in words_count:

        words_count[w] += 1

    else:

        words_count[w] = 1

print(words_count)

text = "this is a python program this python program is simple"

word = text.split(" ")

word_count = {}

for c in word:

    if c in word_count:

        word_count[c]+=1
    
    else:

        word_count[c]=1

print(word_count)
