


def merge_string(word1,word2):

    result=""

    for index in range(0,len(word1)):

        result+=word1[index]+word2[index]

    return result



print(merge_string("ABCD","PQRS"))

