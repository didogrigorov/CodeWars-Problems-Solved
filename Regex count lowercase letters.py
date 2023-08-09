import re
def lowercase_count(strng):
    if strng == "":
        return 0
    small_counter = 0
    match = re.findall(r'[a-z]', strng)
    for char in match:
        if char.islower():
            small_counter += 1

    return small_counter

print(lowercase_count("ABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~"))