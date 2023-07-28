def sum_digits(number):
    total = 0
    number = abs(number)
    num = str(number)
    for item in num:
        item = int(item)
        total += item

    return total

print(sum_digits(-32))