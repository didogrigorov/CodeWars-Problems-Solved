def friend(x):
    friends = []
    for item in x:
        if len(item) == 4:
            friends.append(item)

    return friends

# def friend(x):
#     return [f for f in x if len(f) == 4]


print(friend(["Ryan", "Kieran", "Mark"]))