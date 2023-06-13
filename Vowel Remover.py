def shortcut(s):
    vowels = ["a", "e", "i", "o", "u"]
    s = list(s)
    result_word = s.copy()

    for i in range(len(s)):
        if s[i] in vowels:
            result_word.remove(s[i])

    return ''.join(result_word)


string = "hellooooo"
print(shortcut(string))
