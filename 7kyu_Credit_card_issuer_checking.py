import re

def get_issuer(number):
    
    s = str(number)
    if re.search("^3(4|7)",s) is not None and len(s) == 15:
        return "AMEX"
    elif s.startswith("6011") and len(s) == 16:
        return "Discover"
    elif re.search("^5[1-5]",s) and len(s) == 16:
        return "Mastercard"
    elif s[0] == "4" and (len(s) == 13 or len(s) == 16):
        return "VISA"
    return "Unknown"
    