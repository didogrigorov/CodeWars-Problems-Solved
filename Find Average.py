def find_average(numbers):
    # your code here
    if len(numbers) == 0:
        return 0
    sum = 0
    for item in numbers:
        sum += item

    return sum / len(numbers)

print(find_average([1,2,3]))