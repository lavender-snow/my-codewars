import re
def remove(s):
    return re.sub("!+(\s|$)","\g<1>",s)