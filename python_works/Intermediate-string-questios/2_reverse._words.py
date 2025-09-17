
sentence = input("Enter a sentence:")

def reverse_words(sentence):
    words = sentence.split()      # split into words
    result = ""                   # to store reversed sentence

    for i in range(len(words)-1, -1, -1):   # loop backwards
        result += words[i]
        if i != 0:                 # add space (but not after last word)
            result += " "

    return result


print("Reversed words:", reverse_words(sentence))

