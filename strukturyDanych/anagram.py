def is_anagram(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()

    return sorted(w1) == sorted(w2)

print(is_anagram("absurd", "brudas"))
print(is_anagram("ognia", "orgia"))