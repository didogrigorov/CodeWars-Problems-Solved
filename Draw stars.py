def draw_stairs(n):
    output = ""
    for i in range(n):
        if i == n - 1:
            output += " " * i + "I"
            break
        output += " " * i + "I\n"

    return output

print(draw_stairs(3))