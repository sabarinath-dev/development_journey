

"""
source_word = "chicken"
target word = "hen"

"""

source_word = "chicken"
target_word = "hen"

is_container_word = set(target_word).issubset(set(source_word))

print(is_container_word)