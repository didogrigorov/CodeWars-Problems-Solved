def second_symbol(s, symbol):

    if symbol not in s or s.count(symbol) == 1:
        return -1

    counter = 0
    if s != "":
        for i in range(0, len(s) + 1):
            if s[i] == symbol:
                counter += 1
                if counter == 2:
                    break

        return i
    else:
        return -1




# test function
symbol = 'G'
s = "GNSEOMPjTjgeHpwzKjLDoUtnXOOhugxtdqpPXSrRpkHUTzRGGqhxvBZxZl"
print(second_symbol(s, symbol))