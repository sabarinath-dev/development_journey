

#pangram = a sentence contains every letter of the alphabet.

text = "the quick brown fox jumps over lazy dog"    #contains all alphabet letters.

alphabets = "abcdefghijklmnopqrstuvwxyz"

is_pangram = True

for al in alphabets:

    if al not in text:

        is_pangram = False

        break
print(is_pangram)