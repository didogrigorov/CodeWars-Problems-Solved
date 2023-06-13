def capitalize_word(word):
    word_list = list(word)
    new_word = []

    for i in range(len(word_list)):
        if i == 0:
            new_word.append(word_list[i].upper())
        else:
            new_word.append(word_list[i])

    return ''.join(new_word)


print(capitalize_word("hello"))