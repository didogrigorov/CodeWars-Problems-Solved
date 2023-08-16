def seats_in_theater(tot_cols, tot_rows, col, row):
    people_per_row = tot_cols - col + 1
    remaining_rows = tot_rows - row
    return people_per_row * remaining_rows

print(seats_in_theater(1000, 1000, 1000, 1000))