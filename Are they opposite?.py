def is_opposite(s1,s2):
    if s1 == "" and s2 == "":
        return False

    result = []

    for i in range(len(s1)):
        for j in range(i, i + 1):
            if s1[i].isupper() and s2[j].islower() or s1[i].islower() and s2[j].isupper():
                result.append(True)
            else:
                result.append(False)

    if all(result):
        return True
    else:
        return False


print(is_opposite("AB","Ab"))