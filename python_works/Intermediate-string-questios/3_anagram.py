

word1 = input("Enter the first word:")
word2 = input("Enter the second word:")

def is_anagram_text(word1,word2):

    is_anagram = True

    if sorted(word1) != sorted(word2):

        is_anagram = False

    return is_anagram

print(is_anagram_text(word1,word2))