def find_needle(haystack):
    for idx, word in enumerate(haystack):
        if word == "needle":
            return f"found the needle at position {idx}"


print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))