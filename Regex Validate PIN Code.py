import re
def validate_pin(pin):
    if "\n" in pin:
        return False
    pattern = r"^\d{4}$|^\d{6}$"
    result = re.match(pattern, pin)
    if result:
        return True
    else:
        return False


print(validate_pin("1234"))