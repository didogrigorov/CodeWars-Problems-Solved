def enough(cap, on, wait):
    passengers_space = cap - on
    if passengers_space >= wait:
        return 0
    else:
        return abs(wait - passengers_space)

print(enough(20, 5, 5))