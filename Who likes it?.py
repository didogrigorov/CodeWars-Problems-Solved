def likes(names):
    len_names = len(names)
    if len_names == 0:
        return "no one likes this"
    for i in range(len_names):
        if len_names == 1:
            return f"{names[i]} likes this"
        elif len_names == 2:
            return f"{names[i]} and {names[i + 1]} like this"
        elif len_names == 3:
            return f"{names[i]}, {names[i + 1]} and {names[i + 2]} like this"
        else:
            return f"{names[i]}, {names[i + 1]} and {len(names[2:])} others like this"


print(likes(["James", "Dean", "Dido", "John"]))