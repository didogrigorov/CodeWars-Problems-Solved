def capitals(word):
    idx = []
    for i in range(len(word)):
        if word[i].isupper():
            idx.append(i)

    return idx

print(capitals("CodEWaRs"))