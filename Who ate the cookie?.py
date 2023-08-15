def cookies(x):
    if type(x) == int:
        return "Who ate the cookie? It was Monica!"
    elif type(x) == float:
        return "Who ate the cookie? It was Monica!"
    elif type(x) == str:
        return "Who ate the cookie? It was Zach!"
    else:
        return "Who ate the cookie? It was the dog!"

print(cookies(True))