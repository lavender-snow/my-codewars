def caffeineBuzz(n):
    res = ""
    if n % 3 == 0:
        if n % 4 == 0:
            res = "Coffee"
        else:
            res = "Java"
        if n % 2 == 0:
            res += "Script"
    else:
        res = "mocha_missing!"
    return res