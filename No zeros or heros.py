def no_boring_zeros(n):
    if n == 0:
        return 0
    str_n = str(n)
    final = str_n.strip("0")
    return int(final)

print(no_boring_zeros(10500000))