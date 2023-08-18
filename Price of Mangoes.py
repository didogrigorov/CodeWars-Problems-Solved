def mango(quantity, price_per_mango):
    # Calculate the number of sets of 3 mangoes
    sets_of_3 = quantity // 3

    # Calculate the remaining mangoes after forming sets of 3
    remaining_mangoes = quantity % 3

    # Calculate the total cost based on the offer
    total_cost = (sets_of_3 * 2 + remaining_mangoes) * price_per_mango

    return total_cost

print(mango(9, 5))