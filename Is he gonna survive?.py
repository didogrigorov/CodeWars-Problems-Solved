def hero(bullets, dragons):
    for num in range(1, bullets):
        if bullets == 0 or bullets < 0 or bullets == dragons:
            break
        bullets -= 2
        dragons -= 1

    if dragons == 0 or dragons < 0:
        return True
    else:
        return False