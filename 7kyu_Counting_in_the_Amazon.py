def count_arara(n):
    res = []
    while n > 0:
        if n % 2 == 0:
            res.append("adak")
            n -=2
        else:
            res.append("anane")
            n -=1
        
    return " ".join(res[::-1])