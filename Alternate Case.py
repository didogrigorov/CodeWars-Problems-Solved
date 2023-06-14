def alternate_case(s):
    # your code here
    if s == "":
        return ""
    elif s == " ":
        return " "

    new_str = ''

    for char in s:
        if char.islower():
            char = char.upper()
            new_str += char
        elif char == " ":
            new_str += char
        elif char.isupper():
            char = char.lower()
            new_str += char

    return new_str


print(alternate_case("i LIKE MAKING KATAS VERY MUCH"))