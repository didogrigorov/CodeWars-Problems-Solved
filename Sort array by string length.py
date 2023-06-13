def sort_by_length(arr):
    sorted_array = sorted(arr, key = lambda x: len(x))
    return sorted_array


list_arr = ["Telescopes", "Glasses", "Eyes", "Monocles"]
print(sort_by_length(list_arr))