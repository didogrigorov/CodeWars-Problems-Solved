def print_array(arr):
    output = []
    for i in range(len(arr)):
        str_item = str(arr[i])
        output.append(str_item)

    return ','.join(output)


data = [2, 4, 5, 2]
print(print_array(data))