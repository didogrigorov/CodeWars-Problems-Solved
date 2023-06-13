def reverse_seq(n):
    result = []
    while n > 0:
        result.append(n)
        n-=1
    return result


print(reverse_seq(5))