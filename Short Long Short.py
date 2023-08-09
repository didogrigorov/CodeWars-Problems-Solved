def solution(a, b):
    if a == "":
        return b
    elif b == "":
        return a
    elif len(a) < len(b):
        return a + b + a
    else:
        return b + a + b

print(solution("22", "1"))