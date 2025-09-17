

def is_palindrome(word):

    flag = True

    reverse_word = word[::-1]

    if(word != reverse_word):

        flag = False

    return flag

print(is_palindrome("madam"))

print(is_palindrome("man"))

