def color_2_grey(image):
    result = []
    for item in image:
        item_result = []
        for colors in item:
            calculation = sum(colors) / 3
            item_to_add = [round(calculation)]
            item_result.append(item_to_add * 3)
        result.append(item_result)

    return result


print(color_2_grey([
 [ [88,110,23], [56, 43, 124] ],
 [ [78, 152, 76], [64, 132, 200] ]
]))