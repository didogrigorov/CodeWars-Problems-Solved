def convert(number):
    result = ""
    for i in range(0, len(number), 2):
        char_num = number[i:i+2]
        item = chr(int(char_num))
        result += item

    return result

print(convert("73327673756932858080698267658369"))