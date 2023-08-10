def distinct(seq):
    result = []
    
    for num in seq:
        if num in result:
            continue
        else:
            result.append(num)

    return result

print(distinct([1, 1, 1, 2, 3, 4, 5]))