def who_is_paying(name):
    if len(name) > 2:
        return [name, name[0:2]]
    elif len(name) <= 2:
        return[name]
    else:
        return ['']

print(who_is_paying('I'))