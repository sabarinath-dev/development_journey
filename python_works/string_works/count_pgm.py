
# text = "python has more than 3 frameworks 1 django 2 flask > @"

# write a program to display vowel_count
# consonant count
# alphabet count
# digit count 

text = "python has more than 3 frameworks 1 django 2 flask > @"

vowels = "aeiou"

v_count = 0
c_count = 0
a_count = 0
d_count = 0

for ch in text:

    if ch.isalpha():
        a_count += 1

        if ch in vowels:
            v_count += 1

        else:
            c_count +=1

    elif ch.isdigit():
        d_count += 1

print("Vowel count:", v_count)
print("consonant count:", c_count)
print("alphabet count:", a_count)
print("digit count:", d_count)
