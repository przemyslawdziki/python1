def is_palindrom(word):
    word = word.lower()
    return word[::-1] == word

print(is_palindrom("Mama"))
print(is_palindrom("Mim"))