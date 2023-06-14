def solve(arr):

    new_array = []

    for i, n in enumerate(arr):
        if arr.index(n) != i:
            new_array.append(n)

    for i in range(len(new_array)):
        arr.remove(new_array[i])

    return arr


arr = [3, 4, 4, 3, 6, 3]
print(solve(arr))