def special_number(number):
    return "Special!!" if len([n for n in list(str(number)) if n in "6789"]) == 0 else "NOT!!"