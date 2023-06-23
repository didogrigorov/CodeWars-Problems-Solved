def nb_year(p0, percent, aug, p):
    years = 0
    while p0 <= p:
        current = round(p0 * percent // 100) + aug
        p0 += current
        if p0 == p:
            break
        years += 1

    return years

print(nb_year(1500, 5, 100, 5000))