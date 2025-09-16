
#set vowels = "aeiou"
#set vowel_count = 0
#extract each characters from text
#increment vowel_count to +1 if char is in vowel

text = "sabarinath"

vowels = "aeiou"

v_count = 0

for ch in text:

    if ch in vowels:

        v_count+=1
         
print(v_count)