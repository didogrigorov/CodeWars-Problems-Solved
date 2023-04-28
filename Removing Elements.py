# first algorithm
def remove_every_other(my_list):
    working_list = my_list[1:]
    mylst = working_list.copy()

    for i in range(len(working_list)):
        if i % 2 == 0:
            element = working_list[i]
            mylst.remove(element)


    return my_list[0:1] + mylst


# second algorithm
def remove_every_other(data):
    result = []
    for i in range(0, len(data), 2):
        result.append(data[i])

    return result



print(remove_every_other([{'Goodbye': 18}, {False: False}, [23], [23], [0]]))

#[{'Goodbye': 18}, [23], [0]]