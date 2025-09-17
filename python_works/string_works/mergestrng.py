

# mergestring
# sample output

# word1 = ABCDE
# word1 = PQRS

# output = APBQCRDSE

word1="ABCD"
word2="PQRS"
result = ""

for index in range(0, len(word1)):
	result += word1[index] + word2[index]

print(result)
    