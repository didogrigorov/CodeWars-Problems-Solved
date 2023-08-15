def str_count(strng, letter):
    counter = 0
    for char in strng:
        if char == letter:
            counter += 1

    return counter

print(str_count("Hello", "o"))