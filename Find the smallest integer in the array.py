def find_smallest_int(arr):
    arr.sort()
    smallest = arr[0]

    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]

    return smallest



arr = [78, 56, 232, 12, 11, 43]
print(find_smallest_int(arr))