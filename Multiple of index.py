def multiple_of_index(arr):
    result = []

    for i in range(len(arr)):
        if arr[i] == 0:
            result.append(arr[i])
        elif arr[i] != 0 and i == 0:
            continue
        elif arr[i] % i == 0:
            result.append(arr[i])

    return result



arr = [0,2,3,6,9]
print(multiple_of_index(arr))