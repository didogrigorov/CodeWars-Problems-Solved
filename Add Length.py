def add_length(str_):
    new_str = str_.split(" ")
    result = []

    for item in new_str:
        length = str(len(item))
        item = item + " " + length
        result.append(item)

    return result


print(add_length("apple ban"))