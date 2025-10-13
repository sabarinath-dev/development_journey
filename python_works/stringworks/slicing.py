# slicing extracting a portion from a sequence (string,list)
# sliced_text=object[start:stop:step]

text="pythonprogramming"
#     01234567890123456


sliced_text=text[6:]

print(sliced_text)

sliced_word2=text[:6]

reverse_word=text[::-1]

print(reverse_word)


def is_palindrome(word):

    flag=True

    if word !=word[::-1]:

        flag=False


    return flag


print(is_palindrome("madam"))

print(is_palindrome("man"))