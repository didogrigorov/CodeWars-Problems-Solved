def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18 and age >= 14:
        return "dring coke"
    elif 15 <= age < 21:
        return "drink beer"
    elif age >= 21:
        return "drink whisky"


print(people_with_age_drink(0))