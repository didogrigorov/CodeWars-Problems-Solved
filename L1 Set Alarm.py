def set_alarm(employed, vacation):
    if employed == True and vacation == True:
        return False
    elif employed == True and vacation == False:
        return True
    else:
        return False