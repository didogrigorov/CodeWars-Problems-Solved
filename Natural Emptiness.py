def rep_set(n):
    result = [rep_set(k) for k in range(n)]
    return result

print(rep_set(3))