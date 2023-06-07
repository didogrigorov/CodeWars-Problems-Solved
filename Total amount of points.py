def points(games):
    all_points = 0

    for item in games:

        item = item.split(':')

        if item[0] > item[1]:
            all_points += 3
        elif item[0] == item[1]:
            all_points += 1

    return all_points


games = ['0:1','0:2','0:3','0:4','1:2','1:3','1:4','2:3','2:4','3:4']
print(points(games))
