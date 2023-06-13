def between(a,b):
    result = []

    for i in range(a, b + 1):
        result.append(i)

    return result

print(between(-2, 2))