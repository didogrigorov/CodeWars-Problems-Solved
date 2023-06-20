def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    chars = {}
    original_chars = {}

    for char in test:
        if char not in chars:
            chars[char] = 0
        chars[char] += 1

    for char in original:
        if char not in original_chars:
            original_chars[char] = 0
        original_chars[char] += 1

    return chars == original_chars


print(is_anagram("foefet", "toffee"))
print(is_anagram("Buckethead", "DeathCubeK"))
print(is_anagram("dumble", "bumble"))
print(is_anagram("ound", "round"))
