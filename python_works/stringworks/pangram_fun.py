


def is_pangram(word):

    flag=True

    alphabets = "abcdefghijklmnopqrstuvwxyz"
    #             0


    for al in alphabets:

        if al not in word.lower():

            flag=False

            break

    return flag


print(is_pangram("hello world"))
# function taht return True if word is opangram else return False


# listen
# silent