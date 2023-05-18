def name_shuffler(str_):
    name = str_.split()
    return name[-1] + " " + name[0]

print(name_shuffler('Dido Grigorov'))