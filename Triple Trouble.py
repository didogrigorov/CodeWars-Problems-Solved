def triple_trouble(one, two, three):
    result = ""
    for i in range(len(one)):
        for j in range(i, i + 1):
            for k in range(j , j + 1):
                result += one[i] + two[j] + three[k]

    return result


print(triple_trouble("aaa", "bbb", "ccc"))