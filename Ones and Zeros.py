def binary_array_to_number(arr):
    number = 0
    len_arr = len(arr) - 1
    for i in range(len(arr)):
        number += 2 ** len_arr * arr[i]
        len_arr -= 1
    return number

print(binary_array_to_number([0,0,0,1]))