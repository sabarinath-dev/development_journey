
Word = input("Enter the word:")

def char_freq(text):

    for ch in text:

        print(ch, ":", text.count(ch))

char_freq(Word)
