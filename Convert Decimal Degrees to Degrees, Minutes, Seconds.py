def convert(degrees):
    if degrees == 0:
        return [0]

    m, s = divmod(degrees * 3600, 60)
    d, m = divmod(m, 60)
    result = [round(d), round(m), round(s)]

    # if seconds are 60, add 1 to the minutes
    if result[-1] == 60:
        result[-2] = result[-2] + 1
        result.remove(result[-1])

    # Omit the trailing zeroes
    for i in range(len(result) - 1, -1, -1):
        if i == 0:
            break
        if result[i] == 0:
            result.remove(result[i])
        else:
            break

    return result



print(convert(69.36666666666666))
