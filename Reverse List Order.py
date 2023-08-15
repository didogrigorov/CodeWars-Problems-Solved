def reverse_list(l):
    output = []
    for i in range(len(l) -1, -1, -1):
        output.append(l[i])

    return output

lst = [1,2,3,4]
print(reverse_list(lst))