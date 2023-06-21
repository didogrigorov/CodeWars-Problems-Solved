def is_isogram(string):
    string = string.lower()

    if string == "":
        return True

    chars = {}

    for char in string:
        if char not in chars:
            chars[char] = 0
        chars[char] += 1

    chars_list = list(chars.values())

    for i in range(len(chars_list)):
        if i + 1 < len(chars_list):
            if chars_list[i] != chars_list[i + 1]:
                return False


    return True



# print(is_isogram("isogram"))
print(is_isogram("isIsogram"))