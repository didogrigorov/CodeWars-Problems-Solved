def find_array(arr1, arr2):
    # if arrays are empty return []
    if not arr1 or not arr2:
        return []

    # result array
    result = []

    for i in range(len(arr2)):
        if arr2[i] >= len(arr1):
            continue

        result.append(arr1[arr2[i]])


    return result

print(find_array([0,3,4], [2, 6]))