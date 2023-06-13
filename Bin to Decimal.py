def binary_to_decimal(binary):
    decimal = 0
    power = len(binary) - 1

    for digit in binary:
        decimal += int(digit) * (2 ** power)
        power -= 1

    return decimal

binary_number = "101010"
decimal_number = binary_to_decimal(binary_number)
print(decimal_number)  # Output: 42
