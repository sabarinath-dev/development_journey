

def is_pangram(word):

    flag = True

    alphabets = "abcdefghijklmnopqrstuvwxyz"
                #0123456789
    for al in alphabets:

        if al not in word.lower():

            flag = False

            break

    return flag

print(is_pangram("hello world"))

#function that return True if word is pangram else return False.