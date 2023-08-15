from math import floor


def duty_free(price, discount, holiday_cost):
    discount_price = price * discount / 100
    bottles = holiday_cost / discount_price
    return floor(bottles)

print(duty_free(12,50,1000))