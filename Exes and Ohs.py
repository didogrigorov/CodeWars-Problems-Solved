def xo(s):
    s = s.lower()
    if "x" not in s and "o" not in s:
        return True
    elif "x" not in s and "o" in s:
        return False
    elif "x" in s and "o" not in s:
        return False
    elif s == "":
        return True
    elif s == "x":
        return True
    elif s == "o":
        return True

    symbols = {}

    for item in s:
        if item not in symbols:
            symbols[item] = 0
        symbols[item] += 1

    if symbols["x"] == symbols["o"]:
        return True

    return False
print(xo("bXoZowi"))

# {'o': 2, 'x': 2}