def max_product(a):
    largest = float('-inf')  # Initialize largest as negative infinity
    second_largest = float('-inf')  # Initialize second largest as negative infinity

    for num in a:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num

    return largest * second_largest

arr = [3,6,4,8,5]
print(max_product(arr))
