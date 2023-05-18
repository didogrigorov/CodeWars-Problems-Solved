def validate_hello(greetings):
    languages = {"hello": "english",
                 "ciao": "italian",
                 "salut": "french",
                 "hallo": "german",
                 "hola": "spanish",
                 "ahoj": "czech republic",
                 "czesc": "polish"}
    for key in languages.keys():
        if key in greetings.lower():
            return True

    return False

print(validate_hello("Ciao Bella!"))