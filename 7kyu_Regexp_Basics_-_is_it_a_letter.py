import re
def is_letter(s):
    return re.fullmatch("[a-zA-Z]",s) is not None