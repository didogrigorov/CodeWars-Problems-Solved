def create_two_sets_of_equal_sum(n):
    sum_ = n * (n + 1) // 2

    if sum_ % 2:
        return []

    set_, sum_ = set(), sum_ // 2

    for x in range(n, 0, -1):
        if x < sum_:
            set_.add(x)
            sum_ -= x
        else:
            set_.add(sum_)
            break

    return set_, set(range(1, n + 1)) - set_

print(create_two_sets_of_equal_sum(4))