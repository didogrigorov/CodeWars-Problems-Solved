def position(alphabet):
    return f"Position of alphabet: {ord(alphabet) % 96}"

alphabet = "d"
print(position(alphabet))