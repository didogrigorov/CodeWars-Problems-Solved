def split_and_merge(string_, separator):
    result = string_.split()
    str_result_arr = []
    str_item = ""

    for item in result:
        for char in item:
            str_item += char + separator
        str_result_arr.append(str_item)
        str_item = ''

    return ' '.join(x.strip(separator) for x in str_result_arr)


# ['M', 'y', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'J', 'o', 'h', 'n']
print(split_and_merge("My name is John", ","))