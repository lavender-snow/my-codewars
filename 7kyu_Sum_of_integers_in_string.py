import re
def sum_of_integers_in_string(s):
    return sum([int(n) for n in re.sub("[^0-9]+"," ",s).split()])