def find(arr, e):
    try: return arr.index(e)
    except: return "Not found"

array = [2, 3, 5, 7, 11]
print(find(array, 15))
