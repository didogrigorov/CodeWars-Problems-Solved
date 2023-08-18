def better_than_average(class_points, your_points):
    all_points = 0
    for point in class_points:
        all_points += point
    average = (all_points + your_points) / len(class_points)
    if your_points >= average:
        return True
    else:
        return False

print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75))