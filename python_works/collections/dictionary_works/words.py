text = "hello hai morning hello hai night evening hello"

# display most frequent word

words = text.split()
# word_count = {w: words.count(w) for w in set(words)}

# print(word_count)

word_count = {}

for w in words:
    if w in word_count:
        word_count[w] += 1
    else:
        word_count[w] = 1

print(word_count)

sorted_word = sorted(word_count , reverse=True , key = word_count.get)
print(sorted_word)
