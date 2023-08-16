def fake_bin(x):
    output = ""
    for digit in x:
        int_digit = int(digit)
        if int_digit < 5:
            output += "0"
        else:
            output += "1"

    return output

print(fake_bin("45385593107843568"))